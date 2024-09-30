from ib111 import week_09  # noqa


class Tree:
    def __init__(self, left: 'Tree | None',
                 right: 'Tree | None') -> None:
        self.left = left
        self.right = right


def leaf() -> Tree:
    return Tree(None, None)


# AVL strom je binární strom, který:
#
# 1. je vyhledávací, tzn. splňuje vlastnost popsanou v ukázce
#    ‹d3_lookup›, a zároveň
# 2. pro každý jeho uzel platí ‹abs(l_height - r_height) ≤ 1›, kde
#    ‹l_height› a ‹r_height› jsou výšky levého a pravého podstromu
#    daného uzlu.
#
# Napište predikát, který ověří, že vstupní strom má tuto druhou
# vlastnost (je-li zároveň stromem vyhledávacím ověřovat nemusíte).
# Pokuste se vlastnost ověřit jediným průchodem stromu (tedy každý
# uzel navštivte pouze jednou – naivní řešení, kdy opakovaně
# počítáte výšky průchodem podstromů není příliš uspokojivé).

def is_avl(tree) -> bool:
    pass


def main() -> None:
    assert is_avl(None)
    assert is_avl(Tree(leaf(), leaf()))
    assert is_avl(Tree(None, leaf()))

    assert is_avl(Tree(Tree(Tree(leaf(), None), leaf()),
                       Tree(Tree(None, leaf()),
                            Tree(Tree(leaf(), leaf()), leaf()))))
    assert not is_avl(Tree(Tree(Tree(leaf(), None), leaf()),
                           Tree(leaf(), Tree(Tree(leaf(),
                                                  leaf()), leaf()))))
    assert not is_avl(Tree(Tree(leaf(), leaf()),
                           Tree(Tree(None, leaf()),
                                Tree(Tree(leaf(), leaf()), leaf()))))

    assert is_avl(Tree(Tree(leaf(),
                            Tree(leaf(), leaf())),
                       Tree(leaf(), leaf())))
    assert is_avl(Tree(Tree(leaf(), leaf()),
                       Tree(Tree(None, leaf()), leaf())))
    assert is_avl(Tree(Tree(leaf(), leaf()), Tree(leaf(), leaf())))
    assert is_avl(Tree(Tree(leaf(), None), Tree(None, leaf())))

    assert not is_avl(Tree(Tree(leaf(), None), None))
    assert not is_avl(Tree(Tree(leaf(), leaf()),
                           Tree(None, Tree(None, leaf()))))


if __name__ == "__main__":
    main()
