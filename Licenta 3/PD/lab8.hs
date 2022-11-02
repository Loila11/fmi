import Test.QuickCheck
import Data.Maybe
import Data.Char

double :: Int -> Int
double x = 2 * x
triple :: Int -> Int
triple x = 3 * x
penta :: Int -> Int
penta x = 5 * x

test :: Int -> Bool
test x = (double x + triple x) == (penta x)

testF :: Int -> Bool
testF x = (double x + 3) == (penta x)

myLookUp :: Int -> [(Int,String)]-> Maybe String
myLookUp _ [] = Nothing
myLookUp x (xs:s)
  | x == fst xs = Just (snd xs)
  | otherwise = myLookUp x s

testLookUp :: Int -> [(Int,String)] -> Bool
testLookUp x s = (myLookUp x s) == (lookup x s)

testLookUpCond :: Int -> [(Int,String)] -> Property
testLookUpCond n list = n > 0 && n `div` 5 == 0 ==> testLookUp n list

myLookUp' :: Int -> [(Int,String)]-> Maybe String
myLookUp' x s =
  if (y == Nothing || y == (Just ""))
    then y else Just $ toUpper (head z) : (tail z)
  where
    z = fromMaybe "" y
    y = myLookUp x s

testLookUp' :: Int -> [(Int,String)] -> Bool
testLookUp' x s = (myLookUp' x s) == (lookup x s)

testLookUpCond' :: Int -> [(Int,String)] -> Property
testLookUpCond' x s = (and $ map (\x ->
                  ((toUpper (head (snd x))) : (tail (snd x))) == (snd x)) s) ==>
                  testLookUp' x s

quicksort :: Ord a => [a] -> [a]
quicksort []     = []
quicksort (x:xs) = smalls ++ [x] ++ bigs
                 where smalls = quicksort [n | n <- xs, n <= x]
                       bigs   = quicksort [n | n <- xs, n > x]

testQuicksortA :: Ord a => [a] -> Bool
testQuicksortA s = quicksort s == quicksort (quicksort s)

testQuicksortB :: Ord a => [a] -> Bool
testQuicksortB s = quicksort s == quicksort (reverse s)

testQuicksortC :: Int -> Bool
testQuicksortC n = quicksort [1..n] == [1..n]

testQuicksortD :: Ord a => [a] -> Bool
testQuicksortD s = length (quicksort s) == length s

quicksortBuggy :: Ord a => [a] -> [a]
quicksortBuggy []     = []
quicksortBuggy (x:xs) = smalls ++ [x] ++ bigs
                where smalls = quicksortBuggy [n | n <- xs, n < x] -- oops
                      bigs   = quicksortBuggy [n | n <- xs, n > x]

testQuicksortBuggyA :: Ord a => [a] -> Bool
testQuicksortBuggyA s = quicksortBuggy s == quicksortBuggy (quicksortBuggy s)

testQuicksortBuggyB :: Ord a => [a] -> Bool
testQuicksortBuggyB s = quicksortBuggy s == quicksortBuggy (reverse s)

testQuicksortBuggyC :: Int -> Bool
testQuicksortBuggyC n = quicksortBuggy [1..n] == [1..n]

testQuicksortBuggyD :: Ord a => [a] -> Bool
testQuicksortBuggyD s = length (quicksortBuggy s) == length s

data ElemIS = I Int | S String
     deriving (Show,Eq)

instance Arbitrary ElemIS where
  arbitrary = do
    x <- arbitrary
    y <- arbitrary
    elements [I x, S y]

myLookUpElem :: Int -> [(Int,ElemIS)]-> Maybe ElemIS
myLookUpElem _ [] = Nothing
myLookUpElem x (xs:s)
  | x == fst xs = Just (snd xs)
  | otherwise = myLookUpElem x s

testLookUpElem :: Int -> [(Int,ElemIS)] -> Bool
testLookUpElem x s = (myLookUpElem x s) == (lookup x s)
