from ib111 import week_10  # noqa


# «Slovní aritmetika¹» (někdy též cryptarithm nebo algebrogram) je matematický
# hlavolam zadaný jako rovnice se slovy, např. „SEND + MORE = MONEY“.
# Cílem je přiřadit každému písmenu unikátní² číslici tak, aby po jejich
# nahrazení rovnost platila. Přitom zápis žádného z čísel nesmí začínat nulou.
# V tomto konkrétním případě (a v desítkové soustavě) je jediné možné
# řešení, a to S → 9, E → 5, N → 6, D → 7, M → 1, O → 0, R → 8, Y → 2.
# Po tomto nahrazení číslicemi skutečně platí ⟦9567 + 1085 = 10652⟧.
#
# ¹ ‹https://en.wikipedia.org/wiki/Verbal_arithmetic›
# ² „Unikátní“ znamená, že dvě různá písmena nemohou mít přiřazenu stejnou
#   číslici.
#
# Cílem této úlohy je napsat čistou funkci, která podobné hlavolamy řeší,
# a to v zadané poziční soustavě (základem bude vždy celé číslo mezi 2 a 26
# včetně). Rovnice na vstupu je zadána dvěma parametry. Levá strana rovnice
# ‹lhs› je seznam (alespoň dvou) slov, přičemž každé slovo je dáno jako seznam
# písmen (jednoznakových řetězců). Pravá strana rovnice je pak je vždy právě
# jedno slovo (seznam písmen).
#
# Funkce vrátí slovník, který každému písmenu hlavolamu přiřazuje unikátní
# hodnotu číslice. Pokud existuje více řešení, funkce vrátí libovolné
# z nich. Pokud neexistuje žádné řešení, funkce vrátí ‹None›.
#
# Nápověda: Použijte techniku backtrackingu. Vzpomeňte si na svá
# základoškolská léta – zejména na sčítání pod sebou, které začíná vždy
# zprava. I zde se k řešení hodí postupně zkoušet přiřazovat hodnoty
# číslicím, které jsou u jednotlivých sčítanců co nejvíce vpravo, a rekurzi
# včas ukončit, když už je jasné, že výsledku není možno dosáhnout.

def solve(lhs: list[list[str]], rhs: list[str], base: int) \
        -> dict[str, int] | None:
    pass


def main() -> None:
    # SEND + MORE = MONEY
    assert solve([['S', 'E', 'N', 'D'],
                  ['M', 'O', 'R', 'E']],
                 ['M', 'O', 'N', 'E', 'Y'], 10) \
        == {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}

    for base in range(2, 27):
        # XY + XY = YX
        result = solve([['X', 'Y'], ['X', 'Y']], ['Y', 'X'], base)
        if base == 2 or base % 3 != 2:
            assert result is None
        else:
            x = base // 3
            y = 2 * x + 1
            assert result == {'X': x, 'Y': y}


if __name__ == '__main__':
    main()
