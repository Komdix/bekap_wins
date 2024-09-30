from ib111 import week_04  # noqa


# Fibonácci používají k zápisu kladných celých čísel Fibonacciho soustavu.
# Ta používá jen dvě číslice 0 a 1; řády čísel ovšem nejsou mocniny dvou
# jako v klasické dvojkové soustavě, ale jsou postupně zprava 1, 2, 3, 5,
# 8, 13, … (Jde tedy o Fibonacciho čísla bez úvodních 0 a 1.)
# Některá čísla je takto možno zapsat dvěma různými způsoby, např. číslo
# ⟦17⟧ se zapíše buď jako ⟦(100101)ᵩ⟧ nebo jako ⟦(11101)ᵩ⟧.
# Platí totiž ⟦17 = 13 + 3 + 1 = 8 + 5 + 3 + 1⟧.
# Proto se zavádí tzv. «kanonický zápis» čísla ve Fibonacciho soustavě,
# kdy se zakazuje mít vedle sebe dvě jedničky.
#
# Čistá funkce ‹fib_ones› spočítá, kolik jedniček je v kanonickém
# Fibonacciho zápisu nezáporného celého čísla ‹num›.
#
# Příklady:
# V kanonickém Fibonacciho zápisu čísla ⟦17⟧ jsou tři jedničky, viz výše.
# V kanonickém Fibonacciho zápisu čísla ⟦34⟧ je jedna jednička (je to totiž
# přímo Fibonacciho číslo).
# V kanonickém Fibonacciho zápisu čísla ⟦101⟧ jsou čtyři jedničky, protože
# platí ⟦101 = 89 + 8 + 3 + 1⟧.

def fib_ones(num):
    pass


def main() -> None:
    assert fib_ones(1) == 1
    assert fib_ones(3) == 1
    assert fib_ones(17) == 3
    assert fib_ones(34) == 1
    assert fib_ones(101) == 4
    assert fib_ones(2022) == 5
    assert fib_ones(123456789) == 12


if __name__ == '__main__':
    main()
