from ib111 import week_12  # noqa


# Máte připraveny třídy, které budou tvořit AST (abstraktní syntaktický strom)
# velmi jednoduchého programu:
#
#  • ‹Arithmetic› reprezentuje binární aritmetickou operaci;
#    její objekty mají atributy ‹op› (jeden z řetězců ‹'+'›, ‹'-'›,
#    ‹'*'›, ‹'/'›), ‹left› (levý operand), ‹right› (pravý operand).
#  • ‹Assignment› reprezentuje přiřazení; její objekty mají atributy
#    ‹var› (řetězec, jméno proměnné na levé straně přiřazení) a ‹rhs›
#    (pravá strana přiřazení).
#
# Dále je připraven typový alias ‹Expression›, který reprezentuje
# uzel stromu výrazu – buď číslo typu int nebo řetězec (reprezentuje
# proměnnou) nebo objekt typu ‹Arithmetic›. Výše uvedené atributy
# ‹left›, ‹right› a ‹rhs› jsou typu ‹Expression›.
#
# Tyto třídy ani typový alias ‹Expression› nijak nemodifikujte.

class Arithmetic:
    def __init__(self, op: str, left: 'Expression',
                 right: 'Expression'):
        self.op = op
        self.left = left
        self.right = right


Expression = Arithmetic | str | int


class Assignment:
    def __init__(self, var: str, rhs: Expression):
        self.var = var
        self.rhs = rhs


# Napište čistou funkci, která dostane na vstupu jednoduchý program ve formě
# seznamu přiřazení a vrátí slovník reprezentující hodnoty proměnných na konci
# programu. Pokud během vykonávání programu dojde k chybě (dělení nulou nebo
# použití proměnné, které předtím nebyla přiřazena hodnota), funkce vrátí
# ‹None›. Dělení je vždy celočíselné (i když je reprezentováno znakem ‹/›).

def execute(program: list[Assignment]) -> dict[str, int] | None:
    pass


def main() -> None:
    # a = 2 + 2
    ar1 = Arithmetic('+', 2, 2)
    as1 = Assignment('a', ar1)
    # b = 10 / a
    ar2 = Arithmetic('/', 10, 'a')
    as2 = Assignment('b', ar2)
    prog1 = [as1, as2]
    assert execute(prog1) == {'a': 4, 'b': 2}
    assert prog1 == [as1, as2]
    assert as2.var == 'b' and as2.rhs == ar2
    assert ar2.op == '/' and ar2.left == 10 and ar2.right == 'a'
    assert as1.var == 'a' and as1.rhs == ar1
    assert ar1.op == '+' and ar1.left == 2 and ar1.right == 2

    # a = 2 - 2
    # b = 10 / a
    prog2 = [
        Assignment('a', Arithmetic('-', 2, 2)),
        Assignment('b', Arithmetic('/', 10, 'a')),
    ]
    assert execute(prog2) is None

    # a = (1 + 2) * 3
    # b = a + 2 * 3
    # a = a + 7
    prog3 = [
        Assignment('a', Arithmetic('*', Arithmetic('+', 1, 2), 3)),
        Assignment('b', Arithmetic('+', 'a', Arithmetic('*', 2, 3))),
        Assignment('a', Arithmetic('+', 'a', 7)),
    ]
    assert execute(prog3) == {'a': 16, 'b': 15}

    # a = 17
    # b = 42
    # tmp = a
    # a = b
    # b = tmp
    # tmp = 0
    prog4 = [
        Assignment('a', 17),
        Assignment('b', 42),
        Assignment('tmp', 'a'),
        Assignment('a', 'b'),
        Assignment('b', 'tmp'),
        Assignment('tmp', 0),
    ]
    assert execute(prog4) == {'a': 42, 'b': 17, 'tmp': 0}

    # a = 1 + a
    prog5 = [
        Assignment('a', Arithmetic('+', 1, 'a')),
    ]
    assert execute(prog5) is None

    # a = 0
    # a = 1 + a
    prog6 = [
        Assignment('a', 0),
        Assignment('a', Arithmetic('+', 1, 'a')),
    ]
    assert execute(prog6) == {'a': 1}

    # result = 17 + 42 * 9 / 2 - 13 * (3 + 7)
    prog7 = [
        Assignment(
            'result',
            Arithmetic(
                '-',
                Arithmetic(
                    '+',
                    17,
                    Arithmetic(
                        '/',
                        Arithmetic('*', 42, 9),
                        2)),
                Arithmetic(
                    '*',
                    13,
                    Arithmetic('+', 3, 7))))
    ]
    assert execute(prog7) == {'result': 76}


if __name__ == '__main__':
    main()
