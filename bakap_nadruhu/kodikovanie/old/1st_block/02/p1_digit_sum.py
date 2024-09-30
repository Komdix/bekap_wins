from ib111 import week_02  # noqa


# Implementujte funkci ‹power_digit_sum›, která vrátí „speciální“
# ciferný součet čísla ‹number›, který se od běžného ciferného
# součtu liší tím, že každou cifru před přičtením umocníme na číslo
# její pozice. Pozice číslujeme zleva, přičemž první má číslo 1.
# Vstupem funkce ‹power_digit_sum› bude libovolné nezáporné celé
# číslo, na výstupu se očekává celé číslo. Výpočet budeme provádět
# v číselné soustavě se základem 7.

# Příklad: Číslo ⟦1234⟧ zapíšeme v sedmičkové soustavě jako
# ⟦(3412)₇⟧ – skutečně, ⟦3⋅7³ + 4⋅7² + 1⋅7¹ + 2⋅7⁰ = 1029 + 196 + 7
# + 2 = 1234⟧.  Proto ‹power_digit_sum(1234)› získáme jako ⟦3¹ + 4²
# + 1³ + 2⁴ = 36⟧.


def power_digit_sum(number):
    n = number
    count = 0
    converted = 0
    kek = 0
    while n > 0:
        count += 1
        n //= 7

    for i in range(count, 0, -1):
        kek = number % 7
        converted += kek ** i
        number //= 7
    return converted


def main() -> None:
    assert power_digit_sum(7) == 1
    assert power_digit_sum(1234) == 36
    assert power_digit_sum(333) == 95
    assert power_digit_sum(52891) == 46693


if __name__ == "__main__":
    main()
