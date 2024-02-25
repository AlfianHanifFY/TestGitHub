module Halo where
    halo :: IO()
    halo = putStrLn "Hallo Dunia !"

    fib :: Int -> Int
    fib n
        | n == 0 = 0
        | n == 1 = 1
        | n == 2 = 1
        | otherwise = fib(n-2) + fib(n-1)