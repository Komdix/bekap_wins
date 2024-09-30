from ib111 import week_01  # noqa


# Napište funkci, která spočítá sumu prvních ‹n› «sudých» členů
# Fibonacciho posloupnosti (tj. členů, které jsou sudé, nikoliv
# těch, které mají sudé indexy). Například volání ‹fibsum(3) = 44 =
# 2 + 8 + 34›.


def fibsum(n):
    a = 0
    b = 1
    c = a + b
    sucet = 0
    step = 0
    pokus = 0
    while n > step:
        pokus += 1
        if c % 2 == 0:
            sucet += c
            step += 1
            a = b
            b = c
            c = a + b

        elif c % 2 == 1:
            a = b
            b = c
            c = a + b

    return sucet


def main():
    assert fibsum(0) == 0
    assert fibsum(1) == 2
    assert fibsum(2) == 10

    assert fibsum(3) == 44
    assert fibsum(4) == 188
    assert fibsum(5) == 798
    assert fibsum(10) == 1089154


if __name__ == "__main__":
    main()
