matchPoints :: (Integer, Integer, Integer) -> (Integer, Integer, Integer) -> (Integer, Integer)
matchPoints (t1, c1, d1) (t2, c2, d2) =
    let score1 = (5 * t1) + (2 * c1) + (3 * d1) -- Body za tým 1
        score2 = (5 * t2) + (2 * c2) + (3 * d2) -- Body za tým 2
        bonusPoints1 = if t1 >= 4 then 1 else 0 -- Bonusové body za tým 1
        bonusPoints2 = if t2 >= 4 then 1 else 0 -- Bonusové body za tým 2
        losingBonus1 = if score2 - score1 >= 0 && score2 - score1 <= 7 then 1 else 0 -- Body za prohru o nejvýše 7 bodů pro tým 1
        losingBonus2 = if score1 - score2 >= 0 && score1 - score2 <= 7 then 1 else 0 -- Body za prohru o nejvýše 7 bodů pro tým 2
    in (if score1 > score2 then 4 + bonusPoints1 + losingBonus1 else if score1 == score2 then 2 + bonusPoints1 + losingBonus1 else bonusPoints1 + losingBonus1, 
        if score2 > score1 then 4 + bonusPoints2 + losingBonus2 else if score2 == score1 then 2 + bonusPoints2 + losingBonus2 else bonusPoints2 + losingBonus2)
