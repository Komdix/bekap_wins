matchPoints :: (Integer, Integer, Integer) -> (Integer, Integer, Integer) -> (Integer, Integer)
matchPoints (t1, c1, d1) (t2, c2, d2) = (points1, points2)
    where
        score_1 = (5 * t1) + (2 * c1) + (3 * d1) 
        score_2 = (5 * t2) + (2 * c2) + (3 * d2)
        bonus_1 = if t1 >= 4 
                  then 1 
                  else 0 
        bonus_2 = if t2 >= 4 
                  then 1 
                  else 0 
        lost_bonus_1 = if score_2 - score_1 >= 0 && score_2 - score_1 <= 7 
                 then 1 
                 else 0 
        lost_bonus_2 = if score_1 - score_2 >= 0 && score_1 - score_2 <= 7 
                 then 1 
                 else 0 

        points1 = if score_1 > score_2 
                   then 4 + bonus_1 + lost_bonus_1
                   else 
                  if score_1 == score_2 
                   then 2 + bonus_1 + lost_bonus_1 
                   else bonus_1 + lost_bonus_1
        points2 = if score_2 > score_1 
                   then 4 + bonus_2 + lost_bonus_2 
                   else 
                  if score_2 == score_1 
                   then 2 + bonus_2 + lost_bonus_2 
                   else bonus_2 + lost_bonus_2
