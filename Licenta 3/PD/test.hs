import Data.Char
-- pun si ce librarii am inclus pt fiecare problema
-- ex 1
f :: String -> [String] -> String
f c [] = []
f c [x] = x
f c (x:s) = sumStrings x $ sumStrings c $ f c s
  where
    sumStrings :: String -> String -> String
    sumStrings [] s = s
    sumStrings (x:xs) s = x : sumStrings xs s

-- ex 2
f2 :: [[Int]] -> Int -> Int
f2 m n = length $ filter (> n) $ map (foldr (+) 0) $ map (filter even) m

-- ex 3
type Name = String
type Quantity= Int
data Ingredient = Ing Name Quantity
    deriving Show
data Receipe = R [Ingredient]
   deriving Show

r1 = R [Ing "faina" 500, Ing "oua" 4, Ing "zahar" 500]
r2 = R [Ing "fAIna" 500, Ing "zahar" 500, Ing "Oua" 4]
r3 = R [Ing "fAIna" 500, Ing "zahar" 500, Ing "Oua" 55]

eqIngredient :: Ingredient -> Ingredient -> Bool
eqIngredient (Ing x1 q1) (Ing x2 q2) =
  (map toLower x1 == map toLower x2) && (q1 == q2)

instance Eq Ingredient where
  (==) = eqIngredient

eqReceipe :: Receipe -> Receipe -> Bool
eqReceipe (R []) (R []) = True
eqReceipe (R []) s = False
eqReceipe s (R []) = False
eqReceipe (R (x:xs)) (R s) =
  if elem x s then (eqReceipe (R xs) (R z)) else False
  where
    -- elimin doar prima aparitie a ingredientului x in reteta s
    y = fst $ head $ filter ((== x) . snd) $ zip [1..] s
    z = (take (y - 1) s) ++ (drop y s)

instance Eq Receipe where
  (==) = eqReceipe
