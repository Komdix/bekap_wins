from ib111 import week_01  # noqa


# Napište čistou funkci ‹nth_element_lv› která vrátí ‹index›-tý
# prvek posloupnosti, která vzniká takto:
#
#  ⟦ x₀ = 2
#    x₁ = p
#    xₙ = pxₙ₋₁ - qxₙ₋₂ ⟧
#
# Parametry ‹p›, ‹q› mohou být libovolná celá čísla, parametr
# ‹index› libovolné nezáporné celé číslo (v tomto příkladu
# indexujeme posloupnost od nuly).

def nth_element_lv(p, q, index):
    pass


def main():
    assert nth_element_lv(7, 9, 0) == 2
    assert nth_element_lv(5, 4, 1) == 5
    assert nth_element_lv(1, -1, 5) == 11
    assert nth_element_lv(3, 2, 7) == 129


if __name__ == '__main__':
    main()
