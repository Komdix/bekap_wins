removeStartingByA :: Filesystem -> Filesystem
removeStartingByA (File name) =
    if startsWithA name 
    then Nothing 
    else Just (File name)
removeStartingByA (Folder name content) =
    if startsWithA name 
    then Nothing 
    else Just (Folder name (removeStartingByA content))  

startsWithA :: String -> Bool
startsWithA (x:_) = x == 'a'
startsWithA _ = False