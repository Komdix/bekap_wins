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


def lnght(grid_huh):
    lngth_max = 0
    for element in grid_huh:
        lnght = len(element)
        if lnght > lngth_max:
            lngth_max = lnght
    return lngth_max


def to_matrix(grid: Grid) -> list[list[str]]:
    rows = lnght(grid) 
    colums = []
    lst = []
    for element in grid:
        lst = []
        for player in element:
            lst.append(player)
        while len(lst) < rows:
            lst.append(" ")
        colums.append(lst)
    lst_maxtrix = []
    for i in range(rows-1, -1, -1):
        lst_add = []
        for item in colums:
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

def diagonals(start_x: int, start_y: int, max_rows: int, max_col, in_row: int, board: Board, player: int, dir_y: int, dir_x: int):
    in_row = 0
    y = start_y
    x = start_x
    while in_row < 4:
        y += dir_y
        x += dir_x
        if y > max_rows or y < 0 or x < 0 or x > max_col:
            break
        col_up = board[y]
        if col_up[x] == player:
            in_row += 1
        else:
            break
        
    return in_row


def play(grid: Grid, player: str, column: int) -> bool:
    col = grid[column]
    col.append(player)

    start_column = len(col)
    board = to_matrix(grid)
    start_y = len(board) - start_column
    start_x = column

    max_rows = lnght(grid) - 1
    max_col = len(board[0]) - 1
    
    directions_LR = [(1,-1), (-1,1)]
    directions_RL = [(1,1), (-1,-1)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    in_row = 1

    while in_row < 4:
        for element in directions_LR:
            y = start_y
            x = start_x
            dir_x, dir_y = element
            in_row += diagonals(x, y, max_rows, max_col, in_row, board, player, dir_y, dir_x)
            if in_row > 3:
                return True
            
        in_row = 1
        for element in directions_RL:
            y = start_y
            x = start_x
            dir_x, dir_y = element
            in_row += diagonals(start_x, start_y, max_rows, max_col, in_row, board, player, dir_y, dir_x)
            if in_row > 3:
                return True
            
        couple = 1
        in_row = 1
        for element in directions:
            if couple == 3:
                in_row = 1
                couple = 0
            couple += 1

            dir_x, dir_y = element
            y = start_y
            x = start_x -1
            while in_row < 4:
                y += dir_y
                x += dir_x
                if y > max_rows or y < 0 or x < 0 or x > max_col:
                    break
                row = board[y]
                horizontal = row[x]
                if horizontal == player:
                    in_row += 1
                else:
                    break
            if in_row > 3:
                return True

        break
    if in_row > 3:
                return True  
    
    return False
grid = [['X'], ['O', 'X', 'O'], ['O', 'X']]
s = play(grid, 'X', 0)
print(s, "should be false")
grid = [['X', 'O', 'O'], ['O', 'X'], ['X', 'O'], ['O', 'O', 'O', 'X'], [], []]
print(play(grid, 'X', 2), 'should true')
grid = [['X'], ['X'], ['X'], []]
print(play(grid, 'X', 3),'should true')
grid = [['O', 'O', 'O'], ['X'], ['X'], ['X'], []]
s =  play(grid, 'X', 4)
print(s,'should true')
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
