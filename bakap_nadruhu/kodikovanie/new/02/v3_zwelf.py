from ib111 import week_02  # noqa


# Cvelfové používají k zápisu čísel dvanáctkovou soustavu, přičemž
# kromě nám známých číslic ⟦0, 1, 2, 3, 4, 5, 6, 7, 8, 9⟧ používají
# ještě číslice ⟦δ⟧ (s hodnotou deset) a ⟦ε⟧ (s hodnotou jedenáct).
#
# Cvelfí míchání je taková operace, kdy vezmeme kladné celé číslo
# v cvelfím zápisu a přeskládáme jeho číslice tak, aby všechny
# číslice ⟦δ⟧ stály vlevo a všechny číslice ⟦ε⟧ stály vpravo.
# Ostatní číslice zůstanou v původním pořadí. Výsledný zápis pak
# opět přečteme jako číslo v cvelfím zápisu.  Napište čistou funkci
# ‹zwelf_shuffle(num)›, která dostane na vstupu kladné celé číslo
# a vrátí výsledek po cvelfím míchání.

# Například:
#
# • číslo 3302 zapíše cvelf jako ⟦(1δε2)ᵦ⟧ a po cvelfím míchání z něj
#   vznikne ⟦(δ12ε)ᵦ = 17459⟧,
# • číslo 1587 zapíše cvelf jako ⟦(ε03)ᵦ⟧ a po míchání z něj vznikne
#   ⟦(03ε)ᵦ = 47⟧ (levostrannou nulu při čtení zápisu samozřejmě
#   ignorujeme),
# • číslo 1729 zapíše cvelf jako ⟦(1001)ᵦ⟧ a to se tedy mícháním nezmění.

def zwelf_shuffle(num):
    pass


def main() -> None:
    assert zwelf_shuffle(3302) == 17459
    assert zwelf_shuffle(1587) == 47
    assert zwelf_shuffle(1729) == 1729
    assert zwelf_shuffle(1451) == 1451


if __name__ == '__main__':
    main()
