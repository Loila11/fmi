import Data.List (nub)
import Data.Maybe (fromJust)

data Fruct
    = Mar String Bool
    | Portocala String Int
      deriving(Show)


ionatanFaraVierme = Mar "Ionatan" False
goldenCuVierme = Mar "Golden Delicious" True
portocalaSicilia10 = Portocala "Sanguinello" 10
listaFructe = [Mar "Ionatan" False, Portocala "Sanguinello" 10, Portocala "Valencia" 22, Mar "Golden Delicious" True, Portocala "Sanguinello" 15, Portocala "Moro" 12, Portocala "Tarocco" 3, Portocala "Moro" 12, Portocala "Valencia" 2, Mar "Golden Delicious" False, Mar "Golden" False, Mar "Golden" True]


ePortocalaDeSicilia :: Fruct -> Bool
ePortocalaDeSicilia (Mar _ _) = False
ePortocalaDeSicilia (Portocala s _)
  | s == "Tarocco" || s == "Moro" || s == "Sanguinello" = True
  | otherwise = False



test_ePortocalaDeSicilia1 = ePortocalaDeSicilia (Portocala "Moro" 12) == True
test_ePortocalaDeSicilia2 = ePortocalaDeSicilia (Mar "Ionatan" True) == False

nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia s = sum [y | (Portocala x y) <- s,
                            ePortocalaDeSicilia (Portocala x y)]

test_nrFeliiSicilia = nrFeliiSicilia listaFructe == 52

nrMereViermi :: [Fruct] -> Int
nrMereViermi s = sum [1 | (Mar _ x) <- s, x == True]

test_nrMereViermi = nrMereViermi listaFructe == 2

type NumeA = String
type Rasa = String
data Animal = Pisica NumeA | Caine NumeA Rasa

vorbeste :: Animal -> String
vorbeste (Pisica _) = "Meow!"
vorbeste (Caine _ _) = "Woof!"

rasa :: Animal -> Maybe String
rasa (Caine _ rasa) = Just rasa
rasa (Pisica _) = Nothing

type Nume = String
data Prop
    = Var Nume
    | F
    | T
    | Not Prop
    | Prop :|: Prop
    | Prop :&: Prop
    | Prop :->: Prop
    | Prop :<->: Prop
    deriving (Eq, Read)
infixr 2 :|:
infixr 3 :&:

p1 :: Prop
p1 = (Var "P" :|: Var "Q") :&: (Var "P" :&: Var "Q")

p2 :: Prop
p2 = (Var "P" :|: Var "Q")  :&: ((Not (Var "P")) :&: (Not (Var "Q")))

p3 :: Prop
p3 = (Var "P" :&: (Var "Q" :|: Var "R")) :&:
      (((Not (Var "P")) :|: (Not (Var "Q"))) :&:
        ((Not (Var "P")) :|: (Not (Var "R"))))

instance Show Prop where
  show p = case p of
    F -> "False"
    T -> "True"
    Var x -> x
    Not x -> "(~" ++ show x ++ ")"
    x :|: y -> "(" ++ show x ++ "|" ++ show y ++ ")"
    x :&: y -> "(" ++ show x ++ "&" ++ show y ++ ")"
    x :->: y -> "(" ++ show x ++ ")->(" ++ show y ++ ")"
    x :<->: y -> "(" ++ show x ++ ")<->(" ++ show y ++ ")"

test_ShowProp :: Bool
test_ShowProp = show (Not (Var "P") :&: Var "Q") == "((~P)&Q)"

type Env = [(Nume, Bool)]

impureLookup :: Eq a => a -> [(a,b)] -> b
impureLookup a = fromJust . lookup a

eval :: Prop -> Env -> Bool
eval p s = case p of
  T -> True
  F -> False
  Var x -> impureLookup x s
  Not x -> not (eval x s)
  x :|: y -> (eval x s) || (eval y s)
  x :&: y -> (eval x s) && (eval y s)
  x :->: y -> (eval x s) <= (eval y s)
  x :<->: y -> (eval x s) == (eval y s)


test_eval = eval  (Var "P" :|: Var "Q") [("P", True), ("Q", False)] == True


variabile :: Prop -> [Nume]
variabile p = case p of
  T -> []
  F -> []
  Var x -> [x]
  Not x -> variabile x
  x :|: y -> nub (variabile x ++ variabile y)
  x :&: y -> nub (variabile x ++ variabile y)
  x :->: y -> nub (variabile x ++ variabile y)
  x :<->: y -> nub (variabile x ++ variabile y)

test_variabile = variabile (Not (Var "P") :&: Var "Q") == ["P", "Q"]

envs :: [Nume] -> [Env]
envs [] = [[]]
envs (x:s) = [(x, b) : l | b <- [False, True], l <- envs s]


test_envs =
      envs ["P", "Q"]
      ==
      [ [ ("P",False)
        , ("Q",False)
        ]
      , [ ("P",False)
        , ("Q",True)
        ]
      , [ ("P",True)
        , ("Q",False)
        ]
      , [ ("P",True)
        , ("Q",True)
        ]
      ]

satisfiabila :: Prop -> Bool
satisfiabila p = or [eval p x | x <- envs (variabile p)]

test_satisfiabila1 = satisfiabila (Not (Var "P") :&: Var "Q") == True
test_satisfiabila2 = satisfiabila (Not (Var "P") :&: Var "P") == False

valida :: Prop -> Bool
valida p = not (satisfiabila (Not p))

test_valida1 = valida (Not (Var "P") :&: Var "Q") == False
test_valida2 = valida (Not (Var "P") :|: Var "P") == True
