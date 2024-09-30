from ib111 import week_09  # noqa


class Tree:
    def __init__(self, key: int,
                 left: 'Tree | None',
                 right: 'Tree | None'):
        self.key = key
        self.left = left
        self.right = right


def leaf(key: int) -> Tree:
    return Tree(key, None, None)


# Binární halda je binární strom, který má dvě speciální vlastnosti
# uvedené níže. V tomto příkladu budeme kontrolovat pouze tu druhou,
# totiž vlastnost haldy:
#
#  1. každé patro je plné (s možnou výjimkou posledního),
#  2. hodnota každého uzlu je větší nebo rovna hodnotě libovolného
#     jeho potomka.
#
# Predikát ‹is_heap› rozhodne, splňuje-li vstupní strom tuto druhou
# vlastnost.

def is_heap(tree) -> bool:
    pass


def main() -> None:
    assert is_heap(None)
    assert is_heap(leaf(1))
    assert is_heap(Tree(1, leaf(0), leaf(0)))
    assert is_heap(Tree(1, leaf(1), leaf(1)))
    assert is_heap(Tree(1, leaf(0), None))
    assert not is_heap(Tree(1, leaf(2), leaf(0)))
    assert not is_heap(Tree(1, leaf(1), leaf(2)))
    assert not is_heap(Tree(1, leaf(8), None))

    assert is_heap(Tree(10, Tree(9,
                                 Tree(7, leaf(3), leaf(2)),
                                 Tree(6, leaf(1), leaf(0))),
                        Tree(8, leaf(5), leaf(4))))
    assert not is_heap(Tree(10, Tree(9,
                                     Tree(7, leaf(3), leaf(2)),
                                     Tree(10, leaf(1), leaf(0))),
                            Tree(8, leaf(5), leaf(4))))
    assert not is_heap(Tree(10, Tree(9,
                                     Tree(7, leaf(3), leaf(2)),
                                     Tree(6, leaf(1), leaf(0))),
                            Tree(8, leaf(5), leaf(9))))
    assert not is_heap(Tree(10, Tree(9,
                                     Tree(7, leaf(3), leaf(2)),
                                     Tree(6, leaf(11), leaf(0))),
                            Tree(8, leaf(5), leaf(4))))
    assert not is_heap(Tree(10, Tree(11,
                                     Tree(7, leaf(3), leaf(2)),
                                     Tree(6, leaf(1), leaf(0))),
                            Tree(8, leaf(5), leaf(4))))
    assert not is_heap(Tree(-10, Tree(9,
                                      Tree(7, leaf(3), leaf(2)),
                                      Tree(6, leaf(1), leaf(0))),
                            Tree(8, leaf(5), leaf(4))))


if __name__ == "__main__":
    main()
