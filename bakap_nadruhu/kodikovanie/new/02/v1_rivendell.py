from ib111 import week_02  # noqa


# Elfové z Groglinky používají k zápisu čísel jedenáctkovou
# soustavu, přičemž kromě nám známých číslic ⟦0, 1, 2, 3, 4, 5, 6,
# 7, 8, 9⟧ používají ještě číslici ⟦δ⟧ reprezentující hodnotu minus
# jedna. (Tím se liší od ostatních elfů, kteří touto číslicí
# reprezentují hodnotu deset). Napište čistou funkci
# ‹elf_digit_sum(num)›, která dostane na vstupu kladné celé číslo
# a vrátí součet hodnot jeho číslic v zápise elfů z Groglinky.
#
# Například:
#  • elfí ciferný součet ⟦1729 = (1332)ₑ⟧ je ⟦1 + 3 + 3 + 2 = 9⟧,
#  • podobně ⟦1234 = (1δ22)ₑ⟧ má součet ⟦1 - 1 + 2 + 2 = 4⟧,
#  • a ⟦999987 = (62334δ)ₑ⟧ má součet ⟦6 + 2 + 3 + 3 + 4 - 1 = 17⟧.

def elf_digit_sum(num):
    pass


def main() -> None:
    assert elf_digit_sum(10) == 0
    assert elf_digit_sum(1729) == 9
    assert elf_digit_sum(1234) == 4
    assert elf_digit_sum(999987) == 17
    assert elf_digit_sum(305997) == -3


if __name__ == '__main__':
    main()
