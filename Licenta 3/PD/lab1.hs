import Data.List

-- L1.1

-- L1.2
myInt = 55555555555555555555555555555555555555555555555555555555555
double :: Integer -> Integer
double x = x + x

triple x = double x + x

-- L1.3
s = permutations "abc"

-- L1.4
maxim :: Integer -> Integer -> Integer
maxim x y =
  if (x > y)
    then x
    else y

max3 x y z =
  let
    u = maxim x y
  in
    maxim u z

maxim3 :: Integer -> Integer -> Integer -> Integer
maxim3 x y z =
  if (x >= y && x >= z)
    then x
    else if (y > z)
      then y
      else z

maxim4 :: Integer -> Integer -> Integer -> Integer -> Integer
maxim4 x y z v =
  let u = maxim3 x y z
  in maxim u v

testMaxim4 :: Integer -> Integer -> Integer -> Integer -> Bool
testMaxim4 x y z v =
  let u = maxim4 x y z v
  in if (u >= x && u >= y && u >= z && u >= v)
      then True
      else False

-- L1.5

-- L1.6
-- i
squareSum :: Integer -> Integer -> Integer
squareSum x y = x * x + y * y

-- ii
parity :: Integer -> String
parity x =
  if (mod x 2 == 0)
    then "par"
    else "impar"
    
prity :: Integer -> String
prity x
  | mod x 4 == 0 = "0"
  | mod x 4 == 1 = "1"
  | otherwise = "altceva"

-- iii
fact :: Integer -> Integer
fact x = case x of
  0 -> 1
  otherwise -> x * fact (x - 1)

-- iv
biggerThan :: Integer -> Integer -> Bool
biggerThan x y =
  if (x > 2 * y)
    then True
    else False
