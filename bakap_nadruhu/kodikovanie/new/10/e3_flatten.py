from ib111 import week_10  # noqa

# Typ pro libovolně zanořený seznam znáte z přednášky:

NestedList = list['int | NestedList']


# Vaším úkolem je napsat čistou funkci, která na vstupu dostane
# ‹NestedList› (vnořený seznam celých čísel) a vrátí obyčejný
# seznam, který zachovává pořadí čísel na vstupu, ale „zapomene“
# strukturu vnoření.

def flatten(to_flatten: NestedList) -> list[int]:
    pass


def main() -> None:
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[[[1]], [2]], 3]) == [1, 2, 3]
    assert flatten([[1, 2], [[7, 4], [5]]]) \
        == [1, 2, 7, 4, 5]


if __name__ == '__main__':
    main()
