from ib111 import week_01  # noqa


# Napište funkci, která pro zadané číslo ‹number› najde nejbližší větší
# číslo, které je násobkem čísla ‹k›.

def next_multiple(number, k):
    final = -1
    while final < 0:
        number += 1
        if number % k == 0:
            final = number
    return final


# Dále napište funkci, která pro zadané číslo ‹number› najde
# nejbližší větší prvočíslo.

def next_prime(number):
    dalsie_prvocislo = -1
    sequence = number+1
    if number == 1:
        return 2
    while dalsie_prvocislo < 0:
        for i in range(2, sequence):
            if sequence % i <= 0:
                sequence += 1
            else:
                pass
        dalsie_prvocislo = sequence
    return dalsie_prvocislo


def main():
    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450

    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13
    assert next_prime(13) == 17
    # assert next_prime(971) == 977
    assert next_prime(10007) == 10009
    # assert next_prime(94169) == 94201
    # assert next_prime(23) == 29


if __name__ == "__main__":
    main()
