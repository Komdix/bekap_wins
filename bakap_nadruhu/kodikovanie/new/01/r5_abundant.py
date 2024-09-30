from ib111 import week_01  # noqa


# † Napište predikát ‹is_abundant›, který je pravdivý, pokud je
# číslo ‹number› abundantní, t.j. je menší, než součet jeho
# vlastních dělitelů.
#
# Za vlastní dělitele čísla považujeme všechny jeho kladné
# dělitele s výjimkou čísla samotného; např. vlastní dělitelé
# čísla 12 jsou 1, 2, 3, 4, 6.

def is_abundant(number):
    pass


def main():
    assert is_abundant(12)
    assert is_abundant(18)
    assert is_abundant(20)
    assert is_abundant(24)
    assert is_abundant(36)
    assert is_abundant(100)
    assert is_abundant(120)

    assert not is_abundant(7)
    assert not is_abundant(15)
    assert not is_abundant(55)
    assert not is_abundant(62)
    assert not is_abundant(130)


if __name__ == "__main__":
    main()
