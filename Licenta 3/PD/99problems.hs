import Data.List
import Data.List.Split
import Data.Char
import System.Random
import Control.Monad

-- 1. Find the last element of a list.
myLast :: [a] -> a
myLast s = case s of
  [] -> error "The list is empty"
  [x] -> x
  (_ : xs) -> myLast xs

-- 2. Find the last but one element of a list.
myButLast :: [a] -> a
myButLast s = case s of
  [] -> error "The list is empty"
  [x] -> error "The list is too short"
  [x, y] -> x
  (_ : xs) -> myButLast xs

-- 3. Find the K'th element of a list.
-- The first element in the list is number 1.
elementAt :: [a] -> Int -> a
elementAt s n = case s of
  [] -> error "There are not enough elements in the list"
  (x : xs) -> case n of
    1 -> x
    _ -> elementAt xs (n - 1)

-- 4. Find the number of elements of a list.
myLength :: [a] -> Int
myLength s = case s of
  [] -> 0
  [x] -> 1
  (_ : xs) -> 1 + myLength xs

-- 5. Reverse a list.
myReverse :: [a] -> [a]
myReverse s = case s of
  [x] -> [x]
  (x : xs) -> myReverse xs ++ [x]

-- 6. Find out whether a list is a palindrome.
-- A palindrome can be read forward or backward; e.g. (x a m a x).
isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome s = (s == myReverse s)

