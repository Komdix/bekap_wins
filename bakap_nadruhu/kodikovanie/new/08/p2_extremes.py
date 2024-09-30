from ib111 import week_08  # noqa

# Napište čistou funkci ‹local_extremes›, která dostane na vstupu
# seznam ‹values› čísel a vrátí dvojici seznamů ‹min_indices,
# max_indices›. Každý prvek seznamu ‹values› je unikátní. Seznam
# ‹min_indices› (‹max_indices›) bude obsahovat indexy lokálních
# minim (maxim) seznamu ‹values›. Oba tyto seznamy budou vzestupně
# seřazené. Řešení očekáváme v lineární časové složitosti.

Minima = list[int]
Maxima = list[int]


def local_extremes(values: list[int]) -> tuple[Minima, Maxima]:
    pass


def main() -> None:
    assert local_extremes([1, 4, 2, 0]) == ([0, 3], [1])
    assert local_extremes([3, 1, 5, 4, 0, 2]) == ([1, 4], [0, 2, 5])
    assert local_extremes([3, 1, 5, 6, 0, 2]) == ([1, 4], [0, 3, 5])
    assert local_extremes([3, 1, 0]) == ([2], [0])
    assert local_extremes([0, 1, 2]) == ([0], [2])
    assert local_extremes([]) == ([], [])
    assert local_extremes([2]) == ([0], [0])
    assert local_extremes([1, 2]) == ([0], [1])


if __name__ == "__main__":
    main()
