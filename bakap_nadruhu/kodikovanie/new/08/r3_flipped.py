from ib111 import week_08  # noqa


# Implementujte predikát ‹is_almost_sorted›, který je pravdivý,
# je-li v seznamu ‹items› potřeba prohodit právě jednu dvojici
# různých čísel, aby se stal vzestupně seřazeným.
# Existuje řešení, jehož časová složitost je lineární.

def is_almost_sorted(items: list[int]) -> bool:
    pass


def main() -> None:
    items = [1, 0, 0, 0]
    assert is_almost_sorted(items)
    assert items == [1, 0, 0, 0]

    assert is_almost_sorted([1, 0, 0, 2])
    assert is_almost_sorted([0, 1, 0, 0, 2])
    assert is_almost_sorted([0, 2, 0, 0, 2, 0])
    assert is_almost_sorted([1, 2, 4, 3, 5])
    assert is_almost_sorted([1, 5, 3, 4, 2])
    assert is_almost_sorted([5, 2, 3, 4, 1])
    assert not is_almost_sorted([4, 5, 6, 7, 8])
    assert not is_almost_sorted([2, 2, 4, 4, 4])
    assert not is_almost_sorted([5, 1, 3, 4, 2])
    assert not is_almost_sorted([5, 4, 3, 2, 1])

    items = [1, 2, 5, 3, 4]
    assert not is_almost_sorted(items)
    assert items == [1, 2, 5, 3, 4]


if __name__ == "__main__":
    main()
