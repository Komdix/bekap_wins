binaryAdd :: [Bool] -> [Bool] -> ([Bool], Bool)
binaryAdd [] [] = ([], False)

binaryAdd (x : rest_x) (y : rest_y) = (sumdone : sumkek, overflow)
    where
     (done, smth) = fullAdder x y overflow_idk
     (kek, overflow) = binaryAdd rest_ rest_y




binaryAdd :: [Bool] -> [Bool] -> ([Bool], Bool)
binaryAdd [] [] = ([], False)  -- Base case: both input lists are empty

binaryAdd (x:restX) (y:restY) = (sumBit : sumRest, carryOut)
  where
    (sumBit, carryIn) = fullAdder x y carryOut
    (sumRest, carryOut) = binaryAdd restX restY

[Float] -> Bool -> [Double]