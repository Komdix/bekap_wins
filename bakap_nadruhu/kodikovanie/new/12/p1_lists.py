from ib111 import week_12  # noqa

# Napište čistou funkci ‹filter_out_odd›, která jako parametr
# dostane seznam seznamů čísel a vrátí nový seznam seznamů čísel,
# který vytvoří takto:
#
#  • z vnitřních seznamů odstraní lichá čísla, a
#  • z vnějšího seznamu odstraní (případně i nově vzniklé) prázdné
#    seznamy.
#
# Ostatní prvky v seznamech zůstanou v původním pořadí. Pro vstup
# ‹[[1, 5], [1, 2, 3], [], [4, 5, 6]]› tedy funkce vrátí ‹[[2], [4,
# 6]]›.


def filter_out_odd(list_of_lists: list[list[int]]) -> list[list[int]]:
    pass


# Dále napište čistou funkci ‹without_middle_occurrence›, která
# dostane jako parametr seznam čísel ‹values› a hledané číslo
# ‹value› a vrátí seznam bez prostředního výskytu hledaného čísla.
# Vyskytuje-li se hledané číslo v zadaném seznamu sudý počet krát,
# bereme jako prostřední ten blíže začátku, tedy např. pro vstup
# ‹([2, 2, 3, 2, 2], 2)› funkce vrátí ‹[2, 3, 2, 2]›. (Pokud seznam
# hledané číslo neobsahuje, vraťte původní seznam nebo jeho kopii.)


def without_middle_occurrence(values: list[int], value: int) -> list[int]:
    pass


def main() -> None:
    assert filter_out_odd([[1, 5], [1, 2, 3], [], [4, 5, 6]]) == [[2], [4, 6]]

    lists = [[42, 17], [6, 7, 8, 9], [11, 12, 13, 14, 15]]
    assert filter_out_odd(lists) == [[42], [6, 8], [12, 14]]
    assert lists == [[42, 17], [6, 7, 8, 9], [11, 12, 13, 14, 15]]

    assert filter_out_odd([]) == []
    assert filter_out_odd([[]]) == []

    assert without_middle_occurrence([2, 2, 3, 2, 2], 2) == [2, 3, 2, 2]
    assert without_middle_occurrence([1, 5, 7, 3, 5, 12, 5, 0, 9], 5) \
        == [1, 5, 7, 3, 12, 5, 0, 9]
    assert without_middle_occurrence([1, 2, 3, 4], 5) == [1, 2, 3, 4]

    values = [0, 0, 0, 0, 7, 0, 0, 0, 0, 7, 8]
    assert without_middle_occurrence(values, 0) \
        == [0, 0, 0, 7, 0, 0, 0, 0, 7, 8]
    assert values == [0, 0, 0, 0, 7, 0, 0, 0, 0, 7, 8]


if __name__ == "__main__":
    main()
