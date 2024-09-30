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


# Napište čistou funkci, která vrátí hloubku zadaného stromu, tzn.
# délku jeho nejdelší větve (posloupnosti uzlů od kořene k listu).

def depth(tree: Tree | None) -> int:
    pass


def main() -> None:
    assert depth(leaf()) == 1
    assert depth(Tree(Tree(leaf(), leaf()), leaf())) == 3
    assert depth(Tree(leaf(), Tree(leaf(), leaf()))) == 3
    assert depth(Tree(leaf(), None)) == 2
    assert depth(None) == 0
    assert depth(Tree(leaf(),
                      Tree(None,
                           Tree(Tree(leaf(), None), None)))) == 5
    assert depth(Tree(Tree(leaf(),
                           Tree(Tree(Tree(leaf(), None), None),
                                leaf())), Tree(None,
                                               Tree(Tree(leaf(),
                                                         None),
                                                    None)))) == 6


if __name__ == "__main__":
    main()
