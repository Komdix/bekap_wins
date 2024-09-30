from ib111 import week_02  # noqa


# Elfové používají k zápisu čísel jedenáctkovou soustavu, přičemž
# kromě nám známých číslic ⟦0, 1, 2, 3, 4, 5, 6, 7, 8, 9⟧ používají
# ještě číslici ⟦δ⟧ reprezentující číslo deset.
#
# O kladném celém čísle řekneme, že je elfím palindromem, pokud se
# jeho elfí (jedenáctkový) zápis čte stejně zleva i zprava poté, co
# «vynecháme» všechny číslice ⟦δ⟧ a následně odstraníme zbytečné
# levostranné nuly. (Za elfí palindromy považujeme i čísla, jejichž
# elfí zápis je tvořen pouze číslicemi ⟦δ⟧.)
#
# Napište predikát ‹elf_palindrome(num)›, který vrátí ‹True›, je-li
# zadané číslo elfím palindromem; ‹False› jinak.
#
# Například číslo ⟦144⟧ je elfím palindromem, protože jeho elfí
# zápis je ⟦(121)ₑ⟧. Elfími palindromy jsou také čísla ⟦2564 =
# (1δ21)ₑ⟧, ⟦1211 = (δ01)ₑ⟧ a ⟦33670 = (2332δ)ₑ⟧.
# Elfími palindromy «nejsou» čísla ⟦233 = (1δ2)ₑ⟧, ⟦1729 = (1332)ₑ⟧.

def elf_palindrome(num):
    pass


def main() -> None:
    assert elf_palindrome(120)
    assert elf_palindrome(144)
    assert elf_palindrome(2564)
    assert elf_palindrome(1211)
    assert not elf_palindrome(233)
    assert not elf_palindrome(1729)


if __name__ == '__main__':
    main()
