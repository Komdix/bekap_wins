from ib111 import week_09  # noqa


# V tomto příkladu budeme pracovat se stromy, které reprezentují
# aritmetické výrazy. Tyto mají následující strukturu:
#
#  • konstantu reprezentuje strom, který má oba podstromy prázdné,
#  • složený výraz je reprezentován stromem, který má v kořenu
#    uložen operátor (‹+› nebo ‹*›) a jeho neprázdné podstromy
#    reprezentují operandy.
#
# Žádné jiné uzly ve stromě přítomny nebudou.

class Tree:
    def __init__(self, value: str | int,
                 left: 'Tree | None',
                 right: 'Tree | None'):
        self.value = value
        self.left = left
        self.right = right


def leaf(value: int) -> Tree:
    return Tree(value, None, None)


# Napište čistou funkci, která na vstupu dostane instanci výše
# popsaného stromu a vrátí výsledek vyhodnocení výrazu, který
# tento strom reprezentuje.

def evaluate(tree) -> int:
    pass


def main() -> None:
    t1 = leaf(5)
    t2 = Tree("+", leaf(2), leaf(4))
    t3 = Tree("*", t1, t2)
    t4 = Tree("*", leaf(0), t3)

    assert evaluate(t1) == 5
    assert evaluate(t2) == 6
    assert evaluate(t3) == 30
    assert evaluate(t4) == 0


if __name__ == '__main__':
    main()
