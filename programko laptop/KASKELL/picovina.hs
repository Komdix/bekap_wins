-- check :: (Eq a) => [a]
-- check = zipwith

-- append :: [a] -> [a] -> [a]
-- append x [] = x
-- append [] x = x
-- append (xf:x) y = xf: append x y

-- sqroots :: [Double] -> [Double]
-- sqroots [] = []
-- sqroots (xf:x) = if xf > 0 then sqrt xf: sqroots x  else xf: sqroots x

-- largestNumber :: [Integer] -> Integer
-- largestNumber x = maximum x

largestNumber :: [Integer] -> Integer
largestNumber [x] = x 
largestNumber (xf:y:x) = largestNumber ((max xf y) :  x)


-- jebem ti mater skurveny haskell jebem ti mater skurveny haskell 
-- jebem ti mater skurveny haskell jebem ti mater skurveny haskell
-- jebem ti mater skurveny haskell jebem ti mater skurveny haskell
-- jebem ti mater skurveny haskell jebem ti mater skurveny haskell

