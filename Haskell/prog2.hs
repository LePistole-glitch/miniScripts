main = do
  putStr "De una cadena: "
  cad <- getLine
  if esCadMin cad
    then do
      putStrLn "es minuscula"
    else do
      putStrLn "Caracter no valido"

esCadMin [] = True
esCadMin (X )