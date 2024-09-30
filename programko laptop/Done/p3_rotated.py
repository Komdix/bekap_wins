from ib111 import week_08  # noqa


# Implementujte predikát ‹is_cyclically_sorted›, který je pravdivý,
# je-li seznam cyklicky seřazený. Seznam je cyklicky seřazený,
# existuje-li rotace, po které bude seřazený vzestupně.
# Měli byste být schopni napsat řešení, jehož složitost je lineární.


def is_cyclically_sorted(records: list[int]) -> bool:
    if len(records) < 2:
        return True

    min_num = min(records)
    max_num = max(records)
    min_index = records.index(min_num)
    max_index = records.index(max_num)
    last = records[min_index]
    iterations = 0

    for i in range(len(records) - min_index):
        expect = records[min_index + i]
        if last > expect and expect != min_num:
            return False
        last = expect
        iterations += 1

    if last != max_num and iterations != len(records):
        for i in range(max_index + 1):
            expect = records[i]
            if last > expect and expect != min_num:
                return False
            iterations += 1

    return iterations == len(records)


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
