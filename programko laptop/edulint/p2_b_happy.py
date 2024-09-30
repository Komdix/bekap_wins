from ib111 import week_06  # noqa


# Dané přirozené číslo je «b–šťastné» platí-li, že nahradíme-li jej
# součtem druhých mocnin jeho cifer, vyjádřených v poziční soustavě
# se základem ‹b›, a tento postup budeme dále opakovat na takto
# vzniklém čísle, po konečném počtu kroků dostaneme číslo 1.

# Například číslo 3 je 4–šťastné, protože:
#
#  • ⟦3 = (3)₄⟧
#  • ⟦3² = 9 = (21)₄⟧
#  • ⟦2² + 1² = 5 = (11)₄⟧
#  • ⟦1² + 1² = 2 = (2)₄⟧
#  • ⟦2² = 4 = (10)₄⟧
#  • ⟦1² + 0² = 1⟧.
#
# Číslo 2 není 5–šťastné:
#
#  • ⟦2 = (2)₅⟧
#  • ⟦2² = 4 = (4)₅⟧
#  • ⟦4² = 16 = (31)₅⟧
#  • ⟦3² + 1² = 10 = (20)₅⟧
#  • ⟦2² + 0² = 4⟧
#
# a protože se nám ve výpočtu číslo 4 zopakovalo, nemůžeme již dojít
# k výsledku 1.

# Napište predikát, který o číslu ‹number› rozhodne, je-li
# ‹base›-šťastné.


def convert(new_num: int, base: int) -> int:
    summary = 0
    while new_num > 0:
        sum_num = new_num % base
        new_num //= base
        summary += sum_num ** 2
    return summary


def is_b_happy(number: int, base: int) -> bool:
    seen = set()
    summary = convert(number, base)
    while summary != 1:
        seen.add(summary)
        summary = convert(summary, base)
        if summary in seen:
            return False
    return True


def main() -> None:
    assert is_b_happy(3, 4)
    assert is_b_happy(11, 11)
    assert is_b_happy(19, 10)
    assert is_b_happy(347, 6)
    assert is_b_happy(123456, 4)
    assert is_b_happy(7, 10)

    assert not is_b_happy(2, 5)
    assert not is_b_happy(20, 6)
    assert not is_b_happy(100, 5)
    assert not is_b_happy(125, 10)
    assert not is_b_happy(40, 10)
    assert not is_b_happy(8, 6)
    assert not is_b_happy(15, 16)


if __name__ == '__main__':
    main()
