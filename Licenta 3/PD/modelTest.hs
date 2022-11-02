-- orice rezolvare corecta cu alta metoda decat cea precizata
-- reprezinta jumate din punctaj

-- ex 1
sfChr :: Char -> Bool
sfChr c
  | (c == '.') || (c == '?') || (c == '!') || (c == ':') = True
  | otherwise = False

countSentences :: String -> Int
countSentences "" = 0
countSentences (x:s)
  | sfChr x == True = 1 + (countSentences s)
  | otherwise = countSentences s

countSentences' :: String -> Int
countSentences' s = sum [1 | x <- s, elem x ".?!:"]

-- ex 2
liniiN :: [[Int]] -> Int -> Bool
liniiN m n = foldr (&&) True $ map (> 0) $ foldr (++) [] $
             filter ((== n) . length) m

-- ex 3
data Punct = Pt [Int]
             deriving Show

data Arb = Vid | F Int | N Arb Arb
          deriving Show

class ToFromArb a where
           toArb :: a -> Arb
           fromArb :: Arb -> a

instance ToFromArb Punct where
  toArb (Pt []) = Vid
  toArb (Pt (x:s)) = N (F x) (toArb (Pt s))

  fromArb Vid = Pt []
  fromArb (F x) = Pt [x]
  fromArb (N arb1 arb2) = Pt (left ++ right)
    where
      Pt left = fromArb arb1
      Pt right = fromArb arb2
