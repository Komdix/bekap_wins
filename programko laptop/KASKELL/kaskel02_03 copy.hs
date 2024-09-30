localMinima :: Ord a => [a] -> [a]
localMinima [] = []
localMinima [_] = []
localMinima [x, y] = []
localMinima (x:y:z:zs) =
    if y < x && y < z
        then y : localMinima (y:z:zs)
        else localMinima (y:z:zs)