-- 7. Flatten a nested list structure.
-- Transform a list, possibly holding lists as elements into a `flat' list
-- by replacing each list with its elements (recursively).
data NestedList a = Elem a | List [NestedList a]

flatten :: NestedList a -> [a]
flatten (List []) = []
flatten (Elem x) = [x]
flatten (List (x : xs)) = flatten x ++ flatten (List xs)

-- 8. Eliminate consecutive duplicates of list elements.
-- If a list contains repeated elements they should be replaced with a single
-- copy of the element. The order of the elements should not be changed.
compress :: (Eq a) => [a] -> [a]
compress s = case s of
  [] -> []
  (x : []) -> [x]
  (x : y : xs) ->
    if x == y then compress (y : xs)
      else x : compress (y : xs)

-- 9. Pack consecutive duplicates of list elements into sublists. If a list
-- contains repeated elements they should be placed in separate sublists.
pack :: (Eq a) => [a] -> [[a]]
pack = foldr func []
  where
    func x [] = [[x]]
    func x (y : xs) =
      if x == (head y) then (x : y) : xs
        else [x] : y : xs

-- 10. Run-length encoding of a list. Use the result of problem P09 to
-- implement the so-called run-length encoding data compression method.
-- Consecutive duplicates of elements are encoded as lists (N E) where N is the
-- number of duplicates of the element E.
encode :: Eq a => [a] -> [(Int, a)]
encode s = [(length x, head x) | x <- pack s]

-- 11. Modify the result of problem 10 in such a way that if an element has no
-- duplicates it is simply copied into the result list. Only elements with
-- duplicates are transferred as (N E) lists.
data ListItem a = Single a | Multiple Int a
  deriving (Show)

encodeModified :: Eq a => [a] -> [ListItem a]
encodeModified s = [y | x <- pack s,
                        let y = if (length x) == 1 then Single (head x)
                                  else Multiple (length x) (head x)]

-- 12. Given a run-length code list generated as specified in problem 11,
-- construct its uncompressed version.
-- decodeModified (Single a) = [a]
-- decodeModified (Multiple l x) = [replicate l x]
-- decodeModified s = [y | x <- s, ]
toTuple :: ListItem a -> (Int, a)
toTuple (Single a) = (1, a)
toTuple (Multiple l a) = (l, a)

decode :: (Int, a) -> [a]
decode (l, x) = replicate l x

decodeModified :: [ListItem a] -> [a]
decodeModified s = foldl (++) [] (map decode (map toTuple s))

-- 13. Implement the so-called run-length encoding data compression method
-- directly. I.e. don't explicitly create the sublists containing the
-- duplicates, as in problem 9, but only count them. As in problem P11, simplify
-- the result list by replacing the singleton lists (1 X) by X.
encodeDirect :: Eq a => [a] -> [ListItem a]
encodeDirect list = encode' [(x, 1) | x <- list]
  where
    encode' :: Eq a => [(a, Int)] -> [ListItem a]
    encode' [] = []
    encode' [x]
      | snd x == 1 = [Single (fst x)]
      | otherwise = [Multiple (snd x) (fst x)]
    encode' (x:y:s)
      | fst x == fst y = encode' ((fst x, snd x + 1) : s)
      | otherwise = encode' [x] ++ encode' (y:s)

-- 14. Duplicate the elements of a list.
dupli :: [a] -> [a]
dupli [] = []
dupli (x:s) = [x, x] ++ dupli s

-- 15. Replicate the elements of a list a given number of times.
repli :: [a] -> Int -> [a]
repli [] _ = []
repli (x:s) n = (replicate n x) ++ repli s n

-- 16. Drop every N'th element from a list.
dropEvery :: [a] -> Int -> [a]
dropEvery [] _ = []
dropEvery s n = take (n - 1) s ++ dropEvery (drop n s) n

-- 17. Split a list into two parts; the length of the first part is given.
split :: [a] -> Int -> ([a], [a])
split s n = (take n s, drop n s)

-- 18. Extract a slice from a list.
-- Given two indices, i and k, the slice is the list containing the elements
-- between the i'th and k'th element of the original list (both limits
-- included). Start counting the elements with 1.
slice :: [a] -> Int -> Int -> [a]
slice s i k = drop (i - 1) (take k s)

-- 19. Rotate a list N places to the left.
rotate :: [a] -> Int -> [a]
rotate s n = drop k s ++ take k s
  where
    k = mod (length s + n) (max (length s) 1)

-- 20. Remove the K'th element from a list.
removeAt :: Int -> [a] -> (a, [a])
removeAt n s = (s !! (n - 1), take (n - 1) s ++ drop n s)

-- 21. Insert an element at a given position into a list.
insertAt :: a -> [a] -> Int -> [a]
insertAt c s n = take (n - 1) s ++ [c] ++ drop (n - 1) s

-- 22. Create a list containing all integers within a given range.
range :: Int -> Int -> [Int]
range i j = [i..j]

-- 23. Extract a given number of randomly selected elements from a list.
rnd_select :: [a] -> Int -> [a]
rnd_select list n = [list !! p | p <-
                      take n $ nub $ randomRs (0, length list - 1) (mkStdGen n)]

rnd_select' :: [a] -> Int -> [a]
rnd_select' list 0 = []
rnd_select' list n = [list !! p] ++
                    rnd_select' [fst x | x <- zip list [0..], snd x /= p] (n - 1)
  where
    p = fst $ randomR (0, length list - 1) (mkStdGen n)

-- 24. Lotto: Draw N different random numbers from the set 1..M.
diff_select :: Int -> Int -> [Int]
diff_select n m = rnd_select [1..m] n

diff_select' :: Int -> Int -> [Int]
diff_select' n m = take n $ nub $ randomRs (1, m) (mkStdGen n)

-- 25. Generate a random permutation of the elements of a list.
rnd_permu :: [a] -> [a]
rnd_permu list = rnd_select list (length list)

-- 26. Generate the combinations of K distinct objects chosen from the N
-- elements of a list
combinations :: Int -> [a] -> [[a]]
combinations _ [] = []
combinations 1 s = map (:[]) s
combinations n (x:s) = addElem x (combinations (n - 1) s) ++ combinations n s
  where
    addElem :: a -> [[a]] -> [[a]]
    addElem c s = [c:x | x <- s]

-- 27. Group the elements of a set into disjoint subsets.
group' :: Eq a => [Int] -> [a] -> [[[a]]]
group' [] _ = [[]]
group' (n:ns) s = [x : y | x <- combinations n s, y <- group' ns (compl x s)]
  where
    compl :: Eq a => [a] -> [a] -> [a]
    compl s' s = [x | x <- s, not (elem x s')]

-- 28. Sorting a list of lists according to length of sublists.
-- a) We suppose that a list contains elements that are lists themselves. The
-- objective is to sort the elements of this list according to their length.
lsort :: Eq a => [[a]] -> [[a]]
lsort [] = []
lsort [x] = [x]
lsort (x:s) = if length x <= length m then x : lsort (delete x s)
              else m : lsort (x : delete m s)
      where
        m = head (lsort s)

-- alternativ
lsort' :: [[a]] -> [[a]]
lsort' = sortBy (\x y -> compare (length x) (length y))

-- b) Again, we suppose that a list contains elements that are lists themselves.
-- But this time the objective is to sort the elements of this list according
-- to their length frequency
lfsort :: [[a]] -> [[a]]
lfsort s = [fst x | x <- sortBy (\xs ys -> compare (snd xs) (snd ys)) y]
  where
    y = [(x, sum [1 | z <- s, length z == length x]) | x <- s]

-- 31. Determine whether a given integer number is prime.
isPrime :: Int -> Bool
isPrime n = length [x | x <- [1..n], mod n x == 0] == 2

-- 32. Determine the greatest common divisor of two positive integer numbers.
-- Use Euclid's algorithm.
myGCD :: Int -> Int -> Int
myGCD a b
  | b == 0 = abs a
  | otherwise = myGCD b (mod a b)

-- 33. Determine whether two positive integer numbers are coprime.
-- Two numbers are coprime if their greatest common divisor equals 1.
coprime :: Int -> Int -> Bool
coprime a b = myGCD a b == 1

-- 34. Calculate Euler's totient function phi(m).
-- Euler's so-called totient function phi(m) is defined as the number of
-- positive integers r (1 <= r < m) that are coprime to m.
totient :: Int -> Int
totient 1 = 1
totient m = sum [1 | x <- [1..m], coprime x m]

-- 35. Determine the prime factors of a given positive integer.
-- Construct a flat list containing the prime factors in ascending order.
primeFactors :: Int -> [Int]
primeFactors n = primeFactor n 2
  where
    primeFactor :: Int -> Int -> [Int]
    primeFactor n x
      | n < x = []
      | isPrime x && mod n x == 0 = x : primeFactor (div n x) x
      | otherwise = primeFactor n (x + 1)

-- 36. Determine the prime factors of a given positive integer.
-- Construct a list containing the prime factors and their multiplicity.
prime_factors_mult :: Int -> [(Int, Int)]
prime_factors_mult n = map swap $ encode $ primeFactors n
  where
    swap (x, y) = (y, x)

-- 37. Calculate Euler's totient function phi(m) (improved).
phi :: Int -> Int
phi m = product [(p - 1) * p ^ (m - 1) | (p, m) <- prime_factors_mult m]

-- 39. A list of prime numbers.
-- Given a range of integers by its lower and upper limit, construct a list of
-- all prime numbers in that range.
primesR :: Int -> Int -> [Int]
primesR a b = [x | x <- [a..b], isPrime x]

-- 40.Goldbach's conjecture.
goldbach :: Int -> (Int, Int)
goldbach n = head [(x, n - x) | x <- [2..n], isPrime x, isPrime (n - x)]

-- 41. Given a range of integers by its lower and upper limit, print a list of
-- all even numbers and their Goldbach composition.
goldbachList :: Int -> Int -> [(Int, Int)]
goldbachList a b = [goldbach x | x <- [a..b], even x]

-- In most cases, if an even number is written as the sum of two prime numbers,
-- one of them is very small. Very rarely, the primes are both bigger than
-- say 50. Try to find out how many such cases there are in the range 2..3000.
goldbachList' :: Int -> Int -> Int -> [(Int, Int)]
goldbachList' a b n = [x | x <- goldbachList a b, fst x > n, snd x > n]

-- 46. Define predicates and/2, or/2, nand/2, nor/2, xor/2, impl/2 and equ/2
-- (for logical equivalence) which succeed or fail according to the result of
-- their respective operations.
and' :: Bool -> Bool -> Bool
and' a b = a && b

or' :: Bool -> Bool -> Bool
or' a b = a || b

nand' :: Bool -> Bool -> Bool
nand' a b = not (a && b)

nor' :: Bool -> Bool -> Bool
nor' a b = a == False && b == False

xor' :: Bool -> Bool -> Bool
xor' a b = (a || b) && (a /= b)

impl' :: Bool -> Bool -> Bool
impl' a b = a <= b

eq' :: Bool -> Bool -> Bool
eq' a b = a == b

-- Now, write a predicate table/3 which prints the truth table of a given
-- logical expression in two variables.
table :: (Bool -> Bool -> Bool) -> IO()
table f = mapM_ putStrLn [show a ++ " " ++ show b  ++ " " ++ show (f a b) |
            a <- [True, False], b <- [True, False]]

-- 47. Truth tables for logical expressions (2).
infixl 4 `or'`
infixl 6 `and'`

