popCount :: Integer -> Integer
popCount 0 = 0
popCount x = (x mod 2) + popCount (x div 2)