import Control.Monad

--- Monada Reader

type M = EnvReader
type Environment = [(Name, Value)]
newtype EnvReader a = Reader { runEnvReader :: Environment -> a }

--- Limbajul si  Interpretorul

instance Show a => Show (EnvReader a) where
  show x = show (runEnvReader x [])

instance Monad EnvReader where
  return = Reader . const
  ma >>= k = Reader $ \env -> let a = k $ runEnvReader ma env
                              in runEnvReader a env

instance Functor EnvReader where
  fmap = liftM

instance Applicative EnvReader where
  pure = return
  (<*>) = ap

showM :: Show a => M a -> String
showM = show

ask :: EnvReader Environment
ask = Reader id

local :: (Environment -> Environment) -> EnvReader a -> EnvReader a
local f ma = Reader $ \env -> runEnvReader ma (f env)

type Name = String

data Term = Var Name
          | Con Integer
          | Term :+: Term
          | Lam Name Term
          | App Term Term
  deriving (Show)

data Value = Num Integer
           | Fun (Value -> M Value)
           | Wrong

instance Show Value where
 show (Num x) = show x
 show (Fun _) = "<function>"
 show Wrong   = "<wrong>"

lookupM :: Name -> M Value
lookupM x = do
  env <- ask
  case lookup x env of
    Just v -> return v
    Nothing -> return Wrong

add :: Value -> Value -> M Value
add (Num i) (Num j) = return (Num  (i + j))
add _ _ = return Wrong

apply :: Value -> Value -> M Value
apply (Fun k) v = k v
apply _ _ = return Wrong

interp :: Term -> M Value
interp (Var x) = lookupM x
interp (Con i) = return $ Num i
interp (Lam x e) = do
  env <- ask
  return $ Fun $ \v -> local (const ((x, v) : env)) (interp e)
interp (t1 :+: t2) = do
  v1 <- interp t1
  v2 <- interp t2
  add v1 v2
interp (App t1 t2) = do
  f <- interp t1
  v <- interp t2
  apply f v

test :: Term -> String
test t = showM $ interp t

pgm :: Term
pgm = App
  (Lam "y"
    (App
      (App
        (Lam "f"
          (Lam "y"
            (App (Var "f") (Var "y"))
          )
        )
        (Lam "x"
          (Var "x" :+: Var "y")
        )
      )
      (Con 3)
    )
  )
  (Con 4)

pgm1:: Term
pgm1 = App
          (Lam "x" ((Var "x") :+: (Var "x")))
          ((Con 10) :+:  (Con 11))

-- test pgm
-- test pgm1
