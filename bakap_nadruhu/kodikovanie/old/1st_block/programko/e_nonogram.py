# from ib111 import week_10  # noqa

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
 LL›.
# Na pořadí seznamů uvnitř vnějšího seznamu nezáleží.
#
# «Nápověda:» Využijte backtracking. Zkuste začít implementací pro situace,
# kdy je ‹prefix› prázdný, a tuto implementaci pak rozšiřte.

# def gen_lines_with_prefix(clue: Clue, size: int,
#                           prefix: list[Pixel]) -> list[list[Pixel]]:
#     pass
def gen_lines_with_prefix(clue: Clue, size: int, prefix: list[Pixel]) -> list[list[Pixel]]:
    def backtrack(clue_idx, line_idx, current_line):
        if clue_idx == len(clue):  # All clues are placed
            if line_idx == size:  # The line is complete
                result.append(current_line)
            return

        # Calculate the minimum and maximum starting positions for the next block
        min_start = line_idx + (1 if line_idx > 0 else 0)  # Add space after previous block if not at start
        max_start = size - sum(clue[clue_idx:]) - (len(clue) - clue_idx - 1)

        for start in range(min_start, max_start + 1):
            new_line = current_line + [EMPTY] * (start - line_idx) + [FULL] * clue[clue_idx]
            backtrack(clue_idx + 1, start + clue[clue_idx], new_line)

    # Start backtracking
    result = []
    backtrack(0, len(prefix), prefix[:])
    return result
# Dále implementujte čistou funkci ‹solve›, která najde řešení malované
# křížovky se zadanou legendou. Pokud žádné řešení neexistuje, vrátí ‹None›.
# Pokud existuje více než jedno řešení, vrátí libovolné z nich.
#
# «Nápověda:» Využijte backtracking. Použijte funkci ‹gen_lines_with_prefix›.
# Začněte v levém horním rohu. Střídejte řádky a sloupce. V testech budeme
# používat jen takové vstupy, které se tímto přístupem dají dostatečně rychle
# vyřešit.

# def solve(rows: list[Clue], cols: list[Clue]) -> Picture | None:
#     pass


def solve(rows: list[Clue], cols: list[Clue]) -> Picture | None:
    height, width = len(rows), len(cols)
    picture = Picture(height, width)

    def is_valid(picture, row, col):
        def check_line(line, clue):
            idx, count, blocks = 0, 0, []
            for cell in line:
                if cell == FULL:
                    count += 1
                elif cell == EMPTY and count > 0:
                    blocks.append(count)
                    count = 0
            if count > 0:
                blocks.append(count)

            # If the line is incomplete (contains UNKNOWN), ensure that the
            # current blocks do not violate the clue
            if UNKNOWN in line:
                if len(blocks) > len(clue):
                    return False
                for i in range(min(len(blocks), len(clue))):
                    if blocks[i] > clue[i]:
                        return False
                return True

            return blocks == clue

        # Check if the row is valid
        if not check_line(picture.pixels[row], rows[row]):
            return False

        # Check if the column is valid
        col_line = [picture.pixels[r][col] for r in range(picture.height)]
        if not check_line(col_line, cols[col]):
            return False

        return True

    def backtrack(row, col):
        if row == height:
            return True

        next_row, next_col = (row, col + 1) if col < width - 1 else (row + 1, 0)
        for state in [FULL, EMPTY]:
            picture.pixels[row][col] = state
            if is_valid(picture, row, col) and backtrack(next_row, next_col):
                return True
            picture.pixels[row][col] = UNKNOWN

        return False

    if backtrack(0, 0):
        return picture
    else:
        return None

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
