import Numeric.Natural

-- 1
produsRec :: [Integer] -> Integer
produsRec [] = 1
produsRec (x:xs) = x * produsRec xs

produsFold :: [Integer] -> Integer
produsFold s = foldr (*) 1 s

-- 2
andRec :: [Bool] -> Bool
andRec [] = True
andRec (x:xs) = x && andRec xs


andFold :: [Bool] -> Bool
andFold s = foldr (&&) True s

-- 3
concatRec :: [[a]] -> [a]
concatRec [] = []
concatRec (x:xs) = x ++ concatRec xs

concatFold :: [[a]] -> [a]
concatFold s = foldr (++) [] s

-- 4
rmChar :: Char -> String -> String
rmChar _ [] = []
rmChar c (x:xs) = if c == x then rmChar c xs
                    else x : rmChar c xs

rmCharsRec :: String -> String -> String
rmCharsRec [] s2 = s2
rmCharsRec _ [] = []
rmCharsRec (c:s1) s2 = rmCharsRec s1 (rmChar c s2)

test_rmchars :: Bool
test_rmchars = rmCharsRec ['a'..'l'] "fotbal" == "ot"

rmCharsFold :: String -> String -> String
rmCharsFold s1 s2 = foldr rmChar s2 s1


-- II
logistic :: Num a => a -> a -> Natural -> a
logistic rate start = f
  where
    f 0 = start
    f n = rate * f (n - 1) * (1 - f (n - 1))


logistic0 :: Fractional a => Natural -> a
logistic0 = logistic 3.741 0.00079
ex1 :: Natural
ex1 = 20


ex20 :: Fractional a => [a]
ex20 = [1, logistic0 ex1, 3]

ex21 :: Fractional a => a
ex21 = head ex20

ex22 :: Fractional a => a
ex22 = ex20 !! 2

ex23 :: Fractional a => [a]
ex23 = drop 2 ex20

ex24 :: Fractional a => [a]
ex24 = tail ex20


ex31 :: Natural -> Bool
ex31 x = x < 7 || logistic0 (ex1 + x) > 2

ex32 :: Natural -> Bool
ex32 x = logistic0 (ex1 + x) > 2 || x < 7
ex33 :: Bool
ex33 = ex31 5

ex34 :: Bool
ex34 = ex31 7

ex35 :: Bool
ex35 = ex32 5

ex36 :: Bool
ex36 = ex32 7
