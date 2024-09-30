from ib111 import week_02  # noqa


# Napište funkci, která zjistí, kolik bude pracovních dnů v roce
# ‹year›, přičemž parametr ‹day_of_week› udává, na který den v týdnu
# v tomto roce padne první leden. Dny v týdnu mají hodnoty 0–6
# počínaje pondělím s hodnotou 0.

# České státní svátky jsou:
#
# │  datum │ svátek                                         │
# ├┄┄┄┄┄┄┄▻┼◅┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
# │   1.1. │ Den obnovy samostatného českého státu          │0
# │      — │ Velký pátek                                    │
# │      — │ Velikonoční pondělí                            │
# │   1.5. │ Svátek práce                                   │120
# │   8.5. │ Den vítězství                                  │127
# │   5.7. │ Den slovanských věrozvěstů Cyrila a Metoděje   │185
# │   6.7. │ Den upálení mistra Jana Husa                   │186
# │  28.9. │ Den české státnosti                            │271
# │ 28.10. │ Den vzniku samostatného československého státu │301
# │ 17.11. │ Den boje za svobodu a demokracii               │321
# │ 24.12. │ Štědrý den                                     │358
# │ 25.12. │ 1. svátek vánoční                              │359
# │ 26.12. │ 2. svátek vánoční                              │360

# Přestupné roky: v některých letech se na konec února přidává 29.
# den. Jsou to roky, které jsou dělitelné čtyřmi, s výjimkou těch,
# které jsou zároveň dělitelné 100 a nedělitelné 400.

# Čistou funkci ‹first_day› můžete použít k tomu, abyste zjistili,
# na který den v týdnu padne 1. leden daného roku. Např.
# ‹first_day(2001)› vrátí nulu, protože rok 2001 začínal pondělím.


def today(year,day):
    assert 1601 <= year
    years = year - 1601
    offset = years + years // 4 - years // 100 + years // 400
    if (year %4 == 0) and (year % 100 == 0):
        day += 1
    elif(year %4 == 0) and (year % 100 == 0):
        day += 1
    weekday = (offset + day) % 7
    if today == 5 or today == 6:
        return "weekend" 
    return weekday


def first_day(year):
    assert 1601 <= year
    years = year - 1601
    offset = years + years // 4 - years // 100 + years // 400
    return offset % 7


def days_of_year(year):
    off = 0
    assert 1601 <= year
    years = year - 1601
    offset = years + years // 4 - years // 100 + years // 400
    leap = offset
    W_days = -2
    if (year %4 == 0) and (year % 100 == 0):
        W_days += 1
    elif (year % 4 == 0) and (year % 400 != 0):
        W_days += 1
    for i in range(364):
        W_days += 1
        leap += 1 
        if leap % 7 == 5 or leap % 7 == 6:
            W_days -= 1
    if first_day(year) != 5 or first_day(year) != 6:
        W_days -= 1
    if today (year, 120 ) != "weekend" :
        off += 1
        W_days -= 1
    if today (year, 127 ) != "weekend" :
        off += 1
        W_days -= 1
    if today (year, 185 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 186 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 271 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 301 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 321 ) != "weekend" :
        off += 1
        W_days -= 1
    if today (year, 358 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 359) != "weekend" :
        off += 1
        W_days -= 1
    if today (year, 360) != "weekend" :
        off += 1
        W_days -= 1


    

        

    
    

    
    return W_days
for i in range(2004,2009):

    t = days_of_year(i)
    print(t)
        


# def today(year,day):
#     assert 1601 <= year
#     years = year - 1601
#     offset = years + years // 4 - years // 100 + years // 400
#     weekday = (offset + day) % 7
#     # print(today)
#     if today == 5 or today == 6:
#         return "weekend" 
#     return weekday
"""
def W_days_count(year):
    w_days = 0
    if (year % 4 == 0) and (year % 100 == 0):
        w_days += 1
        print("leap")
    elif (year % 4 == 0) and (year % 100 != 0):
        w_days += 1
        print("leap")
    for i in range(364):
        s = today (year,i)
        if s == 0 or s == 1 or s == 2 or s == 3 or s == 4 :
            w_days += 1
    return w_days

# t = today(2026,25)
# print(t)
def off_days(year):
    off = 0
    W_days = W_days_count(year) -2
    print(W_days)
    if ((year % 4 == 0) and (year % 100 == 0)) or ((year % 4 == 0) and (year % 100 != 0)):
        if (today (year, -1) != "weekend"):
            off += 1
            W_days -= 1
    else:
        if (today (year, 0) != "weekend"):
            off += 1
            W_days -= 1
    if today (year, 120 ) != "weekend" :
        off += 1
        W_days -= 1
    if today (year, 127 ) != "weekend" :
        off += 1
        W_days -= 1
    if today (year, 185 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 186 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 271 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 301 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 321 ) != "weekend" :
        off += 1
        W_days -= 1
    if today (year, 358 ) != "weekend":
        off += 1
        W_days -= 1
    if today (year, 359) != "weekend" :
        off += 1
        W_days -= 1
    if today (year, 360) != "weekend" :
        off += 1
        W_days -= 1
    print(off,year , W_days)
    return W_days

"""
s = days_of_year(2020)
print(s, "should be 251")
s = days_of_year(2004)
print(s, "should be 253")
s = days_of_year(2000)
print(s, "should be 250")
s = days_of_year(1991)
print(s, "should be 251")
s = days_of_year(1996)
print(s, "should be 252")
    
"""

# def main():
#     assert off_days(2020) == 251
#     assert off_days(2021) == 252
#     assert off_days(2016) == 252
#     # assert off_days(2004) == 253
#     assert off_days(1993) == 252
#     # assert off_days(1991) == 251
#     assert off_days(1990) == 250
#     assert off_days(1900) == 250
#     # assert off_days(2000) == 250
#     # assert off_days(1996) == 252


# if __name__ == "__main__":
#     main()
"""