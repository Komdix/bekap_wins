from ib111 import week_06  # noqa


# † Napište (čistou) funkci, která na vstupu dostane průřez krajiny a
# spočte, kolik vody se v dané krajině udrží, bude-li na ni
# neomezeně pršet. Krajina je reprezentována sekvencí celých
# nezáporných čísel, kde každé reprezentuje výšku jednoho úseku.
# Všechny úseky jsou stejně široké a mimo popsaný úsek krajiny je
# všude výška 0.
#
# Například krajina ‹[3, 1, 2, 3, 2]› dokáže udržet 3 jednotky vody
# (mezi prvním a čtvrtým segmentem):
#
#   ┌───┐       ┌───┐
#   │   │       │   │
#   │   │   ┌───┤   ├───┐
#   │   │   │   │   │   │
#   │   ├───┤   │   │   │
#   │   │   │   │   │   │
#   └───┴───┴───┴───┴───┘
#     3   1   2   3   2

def lakes(land: list[int]) -> int:
    pass


def main() -> None:
    land = [0, 0, 0]
    assert lakes(land) == 0
    assert land == [0, 0, 0]

    assert lakes([20, 0, 1]) == 1
    assert lakes([1, 2, 3, 2, 1]) == 0
    assert lakes([3, 1, 2, 3, 2]) == 3
    assert lakes([2, 0, 1, 3, 2]) == 3
    assert lakes([4, 3, 2, 1, 0, 4]) == 10
    assert lakes([5, 6, 0, 3, 2, 5, 4, 1, 4, 2, 1, 3]) == 16

    land = [4, 3, 2, 3, 1, 4, 5, 5, 3, 2, 1, 3]
    assert lakes(land) == 10
    assert land == [4, 3, 2, 3, 1, 4, 5, 5, 3, 2, 1, 3]


if __name__ == '__main__':
    main()
