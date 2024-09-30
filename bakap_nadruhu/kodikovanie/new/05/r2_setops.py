from ib111 import week_05  # noqa


# Vaším úkolem bude naprogramovat základní množinové operace (zatím
# máme k dispozici pouze operace, které pracují vždy s jedním
# prvkem). U každé operace si rozmyslete, kolik kroků provede
# vzhledem k velikostem obou vstupních množin.

# První a v nějakém smyslu nejjednodušší operací je sjednocení.
# Nejprve implementujte sjednocení jako čistou funkci, poté jako
# proceduru, která rozšíří stávající množinu o prvky nějaké další (a
# implementuje tedy sjednocení „in situ“). Srovnejte jejich
# složitost.

def set_union(a: set[int], b: set[int]) -> set[int]:
    pass


def set_update(to_extend: set[int], other: set[int]) -> None:
    pass


# Druhou standardní operací je průnik. Ten je o něco složitější
# a také je na místě zvážit rozdíl mezi čistou verzí, která sestrojí
# novou množinu, a procedurou, která zmenší množinu stávající. Dejte
# pozor na to, že tu stejnou množinu není dovoleno zároveň jak měnit
# tak procházet.

def set_intersect(a: set[int], b: set[int]) -> set[int]:
    pass


def set_keep(to_reduce: set[int], other: set[int]) -> None:
    pass


def main() -> None:
    x = {1}
    y = {2}

    assert set_union(x, y) == {1, 2}
    assert x == {1}
    assert y == {2}

    set_update(x, y)
    assert x == {1, 2}
    assert y == {2}

    assert set_intersect(x, y) == {2}
    assert x == {1, 2}
    assert y == {2}

    set_keep(x, y)
    assert x == {2}
    assert y == {2}

    for i in range(1000):
        x.add(i)

    set_update(x, y)
    assert len(x) == 1000

    set_update(y, x)
    assert x == y

    set_keep(x, y)
    assert x == y

    assert set_intersect(x, y) == x
    y.remove(33)
    assert set_intersect(x, y) == y
    assert set_union(x, y) == x


if __name__ == '__main__':
    main()
