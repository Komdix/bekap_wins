from ib111 import week_03  # noqa
from math import isclose


# Napište čistou funkci, která dostane na vstup seznam bodů v rovině
# (tj. seznam dvojic čísel) a vrátí délku lomené čáry, která těmito
# body prochází (tzn. takové, která vznikne spojením každých dvou
# sousedních bodů seznamu úsečkou). Souřadnice i délky
# reprezentujeme čísly s plovoucí desetinnou čárkou (typ ‹float›).

# Například seznam ‹[(0, 0), (1, 0), (1, 1), (2, 1)]› definuje tuto
# lomenou čáru:
#
#       (1, 1) ┌───▶(2, 1)
#              │
#    (0, 0)╶───┘(1, 0)
#
# složenou ze tří segmentů (úseček) velikosti 1. Její délka je 3.


def point_distance(a, b):
    lst = [a, b]
    c = lst[0]
    d = lst[1]
    c_x, c_y = c
    d_x, d_y = d
    x = [c_x, d_x]
    y = [c_y, d_y]
    if c_x == d_x or c_y == d_y:
        result = max(x) - min(x) + max(y) - min(y)
        return result
    first = max(c) - min(c)
    second = max(d) - min(d)
    result = (first ** 2 + second ** 2)**0.5
    return result


def length(points):
    if points == []:
        return 0.0
    lst = points
    result = 0
    for element in range(len(lst)-1):
        a = lst[element]
        b = lst[element + 1]
        a_x, a_y = a
        b_x, b_y = b
        x = [a_x, b_x]
        y = [a_y, b_y]
        if a_x == b_x or a_y == b_y:
            result += (max(x) - min(x)) + (max(y) - min(y))
        else:
            first = max(x) - min(x)
            second = max(y) - min(y)
            result += (first ** 2 + second ** 2)**0.5
    return result


def main():
    assert isclose(point_distance((0.0, 0.0), (1.0, 0.0)), 1.0)
    assert isclose(point_distance((3.0, 0.0), (0.0, 4.0)), 5.0)
    assert isclose(length([(0.0, 1.0), (1.0, 1.0), (1.0, 2.0)]), 2.0)
    assert isclose(length([(0.0, 0.0)]), 0.0)
    assert isclose(length([]), 0.0)
    assert isclose(length([(3.0, 5.0), (3.0, 15.0), (4.0, 15.0),
                           (4.0, 0.0), (0.0, 0.0)]), 30.0)
    assert isclose(length([(0.0, 0.0), (3.0, 4.0)]), 5.0)
    assert isclose(length([(0.0, 0.0), (3.0, 4.0), (3.0, 7.0)]), 8.0)


if __name__ == "__main__":
    main()
