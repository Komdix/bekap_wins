from ib111 import week_10  # noqa


# Napište čistou funkci, která dostane na vstup množinu čísel a
# vrátí seznam všech jejích podmnožin (v libovolném pořadí).

def subsets(input_set: set[int]) -> list[set[int]]:
    pass


def main() -> None:
    subsets_test(set())
    subsets_test({1})
    subsets_test({1, 2})
    subsets_test({1, 2, 3})
    subsets_test({-2, 0, 25, 100})


def subsets_test(input_set: set[int]) -> None:
    copy = input_set.copy()
    sets = subsets(input_set)
    count = 2 ** len(input_set)
    assert input_set == copy

    if len(sets) != count:
        assert len(sets) != count, (len(sets), '≠', count)

    for i in range(count):
        for j in range(i):
            assert sets[i] != sets[j], (i, j, sets[i])

    for subset in sets:
        assert subset <= input_set, (subset, '⊆', input_set)


if __name__ == '__main__':
    main()
