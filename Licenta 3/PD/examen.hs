import Control.Monad

data Binar = Leaf Integer | Node Binar Binar

type LeafCode = [Bool]

tree :: Binar
tree = Node (Node (Leaf 3) (Leaf 4)) (Node (Leaf 1) (Leaf 4))

data Writer a = Writer { output ::[LeafCode], value :: a }

findPath :: Binar -> Integer -> LeafCode -> [LeafCode]
findPath (Leaf x) value path
  | x == value = [path]
  | otherwise = [[]]
findPath (Node t1 t2) value path =
  filter (not . null) $ (findPath t1 value (path ++ [True])) ++
                        (findPath t2 value (path ++ [False]))

leafCodes :: Binar  -> Integer -> Writer ()
leafCodes tree value = Writer (findPath tree value []) ()

instance Monad Writer where
    return x = Writer [] x
    (Writer y x) >>= f = Writer (y ++ (output (f x))) (value $ f x)

instance Functor Writer where
  fmap = liftM
instance Applicative Writer where
  pure = return
  (<*>) = ap
