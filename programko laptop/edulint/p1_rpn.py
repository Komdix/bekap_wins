from ib111 import week_06  # noqa


# Napište (čistou) funkci, která na vstupu dostane:
#
#  • neprázdný výraz ‹expr› složený z proměnných a z aritmetických
#    operátorů, zapsaný v postfixové notaci, a
#  • slovník, přiřazující proměnným číselnou hodnotu (můžete se
#    spolehnout, že všechny proměnné použité v daném výrazu jsou
#    v tomto slovníku obsaženy),
#
# a vrátí číslo, na které se daný výraz vyhodnotí. Každý operátor
# nebo proměnná je samostatný řetězec, celý výraz je pak tvořen
# posloupností těchto řetězců. Povolené operátory jsou pouze ‹+› a
# ‹*›.

# Postfixová notace funguje následovným způsobem:
#
#  • výraz čteme zleva doprava, přitom si každou hodnotu zapíšeme,
#  • narazíme-li na operátor, např. ‹+›:
#    ◦ v hlavě sečteme poslední dvě hodnoty které jsme napsali,
#    ◦ tyto hodnoty smažeme,
#    ◦ zapíšeme místo nich součet, který jsme si zapamatovali.
#
# Tento postup opakujeme, až dokud nepřečteme celý výraz. Je-li
# výraz správně utvořený, na konci tohoto procesu máme zapsané
# jediné číslo. Toto číslo je výsledkem vyhodnocení zadaného výrazu.


def pop_append(lst: list[int], temp_sum: int) -> list[int]:
    for _ in range(2):
        lst.pop()
    lst.append(temp_sum)
    return lst


def rpn_eval(expr: list[str], variables: dict[str, int]) -> int:

    lst: list[int] = []

    for item in expr:
        if item != "+" and item != "*":
            convert_variable = variables.get(item)
            assert convert_variable is not None
            lst.append(convert_variable)
        if item == "+":
            temp_sum = lst[-1] + lst[-2]
            pop_append(lst, temp_sum)
        if item == "*":
            temp_sum = lst[-1] * lst[-2]
            pop_append(lst, temp_sum)
    return lst[0]


def main() -> None:
    assert rpn_eval(["a"], {"a": 5}) == 5
    assert rpn_eval(["a", "b", "+"], {"a": 1, "b": -4}) == -3
    assert rpn_eval(["x", "y", "+"], {"x": 1, "y": 2}) == 3
    assert rpn_eval(["x", "y", "+", "y", "*", "z", "+"],
                    {"x": 5, "y": 2, "z": 25}) == 39
    assert rpn_eval(["x", "x", "*", "x", "*"],
                    {"x": 5}) == 125
    assert rpn_eval(["a", "a", "a", "a", "a", "a", "+", "+", "+",
                     "+", "+"], {"a": 1}) == 6


if __name__ == '__main__':
    main()
