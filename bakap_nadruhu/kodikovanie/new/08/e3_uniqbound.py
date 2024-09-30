from ib111 import week_08  # noqa


# Napište čistou funkci, která najde v zadaném uspořádaném seznamu
# ‹numbers› největší číslo, které není větší než parametr ‹value›.
# Neexistuje-li takové, vraťte ‹None›.
#
# V ostatních případech je tedy výsledkem vždy číslo, které se
# nachází v ‹numbers› a vždy platí ‹lower_bound(numbers, x) ≤ x›.
#
# Předpokládejte, že v seznamu ‹numbers› se čísla neopakují.
# Očekávaná složitost řešení je logaritmická.

def lower_bound(numbers: list[int], value: int) -> int | None:
    pass


def main() -> None:
    assert lower_bound([1, 2, 3], 2) == 2
    assert lower_bound([1, 3, 5], 2) == 1
    assert lower_bound([1, 2, 3, 4, 5, 6], 6) == 6
    assert lower_bound([], 2) is None
    assert lower_bound([1, 2, 3], -2) is None
    assert lower_bound([-5, -1, 8, 90], 2) == -1
    assert lower_bound([-5, -1, 0], 2) == 0
    assert lower_bound([1, 3], 2) == 1
    assert lower_bound([1, 3], 1) == 1
    assert lower_bound([-5, -1, 0, 2], 2) == 2
    assert lower_bound([-5, -1, 0, 1], 2) == 1


if __name__ == '__main__':
    main()
