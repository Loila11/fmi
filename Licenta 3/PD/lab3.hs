import   Data.List

-- L3.1 Încercati sa gasiti valoarea expresiilor de mai jos si
-- verificati raspunsul gasit de voi în interpretor:
{-
[x^2 | x <- [1 .. 10], x `rem` 3 == 2]
[(x, y) | x <- [1 .. 5], y <- [x .. (x+2)]]
[(x, y) | x <- [1 .. 3], let k = x^2, y <- [1 .. k]]
[x | x <- "Facultatea de Matematica si Informatica", elem x ['A' .. 'Z']]
[[x .. y] | x <- [1 .. 5], y <- [1 .. 5], x < y ]

-}

factori :: Int -> [Int]
factori n = [x | x <- [1..(abs n)], rem (abs n) x == 0]

prim :: Int -> Bool
prim n = length (factori n) == 2

numerePrime :: Int -> [Int]
numerePrime n = [x | x <- [1..(abs n)], prim x]

-- L3.2 Testati si sesizati diferenta:
-- [(x,y) | x <- [1..5], y <- [1..3]]
-- zip [1..5] [1..3]

myzip3 :: [a] -> [b] -> [c] -> [(a, b, c)]
myzip3 l1 l2 l3 = [(x, y, z) | ((x, y), z) <- zip(zip l1 l2) l3]


--------------------------------------------------------
----------FUNCTII DE NIVEL INALT -----------------------
--------------------------------------------------------
aplica2 :: (a -> a) -> a -> a
--aplica2 f x = f (f x)
--aplica2 f = f.f
--aplica2 f = \x -> f (f x)
aplica2  = \f x -> f (f x)

-- L3.3
{-

map (\ x -> 2 * x) [1 .. 10]
map (1 `elem` ) [[2, 3], [1, 2]]
map ( `elem` [2, 3] ) [1, 3, 4, 5]

-}

-- firstEl [ ('a', 3), ('b', 2), ('c', 1)]
firstEl :: [(a, b)] -> [a]
firstEl l = map fst l

-- sumList [[1, 3],[2, 4, 5], [], [1, 3, 5, 6]]
sumList :: [[Integer]] -> [Integer]
sumList l = map sum l

-- prel2 [2,4,5,6]
prel2 :: [Integer] -> [Integer]
prel2 l = map f l
  where
    f x
      | even x = div x 2
      | otherwise = x * 2

-- L3.4
f1 :: Char -> [String] -> [String]
f1 x s = filter (x `elem`) s

f2 :: [Integer] -> [Integer]
f2 s = map (^2) (filter odd s)

f3 :: [Integer] -> [Integer]
f3 s = map ((^2).fst) (filter (odd.snd) (zip s [0..]))

f4 :: [String] -> [String]
f4 s = map (filter (`elem` "aeiouAEIOU")) s

-- L3.5
mymap :: (a -> b) -> [a] -> [b]
mymap f [] = []
mymap f (h:t) = f h : mymap f t

myfilter :: (a -> Bool) -> [a] -> [a]
myfilter f [] = []
myfilter f (h:t)
    | f h = h : myfilter f t
    | otherwise = myfilter f t

-- numerePrimeCiur :: Int -> [Int]

-- 1
ordonataNat :: [Int] -> Bool
ordonataNat [] = True
ordonataNat [x] = True
ordonataNat (x : xs) = and (ordonataNat xs : [x <= y | y <- xs])

-- 2
ordonataNat1 :: [Int] -> Bool
ordonataNat1 [] = True
ordonataNat1 [x] = True
ordonataNat1 (x : xs) = case xs of
  (y : xxs) -> if x <= y then ordonataNat1 xs
                else False

-- 3
ordonata :: [a] -> (a -> a -> Bool) -> Bool
ordonata [] f = True
ordonata [x] f = True
ordonata (x : s) f = and (ordonata s f : [f x y | y <- s])

(*<*) :: (Integer, Integer) -> (Integer, Integer) -> Bool
(*<*) (a, b) (c, d) = a < c && b < d

-- 4
compuneList :: (b -> c) -> [(a -> b)] -> [(a -> c)]
compuneList f lf = map ((f) . ) lf

aplicaList :: a -> [(a -> b)] -> [b]
aplicaList x lf = map ($x) lf

myzip3' :: [a] -> [b] -> [c] -> [(a, b, c)]
myzip3' l1 l2 l3 = map (\((a, b), c) -> (a, b, c)) (zip (zip l1 l2) l3)
