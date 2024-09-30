from ib111 import week_09  # noqa


# Uvažujme ternární stromy, které mají v uzlech uložena celá čísla:

class Tree:
    def __init__(self, value: int,
                 first: 'Tree | None',
                 second: 'Tree | None',
                 third: 'Tree | None'):
        self.value = value
        self.first = first
        self.second = second
        self.third = third


def leaf(value: int) -> Tree:
    return Tree(value, None, None, None)


# Napište čistou funkci, která na vstupu dostane instanci výše
# popsaného stromu a vrátí součet všech hodnot ve všech jeho uzlech.

def sum_tree(tree) -> int:
    pass


def main() -> None:
    t1 = leaf(5)
    t2 = Tree(1, leaf(2), leaf(3), leaf(4))
    t3 = Tree(2, None, leaf(1), None)
    t4 = Tree(10, t2, None, None)
    t5 = Tree(-5, leaf(5), t1, t4)

    assert sum_tree(t1) == 5
    assert sum_tree(t2) == 10
    assert sum_tree(t3) == 3
    assert sum_tree(t4) == 20
    assert sum_tree(t5) == 25


if __name__ == '__main__':
    main()
