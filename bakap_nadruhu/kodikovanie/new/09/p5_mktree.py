from ib111 import week_09  # noqa

# Uvažujme neprázdný strom s očíslovanými vrcholy (kořen má vždy
# číslo 1):
#
#             ┌───┐
#             │ 1 │
#             └───┘
#          ╭───╯ ╰─────╮
#          ▼           ▼
#        ┌───┐       ┌───┐
#        │ 2 │       │ 3 │
#        └───┘       └───┘
#    ╭────╯│╰────╮     │
#    │     │     │     │
#    ▼     ▼     ▼     ▼
#  ┌───┐ ┌───┐ ┌───┐ ┌───┐
#  │ 4 │ │ 5 │ │ 6 │ │ 7 │
#  └───┘ └───┘ └───┘ └───┘
#
# Tento strom zakódujeme do slovníku takto:

TreeDict = dict[int, list[int]]


def example_tree() -> TreeDict:
    return {1: [2, 3],
            2: [4, 5, 6],
            3: [7],
            4: [], 5: [], 6: [], 7: []}


# Klíče tohoto slovníku jsou čísla vrcholů a hodnoty jsou seznamy
# čísel jejich přímých potomků. Nejprve napište predikát, který
# ověří, že se jedná o korektně zadaný strom, tedy:
#
#  1. obsahuje kořen (uzel číslo 1),
#  2. každý vrchol se v seznamech potomků objevuje právě jednou,
#     s výjimkou kořene, který se zde neobjevuje vůbec,
#  3. žádný uzel není svým vlastním (přímým) potomkem.

def is_tree(tree: TreeDict) -> bool:
    pass


# Dále napište čistou funkci ‹make_tree›, která ze zadaného
# „slovníkového“ stromu ‹tree› vytvoří instanci třídy ‹Tree› tak,
# aby reprezentovala stejný strom. Vstupní podmínkou je, že ‹tree›
# je korektní strom, tzn. platí ‹is_tree(tree)›.

class Tree:
    def __init__(self, value: int, children: list["Tree"]):
        self.value: int = value
        self.children = children


def make_tree(tree: TreeDict) -> Tree:
    pass


def main() -> None:
    assert is_tree(example_tree())
    assert not is_tree({1: [1]})
    assert not is_tree({})
    assert not is_tree({1: [], 2: []})
    assert not is_tree({1: [], 2: [2]})
    assert not is_tree({1: [2], 2: [1]})
    tree = make_tree(example_tree())
    assert tree.value == 1
    assert len(tree.children) == 2
    assert tree.children[0].value == 2
    assert tree.children[1].value == 3
    assert len(tree.children[0].children) == 3
    assert len(tree.children[1].children) == 1
    assert len(tree.children[0].children[0].children) == 0
    assert tree.children[0].children[0].value == 4
    assert tree.children[0].children[1].value == 5
    assert tree.children[0].children[2].value == 6
    assert tree.children[1].children[0].value == 7
    assert len(tree.children[0].children[1].children) == 0
    assert len(tree.children[0].children[2].children) == 0
    assert len(tree.children[1].children[0].children) == 0


if __name__ == "__main__":
    main()
