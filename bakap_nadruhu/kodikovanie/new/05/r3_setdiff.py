from ib111 import week_05  # noqa


# Uvažme nyní operaci rozdílu – opět v čisté i procedurální verzi.
# Opět srovnejte efektivitu obou implementací vzhledem k velikosti
# obou parametrů.

def set_difference(a: set[int], b: set[int]) -> set[int]:
    pass


def set_remove(to_reduce: set[int], other: set[int]) -> None:
    pass


# Množinový rozdíl má jednu zajímavou variaci – tzv. symetrický
# rozdíl, kdy konstruujeme množinu, která obsahuje prvky, které
# náleží do právě jedné vstupní množiny. Opět implementujte obě
# verze. Symetrický rozdíl je možné složit z ostatních množinových
# operacích mnoha způsoby – rozmyslete si, které fungují lépe a
# které hůře.

def set_symmetric_diff(a: set[int], b: set[int]) -> set[int]:
    pass


def set_symmetric_inplace(to_change: set[int],
                          other: set[int]) -> None:
    pass


def main() -> None:
    x = {1}
    y = {2}

    assert set_difference(x, y) == x
    assert set_difference(y, x) == y
    assert x == {1}
    assert y == {2}

    set_remove(x, y)
    assert x == {1}
    assert y == {2}

    x.add(2)

    assert set_difference(x, y) == {1}
    assert set_difference(y, x) == set()

    set_remove(x, y)
    assert x == {1}
    assert y == {2}

    assert set_symmetric_diff(x, y) == {1, 2}
    x.add(2)
    assert set_symmetric_diff(x, y) == {1}
    y.add(3)
    assert set_symmetric_diff(x, y) == {1, 3}
    y.add(4)
    assert set_symmetric_diff(x, y) == {1, 3, 4}

    set_symmetric_inplace(x, y)
    assert x == {1, 3, 4}
    assert y == {2, 3, 4}

    set_symmetric_inplace(x, y)
    assert x == {1, 2}
    assert y == {2, 3, 4}


if __name__ == '__main__':
    main()
