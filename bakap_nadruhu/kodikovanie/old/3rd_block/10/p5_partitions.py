from ib111 import week_10  # noqa


# † Rozkladem množiny M je množina neprázdných množin P₁, P₂, … Pₙ,
# které jsou vzájemně disjunktní a jejichž sjednocením je celá
# množina M.
#
# Máme-li například množinu M = {1, 2, 3}, pak všechny její rozklady
# jsou:
#
#     {{1}, {2}, {3}}
#     {{1}, {2, 3}}
#     {{2}, {1, 3}}
#     {{3}, {1, 2}}
#     {{1, 2, 3}}
#
# Vaším úkolem bude napsat čistou funkci, která vygeneruje všechny
# rozklady dané množiny celých čísel. Pro zjednodušení nebudeme
# pracovat s datovým typem množina, ale všechny množiny budeme
# reprezentovat pomocí seznamů. Můžete předpokládat, že jednotlivé
# prvky vstupního seznamu jsou unikátní.

NumSet = list[int]
Partitions = list[list[list[int]]]


def partitions(nums: NumSet) -> Partitions:
    pass


def main() -> None:
    partitions_test(partitions([]), [])
    partitions_test(partitions([1]), [1])
    partitions_test(partitions([1, 2]), [1, 2])
    partitions_test(partitions([1, 2, 3]), [1, 2, 3])
    list1 = [100, 99, 98, 97, 96, 95]
    partitions_test(partitions(list1), list1)


def partitions_test(all_partitions: Partitions, original_set: NumSet) -> None:
    # check the number of partitions
    assert len(all_partitions) == bell_number(len(original_set))

    # make sure there are no duplicates
    for i, p1 in enumerate(all_partitions):
        for j in range(i + 1, len(all_partitions)):
            p2 = all_partitions[j]
            assert sorted(p1) != sorted(p2)

    # make sure the list contains correct partitions
    for partition in all_partitions:
        assert test_disjoint(partition)
        assert test_union(partition, original_set)


def test_disjoint(sets: list[NumSet]) -> bool:
    for i, a in enumerate(sets):
        for j in range(i + 1, len(sets)):
            b = sets[j]
            if set(a) & set(b):
                return False
    return True


def test_union(sets: list[NumSet], original_set: NumSet) -> bool:
    union = []
    for a in sets:
        union.extend(a)
    return set(union) == set(original_set)


def bell_number(n: int) -> int:
    bell_table: list[list[int]] = \
                [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell_table[0][0] = 1

    for i in range(1, n + 1):
        bell_table[i][0] = bell_table[i - 1][i - 1]

        for j in range(1, i + 1):
            bell_table[i][j] = bell_table[i - 1][j - 1] + bell_table[i][j - 1]

    return bell_table[n - 1][n - 1]


if __name__ == '__main__':
    main()