-- 48. Truth tables for logical expressions (3).
infixl 4 `nor'`
infixl 5 `xor'`
infixl 6 `nand'`
infixl 3 `eq'`

tablen :: Int -> ([Bool] -> Bool) -> IO()
tablen n f = mapM_ putStrLn
              [unwords
                [show (line !! p) | p <- [0..(n - 1)]] ++ " " ++ (show (f line))
              | line <- table]
  where
    table = replicateM n [True, False]

-- 49. Gray codes.
gray :: Int -> [String]
gray 0 = []
gray 1 = ["0", "1"]
gray n = ["0" ++ c | c <- s] ++ ["1" ++ c | c <- s]
  where
    s = gray (n - 1)

-- 50. Huffman codes.
huffman :: [(Char, Int)] -> [(Char, String)]
huffman s = huff s ""
  where
    score :: [(Char, Int)] -> Int
    score s = sum [snd x | x <- s]

    allCuts :: [(Char, Int)] -> [[(Char, Int)]]
    allCuts s = [take i s | i <- [1..(length s)]]

    bestCutScore :: [(Char, Int)] -> Int
    bestCutScore s = minimum [abs (score s - 2 * score x) | x <- allCuts s]

    bestCut :: [(Char, Int)] -> [(Char, Int)]
    bestCut s = head [x | x <- allCuts s,
                          abs (score s - 2 * score x) == bestCutScore s]

    huff :: [(Char, Int)] -> String -> [(Char, String)]
    huff [] _ = []
    huff [x] p = [(fst x, p)]
    huff s p
      | score xs <= score ys = (huff xs (p ++ "0")) ++ (huff ys (p ++ "1"))
      | otherwise = (huff xs (p ++ "1")) ++ (huff ys (p ++ "0"))
      where
        xs = bestCut s
        ys = drop (length xs) s

