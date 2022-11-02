#!/usr/bin/env stack
-- stack --resolver lts-13.7 script

main :: IO ()
main = return ()

-- curs
f x = g x + z
  where
    g x = 2 * x
    z = x - 1

x1 = y where y = 8
x2 = let y = 8 in y

h1 x | x == 0 = x
     | x == 1 = y + 1
     | otherwise = y
  where y = x * x

h2 x = case x of
              0 -> 0
              1 -> y + 1
              _ -> y
  where y = x * x

h (x) = (x - 1)
dist (e1, e2) = abs(e1 - e2)
