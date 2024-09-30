from ib111 import week_04  # noqa


# Napište čistou funkci, která na vstupu dostane dvě celá kladná
# čísla ‹rows› a ‹cols› a vrátí tabulku (dvourozměrný seznam)
# o ‹rows› řádcích a ‹cols› sloupcích. V buňce v řádku ‹y› a sloupci
# ‹x› bude počet společných dělitelů čísel ‹x› a ‹y›. Levý horní roh
# má souřadnice ‹x = y = 1›.

# Například pro vstup ‹rows = 4›, ‹cols = 2› dostaneme tabulku ‹[[1,
# 1], [1, 2], [1, 1], [1, 2]]›.

def common_divisors(rows, cols):
    pass


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
