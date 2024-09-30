turn :: Direction -> Instruction -> Direction
turn North TurnLeft  = West
turn North TurnRight = East
turn East TurnLeft   = North
turn East TurnRight  = South
turn South TurnLeft  = East
turn South TurnRight = West
turn West TurnLeft   = South
turn West TurnRight  = North
turn dir _             = dir


move :: State -> Instruction -> State
move (State x y North) (Forward n) = State x (y + n) North
move (State x y East) (Forward n)  = State (x + n) y East
move (State x y South) (Forward n) = State x (y - n) South
move (State x y West) (Forward n)  = State (x - n) y West
move state _                       = state 


executeInstructions :: [Instruction] -> State -> State
executeInstructions [] state = state  
executeInstructions (i:is) (State x y dir) =
    executeInstructions is (move (State x y newDir) i)
    where
      newDir = turn dir i