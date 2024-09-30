from ib111 import week_09  # noqa


# Uvažme n-ární strom, který má v uzlech uloženu volitelnou hodnotu
# typu ‹int›.

class Tree:
    def __init__(self, children: list["Tree"]):
        self.value: int | None = None
        self.children = children


# Napište proceduru, která obdrží instanci výše popsaného stromu, a
# vyplní atributy ‹value› všech jeho uzlů tak, aby byl v každém uzlu
# uložen celkový počet jeho potomků (tedy včetně nepřímých).
# Správné řešení má složitost lineární vůči počtu uzlů stromu.

def count_children(tree) -> None:
    pass


def main() -> None:
    t1 = Tree([])
    count_children(t1)
    assert get_value(t1, []) == 0

    t2 = Tree([Tree([]), Tree([])])
    count_children(t2)
    assert get_value(t2, []) == 2
    assert get_value(t2, [0]) == 0
    assert get_value(t2, [1]) == 0

    t3 = Tree([Tree([]), Tree([Tree([Tree([])])])])
    count_children(t3)
    assert get_value(t3, []) == 4
    assert get_value(t3, [0]) == 0
    assert get_value(t3, [1]) == 2
    assert get_value(t3, [1, 0]) == 1
    assert get_value(t3, [1, 0, 0]) == 0

    t4 = Tree([Tree([]),
               Tree([Tree([Tree([]), Tree([])])]),
               Tree([])])
    count_children(t4)
    assert get_value(t4, []) == 6
    assert get_value(t4, [0]) == 0
    assert get_value(t4, [1]) == 3
    assert get_value(t4, [2]) == 0
    assert get_value(t4, [1, 0]) == 2
    assert get_value(t4, [1, 0, 0]) == 0
    assert get_value(t4, [1, 0, 1]) == 0


def get_value(tree: Tree, indices: list[int]) -> int:
    for idx in indices:
        tree = tree.children[idx]
    assert tree.value is not None
    return tree.value


if __name__ == '__main__':
    main()
