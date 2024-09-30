from ib111 import week_10  # noqa

# «Numberlink¹» je logický hlavolam, v němž je zadána čtvercová síť s několika
# dvojicemi čísel a cílem je spojit všechny dvojice stejných čísel lomenou
# čarou, přičemž každým políčkem čtvercové sítě musí procházet právě jedna
# čára. V naší implementaci místo kreslení čar do čtvercové sítě vepíšeme
# čísla všude tam, kudy by spojnice zadaných čísel prošla.
#
# ¹ ‹https://en.wikipedia.org/wiki/Numberlink›
#
# Příklad vstupu:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │   │   │   │ 4 │   │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │ 3 │   │   │ 2 │ 5 │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │   │   │ 3 │ 1 │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │   │   │ 5 │   │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │   │   │   │   │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │   │ 1 │   │   │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │ 2 │   │   │   │ 4 │   │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#
# a řešení:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐ ┌───┬───┬───┬───┬───┬───┬───┐
#  │ 2 │ 2 │ 2 │ 4 │ 4 │ 4 │ 4 │ │▒▒▒│▒▒▒│▒▒▒│ 4 │ ◦ │ ◦ │ ◦ │
#  ├───┼───┼───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┼───┼───┤
#  │ 2 │ 3 │ 2 │ 2 │ 2 │ 5 │ 4 │ │▒▒▒│ 3 │▒▒▒│▒▒▒│▒2▒│░5░│ ◦ │
#  ├───┼───┼───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┼───┼───┤
#  │ 2 │ 3 │ 3 │ 3 │ 1 │ 5 │ 4 │ │▒▒▒│ ◦ │ ◦ │ 3 │ 1 │░░░│ ◦ │
#  ├───┼───┼───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┼───┼───┤
#  │ 2 │ 5 │ 5 │ 5 │ 1 │ 5 │ 4 │ │▒▒▒│░░░│░░░│░5░│ ◦ │░░░│ ◦ │
#  ├───┼───┼───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┼───┼───┤
#  │ 2 │ 5 │ 1 │ 1 │ 1 │ 5 │ 4 │ │▒▒▒│░░░│ ◦ │ ◦ │ ◦ │░░░│ ◦ │
#  ├───┼───┼───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┼───┼───┤
#  │ 2 │ 5 │ 1 │ 5 │ 5 │ 5 │ 4 │ │▒▒▒│░░░│ 1 │░░░│░░░│░░░│ ◦ │
#  ├───┼───┼───┼───┼───┼───┼───┤ ├───┼───┼───┼───┼───┼───┼───┤
#  │ 2 │ 5 │ 5 │ 5 │ 4 │ 4 │ 4 │ │▒2▒│░░░│░░░│░░░│ 4 │ ◦ │ ◦ │
#  └───┴───┴───┴───┴───┴───┴───┘ └───┴───┴───┴───┴───┴───┴───┘
#
# (Srovnejte s obrázkem na Wikipedii.)
#
# Máme připravené typové aliasy ‹Grid› pro 2D seznamy, ‹Position› pro dvojice
# souřadnic (sloupec, řádek; číslujeme jako obvykle od nuly zleva a shora)
# a ‹Ends›, jehož význam je vysvětlen níže.

Grid = list[list[int]]
Position = tuple[int, int]
Ends = dict[tuple[int, bool], Position]


# Nejprve implementujte čistou funkci ‹get_ends›, která dostane na vstup zadání
# hlavolamu jako 2D seznam, který obsahuje pouze nezáporná celá čísla, přičemž
# nuly reprezentují prázdná políčka a ostatní čísla ve vstupu jsou vždy přesně
# dvakrát. Funkce vrátí slovník typu ‹Ends›, v němž jsou pro každé kladné číslo
# ‹n› ze vstupu dvě položky:
# ‹(n, True): (x_1, y_1)› a ‹(n, False): (x_2, y_2)›,
# kde ‹(x_1, y_1)› a ‹(x_2, y_2)› jsou souřadnice výskytu daného čísla.
# Na tom, které souřadnice jsou u položky s ‹True› a s ‹False›, nezáleží.
# ‹True›, ‹False› zde používáme jenom proto, abychom mohli mít dvě různé
# položky pro každé číslo.
# (Proč volíme zrovna takovou reprezentaci, je vysvětleno níže.)