-- Binary Trees
data Tree a = Empty | Branch a (Tree a) (Tree a)
              deriving (Show, Eq)

leaf x = Branch x Empty Empty

tree1 = Branch 'a' (Branch 'b' (leaf 'd')
                                (leaf 'e'))
                    (Branch 'c' Empty
                                (Branch 'f' (leaf 'g')
                                            Empty))

-- 54. Check whether a given term represents a binary tree
-- Din definitie

-- 55. Construct completely balanced binary trees
-- In a completely balanced binary tree, the following property holds for every
-- node: The number of nodes in its left subtree and the number of nodes in its
-- right subtree are almost equal, which means their difference is not greater
-- than one.
-- Write a function cbal-tree to construct completely balanced binary trees for
-- a given number of nodes. The predicate should generate all solutions via
-- backtracking. Put the letter 'x' as information into all nodes of the tree.
cbalTree :: Int -> [Tree Char]
cbalTree 0 = [Empty]
cbalTree n = [Branch 'x' left right | i <- [q..(q + r)],
                                      left <- cbalTree i,
                                      right <- cbalTree (n - i - 1)]
            where
              (q, r)  = quotRem (n - 1) 2

-- 56.Symmetric binary trees
-- Let us call a binary tree symmetric if you can draw a vertical line through
-- the root node and then the right subtree is the mirror image of the left
-- subtree. Write a predicate symmetric/1 to check whether a given binary tree
-- is symmetric. Hint: Write a predicate mirror/2 first to check whether one
-- tree is the mirror image of another. We are only interested in the structure,
-- not in the contents of the nodes.
mirror :: Tree a -> Tree a -> Bool
mirror Empty Empty = True
mirror Empty _ = False
mirror _ Empty = False
mirror (Branch _ l1 r1) (Branch _ l2 r2) = mirror l1 r2 && mirror r1 l2

symmetric :: Tree a -> Bool
symmetric Empty = True
symmetric (Branch _ left right) = mirror left right

