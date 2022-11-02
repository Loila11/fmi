
-- la nevoie decomentati liniile urmatoare:

import Data.Char
import Data.List


---------------------------------------------
-------RECURSIE: FIBONACCI-------------------
---------------------------------------------

fibonacciCazuri :: Integer -> Integer
fibonacciCazuri n
  | n < 2     = n
  | otherwise = fibonacciCazuri (n - 1) + fibonacciCazuri (n - 2)

fibonacciEcuational :: Integer -> Integer
fibonacciEcuational 0 = 0
fibonacciEcuational 1 = 1
fibonacciEcuational n =
    fibonacciEcuational (n - 1) + fibonacciEcuational (n - 2)

{-| @fibonacciLiniar@ calculeaza @F(n)@, al @n@-lea element din secvența
Fibonacci în timp liniar, folosind funcția auxiliară @fibonacciPereche@ care,
dat fiind @n >= 1@ calculează perechea @(F(n-1), F(n))@, evitănd astfel dubla
recursie. Completați definiția funcției fibonacciPereche.

Indicație:  folosiți matching pe perechea calculată de apelul recursiv.
-}
fibonacciLiniar :: Integer -> Integer
fibonacciLiniar 0 = 0
fibonacciLiniar n = snd (fibonacciPereche n)
  where
    fibonacciPereche :: Integer -> (Integer, Integer)
    fibonacciPereche 1 = (0, 1)
    fibonacciPereche n = (a, b)
      where
        (a, b) = fibonacciPereche (n - 1)
      -- let (a, b) = fibonacciPereche (n - 1)
      -- in (a, a + b)
      -- let p = fibonacciPereche(n - 1)
      -- in (snd p, snd p + fst p)


---------------------------------------------
----------RECURSIE PE LISTE -----------------
---------------------------------------------
semiPareRecDestr :: [Int] -> [Int]
semiPareRecDestr l
  | null l    = l
  | even h    = h `div` 2 : t'
  | otherwise = t'
  where
    h = head l
    t = tail l
    t' = semiPareRecDestr t

semiPareRecEq :: [Int] -> [Int]
semiPareRecEq [] = []
semiPareRecEq (h:t)
  | even h    = h `div` 2 : t'
  | otherwise = t'
  where t' = semiPareRecEq t

---------------------------------------------
----------DESCRIERI DE LISTE ----------------
---------------------------------------------
semiPareComp :: [Int] -> [Int]
semiPareComp l = [ x `div` 2 | x <- l, even x ]


-- L2.2
inInterval :: Int -> Int -> [Int] -> [Int]
inInterval lo hi list = filter (>= lo) $ filter ( <= hi) list

inIntervalRec :: Int -> Int -> [Int] -> [Int]
inIntervalRec lo hi list
  | null list = []
  | x >= lo && x <= hi = (x : inIntervalRec lo hi xs)
  | otherwise = inIntervalRec lo hi xs
    where
      (x : xs) = list

inIntervalComp :: Int -> Int -> [Int] -> [Int]
inIntervalComp lo hi xs = [x | x <- xs, x >= lo && x <= hi]

-- L2.3
pozitive :: [Int] -> Int
pozitive l = length $ filter (> 0) l

pozitiveRec :: [Int] -> Int
pozitiveRec l
  | null l = 0
  | x > 0 = 1 + pozitiveRec xs
  | otherwise = pozitiveRec xs
    where
      (x : xs) = l


pozitiveComp :: [Int] -> Int
pozitiveComp l = sum [1 | x <- l, x > 0]

-- L2.4
pozitiiImpare :: [Int] -> [Int]
pozitiiImpare l = map fst $ filter (odd . snd) $ zip [0..] l

pozitiiImpareRec :: [Int] -> [Int]
pozitiiImpareRec l = pozitiiImpare l 0
  where
    pozitiiImpare :: [Int] -> Int -> [Int]
    pozitiiImpare l poz = case l of
      [] -> []
      (x : xs)
        | even x -> pozitiiImpare xs (poz + 1)
        | otherwise -> (poz : pozitiiImpare xs (poz + 1))


pozitiiImpareComp :: [Int] -> [Int]
pozitiiImpareComp l = [ind | (ind, el) <- zip l [0 ..], odd el]


-- L2.5
multDigits :: String -> Int
multDigits sir = foldl (*) 1 $ map digitToInt $ filter isDigit sir

multDigitsRec :: String -> Int
multDigitsRec sir = case sir of
  [] -> 1
  (x : xs) -> case isDigit x of
    True -> digitToInt x * multDigitsRec xs
    False -> multDigitsRec xs

multDigitsComp :: String -> Int
multDigitsComp sir =  product [digitToInt x | x <- sir, isDigit x]

-- L2.6
discount :: [Float] -> [Float]
discount list = filter (< 200) $ map (\x -> x - 25 / 100 * x) list

discountRec :: [Float] -> [Float]
discountRec [] = []
discountRec (x : xs)
    | disc < 200 = (disc : discountRec xs)
    | otherwise = discountRec xs
      where
        disc = x - (x * 25 / 100)

discountComp :: [Float] -> [Float]
discountComp list = [x - x * 25 / 100 | x <- list, x - x * 25 / 100 < 200]
