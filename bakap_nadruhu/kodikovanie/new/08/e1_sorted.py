from ib111 import week_08  # noqa


# Napište predikát ‹is_sorted›, který rozhodne, je-li vstupní seznam
# vzestupně seřazený. Existuje řešení, jehož složitost je lineární.

def is_sorted(num_list: list[int]) -> bool:
    pass


def main() -> None:
    assert is_sorted([])
    assert is_sorted([-1])
    assert is_sorted([-1, 0, 1])
    assert is_sorted([0, 1, 1])
    assert is_sorted([-5, -1, -1, 0, 45, 2000])

    assert not is_sorted([1, -1])
    assert not is_sorted([0, -1])
    assert not is_sorted([1, 2, 3, 2, 4, 5])
    assert not is_sorted([5, 1, 2, 3, 4])
    assert not is_sorted([1, 2, 3, 4, 1])


if __name__ == "__main__":
    main()
