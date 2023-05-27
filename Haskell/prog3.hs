import Data.Char

main = do
  putStr "string: "
  cad <- getLine
  imprime cad

imprime [] = do
  putStr ""
imprime (x : resto) = do
  putStrLn $ [x] ++ " - " ++ (show (ord x))
  imprime resto