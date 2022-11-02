{- Monada Maybe este definita in GHC.Base

instance Monad Maybe where
  return = Just
  Just va  >>= k   = k va
  Nothing >>= _   = Nothing


instance Applicative Maybe where
  pure = return
  mf <*> ma = do
    f <- mf
    va <- ma
    return (f va)

instance Functor Maybe where
  fmap f ma = pure f <*> ma
-}

(<=<) :: (a -> Maybe b) -> (c -> Maybe a) -> c -> Maybe b
f <=< g = (\ x -> g x >>= f)

-- ex 1
f1 :: Int -> Maybe Int
f1 n = if n > 10 then Just n else Just (n * n)

f2 :: Int -> Maybe Int
f2 n = if even n then Just n else Nothing

f3 :: Int -> Maybe Int
f3 n = Just (3 * n)

asoc :: (Int -> Maybe Int) -> (Int -> Maybe Int) -> (Int -> Maybe Int) -> Int -> Bool
asoc f g h x = ((h <=< (g <=< f)) x) == (((h <=< g) <=< f) x)

testAsoc :: Int -> Bool
testAsoc x = asoc f1 f2 f3 x

-- ex 2
pos :: Int -> Bool
pos x = if (x >= 0) then True else False

foo :: Maybe Int ->  Maybe Bool
foo mx =  mx >>= (\x -> Just (pos x))

foo' :: Maybe Int ->  Maybe Bool
foo' mx = do
  x <- mx
  Just (pos x)

-- ex 3
addM :: Maybe Int -> Maybe Int -> Maybe Int
addM mx my = mx >>= (\x -> my >>= \y -> Just (x + y))

addM1 :: Maybe Int -> Maybe Int -> Maybe Int
addM1 Nothing _ = Nothing
addM1 _ Nothing = Nothing
addM1 (Just x) (Just y) = Just (x + y)

addM2 :: Maybe Int -> Maybe Int -> Maybe Int
addM2 mx my = do
  x <- mx
  y <- my
  Just (x + y)

testAdd :: Maybe Int -> Maybe Int -> Bool
testAdd mx my = (addM1 mx my) == (addM2 mx my) && (addM1 mx my) == (addM mx my)

-- ex 4
cartesian_product xs ys = xs >>= ( \x -> (ys >>= \y-> return (x,y)))
cartesian_product' xs ys = do
  x <- xs
  y <- ys
  return (x, y)

prod f xs ys = [f x y | x <- xs, y<-ys]
prod' f xs ys = do
  x <- xs
  y <- ys
  f x y

myGetLine :: IO String
myGetLine = getChar >>= \x ->
  if x == '\n' then return []
  else myGetLine >>= \xs -> return (x:xs)

myGetLine' :: IO String
myGetLine' = do
  x <- getChar
  if x == '\n' then return []
    else do
      xs <- myGetLine
      return (x:xs)

-- ex 5
prelNo noin = sqrt noin
ioNumber = do
  noin <- readLn :: IO Float
  putStrLn $ "Intrare\n" ++ (show noin)
  let noout = prelNo noin
  putStrLn $ "Iesire"
  print noout

ioNumber' = (readLn :: IO Float) >>= \noin ->
  (putStrLn $ "Intrare\n" ++ (show noin)) >>
  (putStrLn $ "Iesire") >>
  (print (prelNo noin))
