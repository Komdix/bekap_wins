from ib111 import week_09  # noqa
from math import isclose


class Tree:
    def __init__(self, left: 'Tree | None',
                 right: 'Tree | None') -> None:
        self.left = left
        self.right = right


def leaf() -> Tree:
    return Tree(None, None)


# Napište čistou funkci, která pro vstupní binární strom spočítá
# průměrnou délku větve (cesty od kořene k listu).
# K řešení úlohy je postačující projít strom jen jednou.

def average_branch_len(tree) -> float:
    pass


def main() -> None:
    assert isclose(average_branch_len(None), 0)
    assert isclose(average_branch_len(leaf()), 1)
    assert isclose(average_branch_len(Tree(leaf(), None)), 2)
    assert isclose(average_branch_len(Tree(leaf(), leaf())), 2)

    assert isclose(average_branch_len(
        Tree(Tree(leaf(), None), Tree(leaf(), Tree(leaf(), None)))),
        10.0 / 3.0)
    assert isclose(average_branch_len(
        Tree(Tree(leaf(), leaf()),
             Tree(Tree(leaf(), leaf()),
                  Tree(Tree(leaf(), leaf()), leaf())))), 28.0 / 7.0)
    assert isclose(average_branch_len(
        Tree(None, Tree(Tree(None, Tree(
            Tree(None, leaf()), None)), None))), 6)
    assert isclose(average_branch_len(
        Tree(Tree(Tree(leaf(), None), None), leaf())), 3)
    assert isclose(average_branch_len(
        Tree(Tree(Tree(Tree(leaf(), None), None), None), leaf())), 7.0 / 2.0)


if __name__ == "__main__":
    main()
