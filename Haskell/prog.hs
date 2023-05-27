{-
    Tabla ASCII
-}
import Data.Char
import Text.Printf

main = do
  putStrLn "Tabla del codigo ASCII"
  tabla 32 127 0

tabla i n x 
  |i > n = do
    putStrLn ""
  |otherwise = do
    printf "%3d"
    putStr $ ": " ++ [chr i] ++ "  "
    if (mod (i+1) 5 == 0)
        then do
        |  putStrLn ""
        else do
        |  putStrLn ""
    tabla (i+1) n (x+1)