def get_ends(grid: Grid) -> Ends:
    pass


# Dále implementujte čistou funkci ‹solve›, která najde řešení pro zadaný
# vstup. Pokud žádné řešení neexistuje, vrátí ‹None›. Pokud existuje více než
# jedno řešení, vrátí libovolné z nich.
#
# «Nápověda:» Využijte backtracking. Spočítejte si nejdříve pozice čísel pomocí
# funkce ‹get_ends›. Na tyto pozice se můžete dívat jako na dva konce provázku,
# které se snažíte dostat k sobě a spojit. V každém kroku backtrackingu si
# zvolte jeden z „konců“ a pokuste se jej posunout – možné směry posunutí jsou
# právě ty lokální volby, které při backtrackingu provedete. Přitom je vhodné
# volit z možných konců takový, který má co nejméně těchto možných směrů.
# Kromě posouvání konců si zároveň chcete zaznamenat, která políčka už jsou
# obsazena.

def solve(grid: Grid) -> Grid | None:
    pass


# «Poznámka» k volbě typu ‹Ends› pro reprezentaci „konců provázků“:
# Mnozí by jistě mohli navrhnout, že mít ve dvojicích klíčů arbitrární
# hodnoty ‹True› a ‹False› je zbytečné a že by se slovník „konců“ dal
# napsat jinak (např. s typem ‹dict[int, tuple[Position, Position]›).
# Zde zvolený typ má ale jistou symetrii, která je výhodná pro implementaci
# funkce ‹solve›. Ke všem „koncům“ se totiž chováme stejně, a tedy kód
# pro nalezení jednoho konkrétního (toho s nejméně možnostmi pohybu)
# stejně jako kód pro jeho posunutí můžeme napsat obecně a nemusíme u toho
# rozebírat více různých případů.


def main() -> None:
    grid = [
        [0, 0, 0, 4, 0, 0, 0],
        [0, 3, 0, 0, 2, 5, 0],
        [0, 0, 0, 3, 1, 0, 0],
        [0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [2, 0, 0, 0, 4, 0, 0],
    ]

    check_ends(grid, get_ends(grid))

    assert solve(grid) == [
        [2, 2, 2, 4, 4, 4, 4],
        [2, 3, 2, 2, 2, 5, 4],
        [2, 3, 3, 3, 1, 5, 4],
        [2, 5, 5, 5, 1, 5, 4],
        [2, 5, 1, 1, 1, 5, 4],
        [2, 5, 1, 5, 5, 5, 4],
        [2, 5, 5, 5, 4, 4, 4],
    ]

    grid = [
        [1, 0, 0, 2],
        [2, 0, 0, 3],
        [3, 0, 0, 1],
    ]

    check_ends(grid, get_ends(grid))

    assert solve(grid) is None

    grid = [
        [1, 2, 3],
        [0, 0, 0],
        [0, 0, 0],
        [1, 2, 0],
        [0, 0, 0],
        [0, 0, 3],
    ]

    check_ends(grid, get_ends(grid))

    assert solve(grid) == [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [3, 3, 3],
        [3, 3, 3],
    ]

    grid = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    check_ends(grid, get_ends(grid))

    assert solve(grid) == [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    ]


def check_ends(grid: Grid, ends: Ends) -> None:
    nums = set()
    for row in grid:
        nums.update(row)

    nums.remove(0)

    for num in nums:
        for b in [True, False]:
            assert (num, b) in ends
            x, y = ends[num, b]
            assert grid[y][x] == num

        assert ends[num, True] != ends[num, False]


if __name__ == '__main__':
    main()
