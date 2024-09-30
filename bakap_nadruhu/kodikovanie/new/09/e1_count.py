from ib111 import week_09  # noqa


# Třída ‹Tree› reprezentuje (neohodnocený) binární strom. Prázdný
# strom je reprezentován hodnotou ‹None›.

class Tree:
    def __init__(self, left: 'Tree | None',
                 right: 'Tree | None'):
        self.left = left
        self.right = right


def leaf() -> Tree:
    return Tree(None, None)


# Napište čistou funkci, která vrátí počet uzlů v zadaném stromě.

def count(tree: Tree | None) -> int:
    pass


def main() -> None:
    assert count(leaf()) == 1
    assert count(Tree(Tree(leaf(), leaf()), leaf())) == 5
    assert count(Tree(leaf(), None)) == 2
    assert count(None) == 0
    assert count(Tree(leaf(),
                      Tree(None,
                           Tree(Tree(leaf(), None), None)))) == 6


if __name__ == "__main__":
    main()
