from ib111 import week_05  # noqa


# «Connect Four¹» je hra pro dva hráče, v češtině někdy nazývaná Cestovní nebo
# Padající piškvorky. Každý hráč má žetony v jedné barvě; vyhrává ten, kdo jako
# první vytvoří nepřerušenou řadu «přesně čtyř» svých žetonů (horizontální,
# vertikální, diagonální). Hrací deska je přitom postavena vertikálně tak, že
# žetony padají směrem dolů, dokud nenarazí na jiný žeton nebo spodní rám
# desky. Hráč si tedy při svém tahu volí pouze sloupec, do nějž žeton hodí.
# (Na rozdíl od klasických piškvorek, kde si hráč volí přesné souřadnice
# a nic nikam nepadá.)
#
# ¹ ‹https://en.wikipedia.org/wiki/Connect_Four›
#
# Pro reprezentaci žetonů hráčů budeme v tomto úkolu používat znaky ‹X› a ‹O›.
# Hrací desku bude představovat seznam seznamů žetonů – vnitřní seznamy jsou
# postupně jednotlivé sloupce desky seřazené zdola nahoru. Tedy např. seznam
# ‹[['X'], [], ['O', 'X'], [], ['X', 'O', 'O'], [], []]›
# popisuje následující situaci:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │   │   │   │   │ O │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │   │ X │   │ O │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │ X │   │ O │   │ X │   │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#    0   1   2   3   4   5   6
#
# V naší reprezentaci přitom nemáme žádnou maximální výšku. Do sloupce
# s indexem 4 tedy je možno přidat další žeton a celá herní deska se tak
# nadstaví o další řádek.
#
# Pro hrací desku používáme typový alias ‹Grid›.

Grid = list[list[str]]


# Herní desku budeme chtít v průběhu hry (textově) vykreslovat. Samotná
# vykreslovací procedura je připravená v dodaném souboru (viz níže), ale abyste
# jí usnadnili práci, implementuje nejprve čistou funkci ‹to_matrix›, která
# zadanou herní desku ‹grid› zkonvertuje do podoby 2D matice (reprezentované
# seznamem seznamů jako na přednášce). Matice bude mít přesně tolik řádků,
# kolik je potřeba. (Matice s nula řádky je prázdný seznam.)
# Prvky matice budou jednoznakové řetězce ‹" "› (prázdné místo), ‹"X"›, ‹"O"›.
#
# Pro desku z výše uvedené situaci tedy funkce ‹to_matrix› vrátí tento seznam:
# ‹[[" ", " ", " ", " ", "O", " ", " "],
#   [" ", " ", "X", " ", "O", " ", " "],
#   ["X", " ", "O", " ", "X", " ", " "]]›


def to_matrix(grid: Grid) -> list[list[str]]:
    lst_lngth: list[int] = []
    for elem in grid:
        lngth = len(elem)
        lst_lngth.append(lngth)
    rows = max(lst_lngth)

    columns = []
    lst: list[str] = []
    lst_maxtrix = []

    for column in grid:
        lst = []
        for player in column:
            lst.append(player)
        while len(lst) < rows:
            lst.append(" ")
        columns.append(lst)

    for i in range(rows-1, -1, -1):
        lst_add = []
        for item in columns:
            lst_add.append(item[i])
        lst_maxtrix.append(lst_add)

    return lst_maxtrix


# Dále pak implementujte proceduru ‹play›, která provede do zadané herní desky
# ‹grid› vhození žetonu hráče ‹player› do sloupce ‹column›. Předpokládejte
# přitom, že herní deska je ve stavu, kdy ještě nikdo nevyhrál, ‹player› je
# buďto ‹'X'› nebo ‹'O'› a ‹column› je validní index sloupce. Procedura vrátí
# ‹True›, pokud tímto tahem hráč vyhrál; ‹False› jinak.
#
# Pro jistotu připomínáme, že za výhru považujeme pouze situaci, kdy má některý
# z hráčů nepřerušenou řadu «přesně čtyř» svých žetonů. Pokud tedy vhozením
# žetonu vznikne nepřerušená řada více než čtyř žetonů, o výhru se nejedná.

Board = list[list[str]]


def control_in_row(start: tuple[int, int], bounds: tuple[int, int],
                   in_row: int, board: Board, player: str,
                   direction: tuple[int, int]) -> int:

    max_rows, max_col = bounds
    dir_x, dir_y = direction
    x, y = start

    in_row = 0
    while in_row < 6:
        y += dir_y
        x += dir_x
        if y > max_rows or y < 0 or x < 0 or x > max_col:
            break

        controled_row = board[y]
        if controled_row[x] == player:
            in_row += 1
        else:
            break

    return in_row


def play(grid: Grid, player: str, column: int) -> bool:
    col = grid[column]
    col.append(player)
    lst = []
    for elem in grid:
        lngth = len(elem)
        lst.append(lngth)
    max_rows = max(lst)

    board = to_matrix(grid)

    start_row = len(col)
    start_y = max_rows - start_row
    start_x = column
    start = (start_x, start_y)

    max_row = max_rows - 1
    max_col = len(grid) - 1
    bounds = (max_row, max_col)

    directions = {(1, 0): "East", (-1, 0): "West",
                  (0, 1): "North", (0, -1): "South",
                  (1, -1): "SE", (-1, 1): "NW",
                  (1, 1): "NE", (-1, -1): "SW"
                  }

    in_row = 0

    while in_row < 6:
        pair = 0
        in_row = 1   # I automatically include the added player move as one
        for direction in directions.keys():
            if pair == 2:
                # I need to control 2 directions from the point of added move
                # before i reset the number of pieces in row
                if in_row == 4:
                    return True
                in_row = 1
                pair = 0
            pair += 1
            in_row += control_in_row(start, bounds, in_row,
                                     board, player, direction)
        return in_row == 4
    return False


# Pro (textovou) vizualizaci je vám k dispozici soubor ‹game_connect_four.py›,
# který vložte do stejného adresáře, jako je soubor s vaším řešením a spusťte.
# Počet sloupců herní desky nastavíte jako globální konstantu ‹SIZE›.

def main() -> None:
    grid: Grid = [['X'], [], ['O', 'X'], [], ['X', 'O', 'O'], [], []]
    assert to_matrix(grid) == [
        [" ", " ", " ", " ", "O", " ", " "],
        [" ", " ", "X", " ", "O", " ", " "],
        ["X", " ", "O", " ", "X", " ", " "],
    ]

    assert not play(grid, 'X', 3)
    assert grid == [['X'], [], ['O', 'X'], ['X'], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'O', 3)
    assert grid == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'X', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], ['X'], []]

    assert not play(grid, 'O', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], ['X', 'O'], []]

    assert not play(grid, 'X', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'],
            ['X', 'O', 'O'], ['X', 'O', 'X'], []]

    assert play(grid, 'O', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'],
            ['X', 'O', 'O'], ['X', 'O', 'X', 'O'], []]


if __name__ == '__main__':
    main()
