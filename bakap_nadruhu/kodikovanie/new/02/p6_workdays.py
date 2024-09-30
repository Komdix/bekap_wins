from ib111 import week_02  # noqa


# Napište funkci, která zjistí, kolik bude pracovních dnů v roce
# ‹year›, přičemž parametr ‹day_of_week› udává, na který den v týdnu
# v tomto roce padne první leden. Dny v týdnu mají hodnoty 0–6
# počínaje pondělím s hodnotou 0.

# České státní svátky jsou:
#
# │  datum │ svátek                                         │
# ├┄┄┄┄┄┄┄▻┼◅┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
# │   1.1. │ Den obnovy samostatného českého státu          │
# │      — │ Velký pátek                                    │
# │      — │ Velikonoční pondělí                            │
# │   1.5. │ Svátek práce                                   │
# │   8.5. │ Den vítězství                                  │
# │   5.7. │ Den slovanských věrozvěstů Cyrila a Metoděje   │
# │   6.7. │ Den upálení mistra Jana Husa                   │
# │  28.9. │ Den české státnosti                            │
# │ 28.10. │ Den vzniku samostatného československého státu │
# │ 17.11. │ Den boje za svobodu a demokracii               │
# │ 24.12. │ Štědrý den                                     │
# │ 25.12. │ 1. svátek vánoční                              │
# │ 26.12. │ 2. svátek vánoční                              │

# Přestupné roky: v některých letech se na konec února přidává 29.
# den. Jsou to roky, které jsou dělitelné čtyřmi, s výjimkou těch,
# které jsou zároveň dělitelné 100 a nedělitelné 400.

# Čistou funkci ‹first_day› můžete použít k tomu, abyste zjistili,
# na který den v týdnu padne 1. leden daného roku. Např.
# ‹first_day(2001)› vrátí nulu, protože rok 2001 začínal pondělím.

def first_day(year):
    assert 1601 <= year
    years = year - 1601
    offset = years + years // 4 - years // 100 + years // 400
    return offset % 7


def workdays(year):
    pass


def main():
    assert workdays(2020) == 251
    assert workdays(2021) == 252
    assert workdays(2016) == 252
    assert workdays(2004) == 253
    assert workdays(1993) == 252
    assert workdays(1991) == 251
    assert workdays(1990) == 250
    assert workdays(1900) == 250
    assert workdays(2000) == 250
    assert workdays(1996) == 252


if __name__ == "__main__":
    main()
