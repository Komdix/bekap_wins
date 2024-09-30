from ib111 import week_01  # noqa


# Napište funkci, která pro zadané celé číslo ‹number›
# najde nejbližší větší číslo, které je násobke kladného
# celého čísla ‹k›.

def next_multiple(number, k):
    final = -1
    while final < 0:
        number += 1
        if number % k == 0:
            final = number
    return final


# Dále napište funkci, která pro zadané kladné celé číslo
# ‹number› najde nejbližší větší prvočíslo.

def next_prime(number):
    next_num = number + 1
    i = next_num
    if number == 0:
        return 1
    while i > 0:
        i -= 1
        if next_num % i == 0 and (next_num != i and i != 1):
            next_num += 1
            i = round(next_num ** 0.5)
        elif next_num % i == 0:
            return next_num

    return next_num


def main():

    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450

    assert next_prime(0) == 1
    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13
    assert next_prime(13) == 17
    assert next_prime(1051) == 1061


if __name__ == "__main__":
    main()
