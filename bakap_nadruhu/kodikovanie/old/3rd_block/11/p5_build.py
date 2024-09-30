from ib111 import week_11  # noqa


# † V tomto příkladu budeme pracovat s n-árními stromy, které nemají
# v uzlech žádné hodnoty (mají pouze stromovou strukturu).
# Třídu Tree nijak nemodifikujte.

class Tree:
    def __init__(self) -> None:
        self.children: list[Tree] = []


# Napište (čistou) funkci, které na základě dobře uzávorkovaného
# řetězce tvořeného pouze znaky ‹(› a ‹)› vybuduje instanci výše
# popsaného stromu, a to tak, že každý pár závorek reprezentuje
# jeden uzel, a jejich obsah reprezentuje podstrom, který v tomto
# uzlu začíná. Ve vstupním řetězci bude vždy alespoň jeden pár
# závorek.

def build_tree(brackets: str) -> Tree:
    root = Tree()
    stak = [root]

    for brat in brackets:
        if brat == "(":
            new_node = Tree()
            stak[-1].children.append(new_node)
            stak.append(new_node)
        elif brat == ")":
            stak.pop()

    return root.children[0]


def main() -> None:
    t2 = build_tree("()")
    assert len(t2.children) == 0

    t3 = build_tree("(()(()())(()))")
    assert len(t3.children) == 3
    assert len(t3.children[0].children) == 0
    assert len(t3.children[1].children) == 2
    assert len(t3.children[1].children[0].children) == 0
    assert len(t3.children[1].children[1].children) == 0
    assert len(t3.children[2].children) == 1
    assert len(t3.children[2].children[0].children) == 0

    t4 = build_tree("(((())))")
    assert len(t4.children) == 1
    assert len(t4.children[0].children) == 1
    assert len(t4.children[0].children[0].children) == 1
    assert len(t4.children[0].children[0].children[0].children) == 0


if __name__ == '__main__':
    main()