-- 57. Binary search trees (dictionaries)
-- Use the predicate add/3, developed in chapter 4 of the course, to write a
-- predicate to construct a binary search tree from a list of integer numbers.
add :: Int -> Tree Int -> Tree Int
add y Empty = leaf y
add y (Branch x left right) = if y > x then Branch x left (add y right)
                                else Branch x (add y left) right

construct :: [Int] -> Tree Int
construct [] = Empty
construct (x:s) = add x (construct s)

-- alternativ:
construct' :: [Int] -> Tree Int
construct' s = foldl (flip add) Empty s

-- 58. Generate-and-test paradigm
-- Apply the generate-and-test paradigm to construct all symmetric, completely
-- balanced binary trees with a given number of nodes.
symCbalTrees :: Int -> [Tree Char]
symCbalTrees n = [x | x <- cbalTree n, symmetric x]

-- 59. Construct height-balanced binary trees
-- In a height-balanced binary tree, the following property holds for every
-- node: The height of its left subtree and the height of its right subtree are
-- almost equal, which means their difference is not greater than one.
-- Construct a list of all height-balanced binary trees with the given element
-- and the given maximum height.
hbalTree :: Char -> Int -> [Tree Char]
hbalTree _ 0 = [Empty]
hbalTree c 1 = [leaf c]
hbalTree c n = nub [Branch c left right |
                    (i, j) <- [(n - 1, n - 1), (n - 1, n - 2), (n - 2, n - 1)],
                    left <- hbalTree c i,
                    right <- hbalTree c j]

-- 60. Construct height-balanced binary trees with a given number of nodes.
hbalTreeNodes :: Char -> Int -> [Tree Char]
hbalTreeNodes c n = [t | i <- [minHeight .. maxHeight],
                         t <- hbalTree c i,
                         countNodes t == n]
              where
                fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

                minNodes = fibs !! (n + 2) - 1
                maxNodes = 2 ^ n - 1

                minHeight = ceiling (logBase 2 (fromIntegral (n + 1)))
                maxHeight = length (takeWhile (<= n + 1) fibs) - 3

                countNodes Empty = 0
                countNodes (Branch _ left right) = countNodes left +
                                                   countNodes right +
                                                   1

-- Example tree.
tree4 = Branch 1 (Branch 2 Empty (Branch 4 Empty Empty))
                 (Branch 2 Empty Empty)

-- 61. Count the leaves of a binary tree.
count_leaves :: Tree a -> Int
count_leaves Empty = 0
count_leaves (Branch _ Empty Empty) = 1
count_leaves (Branch _ left right) = count_leaves left + count_leaves right

-- 61A. Collect the leaves of a binary tree in a list.
leaves :: Tree a -> [a]
leaves Empty = []
leaves (Branch x Empty Empty) = [x]
leaves (Branch _ left right) = leaves left ++ leaves right

-- 62. Collect the internal nodes of a binary tree in a list.
internals :: Tree a -> [a]
internals Empty = []
internals (Branch _ Empty Empty) = []
internals (Branch x left right) = [x] ++ internals left ++ internals right

-- 62B. Collect the nodes at a given level in a list.
atlevel :: Tree a -> Int -> [a]
atlevel (Branch x _ _) 1 = [x]
atlevel (Branch _ left right) n = (atlevel left (n - 1)) ++
                                  (atlevel right (n - 1))

