treeFind :: (Eq a) => a -> BinTree a -> Maybe [TreeDirection]
treeFind value Empty = Nothing
treeFind value (Node v left right)
    | value == v = Just []
    | otherwise = if isJust (treeFind value left)
                    then Just (LeftChild : fromJust (treeFind value left))
                    else if isJust (treeFind value right)
                        then Just (RightChild : fromJust (treeFind value right))
                        else Nothing