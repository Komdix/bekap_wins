from ib111 import week_10  # noqa

# «Malované křížovky¹» (nonogramy) jsou logické hlavolamy, u kterých je cílem
# vybarvit některá políčka čtvercové sítě podle zadané číselné legendy.
# Výsledkem je typicky jednoduchý obrázek. Existují různé druhy malovaných
# křížovek, v této úloze nás budou zajímat pouze ty základní černobílé.
#
# ¹ ‹https://en.wikipedia.org/wiki/Nonogram›
#
# Zadání malované křížovky vypadá např. takto:
#  ┌──────────────────────────────┐
#  │               1              │
#  │               2     1  1     │
#  │         1  2  1  4  2  1  3  │
#  │       ┌──┬──┬──┬──┬──┬──┬──┐ │
#  │     1 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │ 1 1 1 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │     7 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │   2 1 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │     3 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │   1 1 │  │  │  │  │  │  │  │ │
#  │       └──┴──┴──┴──┴──┴──┴──┘ │
#  └──────────────────────────────●
#
# Číselná legenda u řádků a sloupců ukazuje, kolik políček máme v dané řadě
# (řádku nebo sloupci) vybarvit a jak mají být vybarvená políčka seskupena.
# Pokud bychom tedy například měli legendu «1 3 2» a řádek délky 9 políček,
# pak jej můžeme vyplnit jedním z těchto způsobů:
#
#  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
#  │▓▓│  │▓▓│▓▓│▓▓│  │▓▓│▓▓│  │
#  └──┴──┴──┴──┴──┴──┴──┴──┴──┘
#  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
#  │▓▓│  │▓▓│▓▓│▓▓│  │  │▓▓│▓▓│
#  └──┴──┴──┴──┴──┴──┴──┴──┴──┘
#  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
#  │▓▓│  │  │▓▓│▓▓│▓▓│  │▓▓│▓▓│
#  └──┴──┴──┴──┴──┴──┴──┴──┴──┘
#
# Řešením malované křížovky je vybarvení políček takové, že každý řádek
# a každý sloupec odpovídá zadané legendě. Výše uvedený příklad má tedy
# následující (jediné) řešení:
#  ┌──────────────────────────────┐
#  │               1              │
#  │               2     1  1     │
#  │         1  2  1  4  2  1  3  │
#  │       ┌──┬──┬──┬──┬──┬──┬──┐ │
#  │     1 │  │  │▓▓│  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │ 1 1 1 │  │▓▓│  │▓▓│  │  │▓▓│ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │     7 │▓▓│▓▓│▓▓│▓▓│▓▓│▓▓│▓▓│ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │   2 1 │  │  │▓▓│▓▓│  │  │▓▓│ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │     3 │  │  │  │▓▓│▓▓│▓▓│  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │   1 1 │  │  │▓▓│  │▓▓│  │  │ │
#  │       └──┴──┴──┴──┴──┴──┴──┘ │
#  └──────────────────────────────●
#
# V této úloze si zkusíte napsat program, který bude schopen některé jednodušší
# malované křížovky řešit pomocí techniky backtrackingu. Jednotlivá políčka
# křížovky budeme reprezentovat typem ‹Pixel›, což je zde typový alias pro
# ‹int› použitý pouze pro lepší čitelnost anotací.

Pixel = int
EMPTY, FULL, UNKNOWN = 0, 1, 2

# Máme zde připravené globální konstanty ‹EMPTY› (reprezentuje prázdné
# políčko), ‹FULL› (reprezentuje vybarvené políčko), ‹UNKNOWN› (reprezentuje
# neznámý stav políčka). Počet různých druhů políček si můžete pro účely
# implementace případně rozšířit, ale tyto tři konstanty zachovejte.
#
# Dále máme připraven typový alias pro číselnou legendu. Legenda pro řádky bude
# v seznamu uložená zleva doprava, legenda pro sloupce shora dolů.

Clue = list[int]


