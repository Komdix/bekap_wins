from ib111 import week_04  # noqa


# Napište čistou funkci, která na vstupu dostane dvě celá kladná
# čísla ‹rows› a ‹cols› a vrátí tabulku (dvourozměrný seznam)
# o ‹rows› řádcích a ‹cols› sloupcích. V buňce v řádku ‹y› a sloupci
# ‹x› bude počet společných dělitelů čísel ‹x› a ‹y›. Levý horní roh
# má souřadnice ‹x = y = 1›.

# Například pro vstup ‹rows = 4›, ‹cols = 2› dostaneme tabulku
# ‹[[1,1], [1, 2], [1, 1], [1, 2]]›.


def common_divisors(rows: int, cols: int) -> list[list[int]]:
    lst = []

    for row in range(1, rows+1):
        lst_row = [1]

        for divisor_row in range(2, row + 1):
            if row % divisor_row == 0:
                div_row = divisor_row
                lst_row.append(div_row)

        lst_col: list[int] = []
        control = 0

        for col in range(1, cols + 1):
            count = 0

            if control == cols+1:
                lst_col = []
                control = 0

            for divisor_col in range(1, col + 1):
                if col % divisor_col == 0:
                    for element in lst_row:
                        if element == divisor_col:

                            count += 1
                control += 1
            lst_col.append(count)
        lst.append(lst_col)

    return lst


def main() -> None:
    assert common_divisors(4, 2) == [[1, 1], [1, 2], [1, 1], [1, 2]]
    assert common_divisors(1, 1) == [[1]]
    assert common_divisors(1, 8) == [[1, 1, 1, 1, 1, 1, 1, 1]]
    assert common_divisors(5, 1) == [[1], [1], [1], [1], [1]]
    assert common_divisors(6, 6) == [[1, 1, 1, 1, 1, 1],
                                     [1, 2, 1, 2, 1, 2],
                                     [1, 1, 2, 1, 1, 2],
                                     [1, 2, 1, 3, 1, 2],
                                     [1, 1, 1, 1, 2, 1],
                                     [1, 2, 2, 2, 1, 4]]
    assert common_divisors(2, 4) == [[1, 1, 1, 1],
                                     [1, 2, 1, 2]]


if __name__ == '__main__':
    main()
