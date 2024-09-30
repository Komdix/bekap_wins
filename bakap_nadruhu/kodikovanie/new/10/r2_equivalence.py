from ib111 import week_10  # noqa

# Z předmětu IB000 Matematické základy informatiky víme, že každá
# relace ekvivalence na nějaké množině M jednoznačně určuje
# rozklad množiny M, tedy množinu vzájemně disjunktních podmnožin,
# jejichž sjednocením je celá množina M.
# Platí to i naopak, každý rozklad jednoznačně určuje relaci
# ekvivalence.
#
# Například na množině M = {1, 2, 3} můžeme definovat relaci
# ekvivalence {(1, 1), (2, 2), (2, 3), (3, 2), (3, 3)}, které
# odpovídá rozklad [{1}, {2, 3}]
#
# Napište funkci partition2pairs, která jako parametr dostane
# rozklad množiny (tedy seznam podmnožin) a vrátí množinu
# uspořádaných dvojic, které představují odpovídající relaci
# ekvivalence.
# Dále napište funkci pairs2partitions, která z relace zadané
# jako množina uspořádaných dvojic vytvoří odpovídajíí rozklad
# (seznam podmnožin).
# V obou případech můžete předpokldádat, že vstup je korektní.

Pair = tuple[int, int]


def partition2pairs(partition: list[set[int]]) -> set[Pair]:
    pass


def pairs2partition(pairs: set[Pair]) -> list[set[int]]:
    pass


def main() -> None:
    assert partition2pairs([]) == set()
    assert partition2pairs([{99}]) == {(99, 99)}
    assert partition2pairs([{1}, {2, 3}]) == \
           {(1, 1), (2, 3), (3, 3), (2, 2), (3, 2)}
    assert partition2pairs([{1, 2, 3}]) == \
           {(1, 2), (2, 1), (3, 1),
            (1, 1), (2, 3), (3, 3),
            (2, 2), (3, 2), (1, 3)}

    assert pairs2partition(set()) == []
    equiv1 = {(1, 1), (2, 2), (2, 3), (3, 2), (3, 3)}
    equiv2 = {(1, 1), (2, 2), (3, 3)}
    assert test_equal(pairs2partition(equiv1), [{2, 3}, {1}])
    assert test_equal(pairs2partition(equiv2), [{1}, {3}, {2}])


def test_equal(list1: list[set[int]],
               list2: list[set[int]]) -> bool:
    for elem in list1:
        if elem not in list2:
            return False
    for elem in list2:
        if elem not in list1:
            return False
    return True


if __name__ == '__main__':
    main()
