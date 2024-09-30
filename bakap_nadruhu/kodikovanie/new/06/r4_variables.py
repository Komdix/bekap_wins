from ib111 import week_06  # noqa

# Uvažujme jednoduché aritmetické výrazy se sčítáním a násobením.
# Budeme je ukládat do dvojice slovníků (‹expr› a ‹const›), a to
# následovně:
#
#  • klíč je vždy jméno proměnné (řetězec),
#  • hodnota ve slovníku ‹expr› je trojice:
#    ◦ první složka je operátor ‹'*'› nebo ‹'+'›,
#    ◦ druhá a třetí složka jsou operandy – názvy proměnných,
#  • hodnota ve slovníku ‹const› je číslo.
#
# Každá proměnná se objeví v nejvýše jednom slovníku. Proměnné,
# které se nenachází v žádném z nich jsou rovny nule.

# Napište čistou funkci, která dostane jako parametry slovníky
# ‹expr› a ‹const› a název proměnné. Výsledkem bude hodnota této
# proměnné. Při vyhodnocování se Vám bude hodit zásobník a pomocný
# slovník.


def evaluate(expr: dict[str, tuple[str, str, str]],
             const: dict[str, int], var: str) -> int:
    pass


def main() -> None:
    assert evaluate({}, {'a': 1}, 'a') == 1
    assert evaluate({'x': ('+', 'a', 'a')}, {'a': 1}, 'x') == 2
    assert evaluate({'x': ('+', 'a', 'b')},
                    {'a': 1, 'b': 2}, 'x') == 3
    assert evaluate({'x': ('+', 'a', 'b'), 'y': ('*', 'x', 'x')},
                    {'a': 1, 'b': 2}, 'x') == 3
    assert evaluate({'x': ('+', 'a', 'b'), 'y': ('*', 'x', 'x')},
                    {'a': 1, 'b': 2}, 'y') == 9


if __name__ == "__main__":
    main()