# Nakonec je připravena třída ‹Picture›, která bude reprezentovat výsledný
# obrázek. Tuto třídu můžete libovolně upravovat (přidávat vlastní atributy
# a metody), ale zachovejte parametry metody ‹__init__› i způsob inicializace
# atributů ‹height›, ‹width› a ‹pixels›.

class Picture:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.pixels = [[UNKNOWN for _ in range(width)]
                       for _ in range(height)]


# Nejprve implementujte čistou funkci ‹gen_lines_with_prefix›, která vrátí
# seznam všech řad délky ‹size›, které odpovídají zadané legendě (‹clue›)
# a zároveň začínají zadaným prefixem (‹prefix›). Předpokládejte, že ‹prefix›
# má délku nejvýše ‹size› a obsahuje pouze hodnoty ‹EMPTY› a ‹FULL›.
# Na pořadí seznamů uvnitř vnějšího seznamu nezáleží.
#
# «Nápověda:» Využijte backtracking. Zkuste začít implementací pro situace,
# kdy je ‹prefix› prázdný, a tuto implementaci pak rozšiřte.

def gen_lines_with_prefix(clue: Clue, size: int,
                          prefix: list[Pixel]) -> list[list[Pixel]]:
    pass


# Dále implementujte čistou funkci ‹solve›, která najde řešení malované
# křížovky se zadanou legendou. Pokud žádné řešení neexistuje, vrátí ‹None›.
# Pokud existuje více než jedno řešení, vrátí libovolné z nich.
#
# «Nápověda:» Využijte backtracking. Použijte funkci ‹gen_lines_with_prefix›.
# Začněte v levém horním rohu. Střídejte řádky a sloupce. V testech budeme
# používat jen takové vstupy, které se tímto přístupem dají dostatečně rychle
# vyřešit.

def solve(rows: list[Clue], cols: list[Clue]) -> Picture | None:
    pass


def main() -> None:
    # --- empty prefix ---

    assert sorted(gen_lines_with_prefix([1, 3, 2], 9, [])) == [
        [0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0],
    ]

    assert sorted(gen_lines_with_prefix([1], 4, [])) == [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0],
    ]

    assert gen_lines_with_prefix([], 10, []) \
        == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert gen_lines_with_prefix([1, 1, 1, 1], 6, []) == []

    assert gen_lines_with_prefix([1, 1, 1, 1], 7, []) \
        == [[1, 0, 1, 0, 1, 0, 1]]

    assert gen_lines_with_prefix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 64, []) \
        == [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
             1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    assert len(gen_lines_with_prefix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 67,
                                     [])) == 286

    # --- non-empty prefix ---

    assert sorted(gen_lines_with_prefix([1, 3, 2], 9, [1, 0, 1])) == [
        [1, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0],
    ]

    assert sorted(gen_lines_with_prefix([1], 4, [0])) == [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]

    assert gen_lines_with_prefix([], 10, [0, 0, 0]) \
        == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert gen_lines_with_prefix([1, 1, 1, 1], 7, [0]) == []

    assert gen_lines_with_prefix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 1000, [1, 1]) == []

    assert len(gen_lines_with_prefix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                     100,
                                     [0 for _ in range(32)])) == 1001

    # --- solve ---

    pic = solve([[1], [1, 1, 1], [7], [2, 1], [3], [1, 1]],
                [[1], [2], [1, 2, 1], [4], [1, 2], [1, 1], [3]])

    assert pic is not None
    assert pic.width == 7
    assert pic.height == 6
    assert pic.pixels == [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
    ]

    assert solve([[2], [], [2]], [[1, 1], [2]]) is None

    pic = solve([[2], [], [2]], [[1, 1], [1, 1]])
    assert pic is not None
    assert pic.width == 2
    assert pic.height == 3
    assert pic.pixels == [[1, 1], [0, 0], [1, 1]]


if __name__ == '__main__':
    main()
