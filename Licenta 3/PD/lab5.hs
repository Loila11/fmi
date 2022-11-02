import Data.Char
import Data.List


-- 1.
rotate :: Int -> [Char] -> [Char]
rotate n s
  | n < 0 = error "n < 0"
  | n >= length(s) = error "n e prea mare"
  | n == 0 = s
rotate n (x : s) = rotate (n - 1) (s ++ [x])

-- 2.
prop_rotate :: Int -> String -> Bool
prop_rotate k str = rotate (l - m) (rotate m str) == str
                        where l = length str
                              m = if l == 0 then 0 else k `mod` l

-- 3.
makeKey :: Int -> [(Char, Char)]
makeKey n = zip ['A'..'Z'] (rotate n ['A'..'Z'])

-- 4.
lookUp :: Char -> [(Char, Char)] -> Char
lookUp c [] = c
lookUp c (x:s)
  | c == (fst x) = snd x
  | otherwise = lookUp c s

-- 5.
encipher :: Int -> Char -> Char
encipher n c = lookUp c (makeKey n)

-- 6.
normalize :: String -> String
normalize [] = []
normalize (x:s)
  | not (elem x ['a'..'z'] || elem x ['A'..'Z'] || elem x ['1'..'9']) =
    normalize s
  | isLower x = toUpper x : normalize s
  | otherwise = x : normalize s

-- 7.
encipherStr :: Int -> String -> String
encipherStr n s = map (encipher n) (normalize s)

-- 8.
reverseKey :: [(Char, Char)] -> [(Char, Char)]
reverseKey [] = []
reverseKey (x:s) = (snd x, fst x) : reverseKey s

-- 9.
decipher :: Int -> Char -> Char
decipher n c = lookUp c (reverseKey (makeKey n))

decipherStr :: Int -> String -> String
decipherStr n s = map (decipher n) s
