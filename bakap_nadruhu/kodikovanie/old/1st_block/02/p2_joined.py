from ib111 import week_02  # noqa


# Napište funkci, která vytvoří číslo zřetězením ‹count› po sobě
# jdoucích kladných čísel počínaje zadaným číslem ‹start›.  Tato
# čísla zřetězte vyjádřená v binární soustavě. Například volání
# ‹joined(1, 3)› zřetězí sekvenci ⟦(1)₂ = 1⟧, ⟦(10)₂ = 2⟧, ⟦(11)₂ = 3⟧
# a vrátí číslo ⟦(11011)₂ = 27⟧. V Pythonu lze binární čísla přímo
# zapisovat v tomto tvaru: ‹0b11011› (podobně lze stejné číslo
# zapsat v šestnáctkové soustavě zápisem ‹0x1b› nebo osmičkové jako
# ‹0o33›).


def get_digit(number, k):
    return (number // 10 ** k) % 10


# count all digits in the binary code of the sum
def get_count(start, count):
    counter = -1
    for i in range(0, count):
        n = start + i
        while n > 0:
            n //= 2
            counter += 1
    return counter


def joined(start, count):
    order_of_digit = get_count(start, count)
    n = 0
    Binary_form = 0
    final = 0
    for i in range(0, count):
        n = start + i
        Binary_form = 0
        rest = start + i
        count_1 = 0
        while n > 0:
            n //= 2
            count_1 += 1
        n = start + i
        for j in range(count_1):
            rest = n % 2
            n //= 2
            Binary_form += rest * (10 ** j)
        for j in range(count_1, 0, -1):
            dig = get_digit(Binary_form, j-1)
            if dig == 1:
                final += 2 ** order_of_digit
            order_of_digit -= 1
    return final


def main() -> None:
    assert joined(1, 3) == 0b11011
    assert joined(10, 4) == 0b1010101111001101
    assert joined(8, 5) == 0b10001001101010111100
    assert joined(99, 2) == 0b11000111100100
    assert joined(999, 3) == 0b111110011111111010001111101001
    assert joined(1111, 1) == 0b10001010111


if __name__ == "__main__":
    main()