-- 63. Construct a complete binary tree.
completeBinaryTree :: Int -> Tree Char
completeBinaryTree 0 = Empty
completeBinaryTree 1 = Branch 'x' Empty Empty
completeBinaryTree n = Branch 'x'
                        (completeBinaryTree (n - 1 - n'))
                        (completeBinaryTree n')
  where
    n' = div (n - 1) 2

isCompleteBinaryTree :: Eq a => Tree a -> Bool
isCompleteBinaryTree Empty = True
isCompleteBinaryTree tree = sameFormat tree (completeBinaryTree (count tree))
  where
    count :: Tree a -> Int
    count Empty = 0
    count (Branch _ left right) = 1 + (count left) + (count right)

    sameFormat :: Eq a => Eq b => Tree a -> Tree b -> Bool
    sameFormat Empty Empty = True
    sameFormat Empty _ = False
    sameFormat _ Empty = False
    sameFormat (Branch _ left1 right1) (Branch _ left2 right2) =
      (sameFormat left1 left2) && (sameFormat right1 right2)

-- 64. Given a binary tree as the usual Prolog term t(X,L,R) (or nil).
-- As a preparation for drawing the tree, a layout algorithm is required
-- to determine the position of each node in a rectangular grid.
-- In this layout strategy, the position of a node v is obtained by the
-- following two rules:
-- x(v) is equal to the position of the node v in the inorder sequence
-- y(v) is equal to the depth of the node v in the tree
-- Write a function to annotate each node of the tree with a position,
-- where (1,1) in the top left corner or the rectangle bounding the drawn tree.
tree64 = Branch 'n'
                (Branch 'k'
                        (Branch 'c'
                                (Branch 'a' Empty Empty)
                                (Branch 'h'
                                        (Branch 'g'
                                                (Branch 'e' Empty Empty)
                                                Empty
                                        )
                                        Empty
                                )
                        )
                        (Branch 'm' Empty Empty)
                )
                (Branch 'u'
                        (Branch 'p'
                                Empty
                                (Branch 's'
                                        (Branch 'q' Empty Empty)
                                        Empty
                                )
                        )
                        Empty
                )

layout :: Tree a -> Tree (a, (Int, Int))
layout t = layout' t 1 0
  where
    count :: Tree a -> Int
    count Empty = 0
    count (Branch _ left right) = 1 + (count left) + (count right)

    layout' :: Tree a -> Int -> Int -> Tree (a, (Int, Int))
    layout' Empty _ _ = Empty
    layout' (Branch x left right) n m = Branch (x, (head_pos, n))
                                        (layout' left (n + 1) m)
                                        (layout' right (n + 1) head_pos)
      where
        head_pos = count left + m + 1

-- 65. Find out the rules and write the corresponding function.
-- nu se incarca imaginea ca sa pot sa deduc :(

-- 66. La fel ca la 65 :(

-- 67. A string representation of binary trees
-- Somebody represents binary trees as strings of the following type:
-- a(b(d,e),c(,f(g,)))
-- A. Write a Prolog predicate which generates this string representation.
treeToString :: Tree Char -> String
treeToString Empty = ""
treeToString (Branch x Empty Empty) = [x]
treeToString (Branch x left right) = [x] ++ "(" ++ (treeToString left) ++
                                     "," ++ (treeToString right) ++ ")"

-- TODO
-- B. Write a predicate which does this inverse.
stringToTree :: String -> Tree Char
stringToTree = undefined
-- stringToTree "" = return Empty
-- stringToTree [x] = return $ Branch x Empty Empty
-- stringToTree list = aux list >>= \("", t) -> return t
--   where
--     aux a@(x:xs)
--       | x == ',' || x == ')' = return (a, Empty)
--     aux (x:y:xs)
--       | y == ',' || y == ')' = return (y:xs, Branch x Empty Empty)
--       | y == '(' = do (',':xs', l) <- aux xs
--                       (')':xs'', r) <- aux xs'
--                       return (xs'', Branch x l r)
--     aux _ = fail "bad parse"

-- C. Finally, combine the two predicates in a single predicate tree_string/2
-- which can be used in both directions.
type TreeC = Tree Char
data TreeString = Var1 String | Var2 TreeC
  deriving (Show, Eq)

tree_string :: TreeString -> TreeString
tree_string (Var2 t) = Var1 (treeToString t)
tree_string (Var1 s) = Var2 (stringToTree s)

-- 68. Preorder and inorder sequences of binary trees.
-- A. Write predicates preorder/2 and inorder/2.
preorder :: Tree Char -> String
preorder Empty = ""
preorder (Branch x left right) = [x] ++ (preorder left) ++ (preorder right)

inorder :: Tree Char -> String
inorder Empty = ""
inorder (Branch x left right) = (inorder left) ++ [x] ++ (inorder right)

-- B. Can you use preorder/2 from problem part a) in the reverse direction
preorder' :: String -> Tree Char
preorder' "" = Empty
preorder' [x] = Branch x Empty Empty
preorder' (x:s) = Branch x (preorder' (take n1 s)) (preorder' (drop n1 s))
  where
    n = length s
    n1 = div n 2

-- C. If both the preorder sequence and the inorder sequence of the nodes of a
-- binary tree are given, then the tree is determined unambiguously. Write a
-- predicate pre_in_tree/3 that does the job.
tree68 = Branch 'a'
                    (Branch 'b'
                                (Branch 'd'
                                            Empty
                                            Empty
                                )
                                (Branch 'e'
                                            Empty
                                            Empty
                                )
                    )
                    (Branch 'c'
                                Empty
                                (Branch 'f'
                                            (Branch 'g'
                                                        Empty
                                                        Empty
                                            )
                                            Empty
                                )
                    )

pre_in_order :: String -> String -> Tree Char
pre_in_order "" "" = Empty
pre_in_order [x] _ = leaf x
pre_in_order (x:s) inord = Branch x
                           (pre_in_order preord_left inord_left)
                           (pre_in_order preord_right inord_right)
  where
    inord_left = takeWhile (/= x) inord
    inord_right = drop (length inord_left + 1) inord
    preord_left = takeWhile (`elem` inord_left) s
    preord_right = drop (length preord_left) s

-- 69. Dotstring representation of binary trees.
tree2ds :: Tree Char -> String
tree2ds Empty = "."
tree2ds (Branch x left right) = [x] ++ (tree2ds left) ++ (tree2ds right)

bfs :: String -> (Tree Char, String)
bfs ('.' : s) = (Empty, s)
bfs (x : '.' : '.': s) = (leaf x, s)
bfs (x : s) = (Branch x left right, rest2)
  where
    (left, rest) = bfs s
    (right, rest2) = bfs rest

ds2tree :: String -> Tree Char
ds2tree s = fst (bfs s)

tree_dotstring :: TreeString -> TreeString
tree_dotstring (Var1 s) = Var2 (ds2tree s)
tree_dotstring (Var2 t) = Var1 (tree2ds t)

-- Multiway Trees
data MTree a = Node a [MTree a]
        deriving (Eq, Show)

tree71 = Node 'a' []

tree72 = Node 'a' [Node 'b' []]

tree73 = Node 'a' [Node 'b' [Node 'c' []]]

tree74 = Node 'b' [Node 'd' [], Node 'e' []]

tree75 = Node 'a' [
                Node 'f' [Node 'g' []],
                Node 'c' [],
                Node 'b' [Node 'd' [], Node 'e' []]
                ]
-- 70A. Check whether a given term represents a multiway tree.
-- Din definitie

-- 70B. Count the nodes of a multiway tree.
nnodes :: MTree a -> Int
nnodes (Node _ t) = 1 + foldr (+) 0 (map nnodes t)

-- 70C. Tree construction from a node string.
mTreeToString :: MTree Char -> String
mTreeToString (Node x t) = [x] ++ foldr (++) [] (map mTreeToString t) ++ "^"

stringToMTree :: String -> MTree Char
stringToMTree (x:"^") = Node x []
stringToMTree (x:s) = Node x z
  where
    y = map fst $ filter ((== 0) . snd) $ zip [0..] $
        scanl (+) 0 $ map (\x -> if x == '^' then -1 else 1) s
    z = map stringToMTree $ map (\(a,b) -> take (b - a) $ drop a s) $
        zip (init y) (tail y)

-- 71. Determine the internal path length of a tree.
ipl :: MTree a -> Int
ipl t = ipl' 0 t
  where
    ipl' n (Node _ t) = foldr (+) n $ map (ipl' (n + 1)) t

-- 72. Construct the bottom-up order sequence of the tree nodes.
bottom_up :: MTree Char -> String
bottom_up (Node x t) = foldr (++) [x] $ map bottom_up t

-- 73. Lisp-like tree representation.
tree_ltl :: MTree Char -> String
tree_ltl (Node x []) = [x]
tree_ltl (Node x t) = display s
  where
    s = "(" ++ [x] ++ " " ++ foldr (++) "" (map tree_ltl t) ++ ")"

    display :: String -> String
    display [] = []
    display [x] = [x]
    display (x:y:xs)
      | (isAlpha x && isAlpha y) || (x == ')' && not (elem y " )")) ||
        (not (elem x " (") && y == '(') = [x] ++ " " ++ display (y:xs)
      | otherwise = [x] ++ display (y:xs)
