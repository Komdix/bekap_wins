from ib111 import week_08  # noqa


# Implementujte predikát ‹is_cyclically_sorted›, který je pravdivý,
# je-li seznam cyklicky seřazený. Seznam je cyklicky seřazený,
# existuje-li rotace, po které bude seřazený vzestupně.
# Měli byste být schopni napsat řešení, jehož složitost je lineární.

def is_cyclically_sorted(records: list[int]) -> bool:
    pass


def main() -> None:
    assert is_cyclically_sorted([])
    assert is_cyclically_sorted([0])
    assert is_cyclically_sorted([1, 2, 3, 4, 5])
    assert is_cyclically_sorted([5, 1, 2, 3, 4])
    assert is_cyclically_sorted([5, -1, 2, 3, 4])
    assert is_cyclically_sorted([3, 4, 5, 1, 2])
    assert is_cyclically_sorted([3, 4, 5, 1, 2])
    assert is_cyclically_sorted([2, 3, 4, 5, 1])
    assert not is_cyclically_sorted([2, 3, 4, 5, 3])
    assert not is_cyclically_sorted([4, 2, 3, 1, 5])
    assert not is_cyclically_sorted([4, 3, 2, 1, 2])
    assert not is_cyclically_sorted([5, 4, 3, 2, 1])
    for n in range(3, 15):
        seq = [i for i in range(n)]
        assert is_cyclically_sorted(seq + [0])
        assert not is_cyclically_sorted(seq + [1, 0])


if __name__ == "__main__":
    main()
