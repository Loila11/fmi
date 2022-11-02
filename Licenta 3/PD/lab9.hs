import Data.Char (toUpper)
import Data.List
import Data.List.Split
import Data.Char

prelStr strin = map toUpper strin

ioString = do
            strin <- getLine
            putStrLn $ "Intrare\n" ++ strin
            let  strout = prelStr strin
            putStrLn $ "Iesire"
            putStrLn strout


prelNo noin =  sqrt noin
ioNumber = do
            noin  <- readLn :: IO Double
            putStrLn $ "Intrare\n" ++ (show noin)
            let  noout = prelNo noin
            putStrLn $ "Iesire"
            print noout



inoutFile = do
               sin <- readFile "Input.txt"
               putStrLn $ "Intrare\n" ++ sin
               let sout = prelStr sin
               putStrLn $ "Iesire\n" ++ sout
               writeFile "Output.txt" sout

-- ex 1
findMax :: Int -> Int -> [String] -> IO ()
findMax 0 _ names = do
  print "Cea mai mare varsta: "
  print (unwords names)
findMax n maxAge names = do
  name <- getLine
  age <- readLn :: IO Int

  if age > maxAge
    then findMax (n - 1) age [name]
    else if age == maxAge
      then findMax (n - 1) maxAge (name : names)
      else findMax (n - 1) maxAge names

ex1 = do
  n <- readLn :: IO Int
  findMax n 0 []

-- ex 2
ex2 = do
  sin <- readFile "ex2.in"
  let people = map (\x -> (x !! 0, read (x !! 1) :: Int)) $
               map (splitOn ", ") $ init $ splitOn "\n" sin
  let maxAge = foldr (\(_, b) c -> max b c) 0 people
  let oldestPeople = map fst $ filter (\(_, b) -> b == maxAge) people

  print $ "Cea mai mare varsta: " ++ intercalate ", " oldestPeople ++
          " (" ++ show maxAge ++ " ani)"

-- ex 3
-- a
isPalindrome = do
  x <- getLine
  if x == reverse x then print "Numarul este palindrom"
    else print "Numarul nu este palindrom"

-- b
f :: Int -> IO ()
f 0 = print ""
f n = do
  isPalindrome
  f (n - 1)
