from ib111 import week_01  # noqa
from math import sqrt


# Napište čistou funkci ‹nth_smallest_prime_divisor›, která vrátí ‹index›-té
# nejmenší prvočíslo vyskytující se v prvočíselném rozkladu čísla ‹num›.
# Pokud se v rozkladu vyskytuje některé prvočíslo vícekrát, počítáme všechny
# jeho výskyty, tedy např. v čísle ⟦2 · 2 · 3 · 3 · 3 · 5 = 540⟧ je třetím
# nejmenším prvočíslem číslo 3. Pokud má ‹num› méně než ‹index› prvočísel
# v rozkladu, funkce vrátí ‹None›.
#
# Předpokládejte, že ‹num› i ‹index› jsou kladná celá čísla.
# Zde indexujeme od 1, tedy první prvočíslo v rozkladu má ‹index› 1.
#
# Je potřeba, aby vaše funkce fungovala rozumně rychle i pro velmi velká
# čísla, u nichž je hledané prvočíslo malé. (Není třeba vymýšlet zvláště
# chytrá řešení, jen je třeba nedělat zbytečnou práci navíc.)

def nth_smallest_prime_divisor(num, index):

    count = 0
    div = 2

    for _ in range(num):

        if num % div == 0:
            num //= div
            result = div
            count += 1
            div = 1

        div += 1

        if count >= index:
            return result
    return None

# t = nth_smallest_prime_divisor(1,1)
# print(t)

def main():
    assert nth_smallest_prime_divisor(20, 1) == 2
    assert nth_smallest_prime_divisor(42350, 2) == 5
    assert nth_smallest_prime_divisor(42350, 3) == 5
    assert nth_smallest_prime_divisor(42350, 4) == 7
    assert nth_smallest_prime_divisor(42350, 7) is None


if __name__ == '__main__':
    main()
