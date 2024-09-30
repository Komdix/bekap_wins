from ib111 import week_01  # noqa


# Napište funkci ‹largest_triple›, která najde pythagorejskou
# trojici ⟦(a, b, c)⟧ – totiž takovou, že ⟦a⟧, ⟦b⟧ a ⟦c⟧ jsou
# přirozená čísla a platí ⟦a² + b² = c²⟧ (tzn. tvoří pravoúhlý
# trojúhelník). Hledáme trojici, která:
#
#  1. má největší možný součet ⟦a + b + c⟧,
#  2. hodnoty ⟦a⟧, ⟦b⟧ jsou menší než ‹max_side›.
#
# Výsledkem funkce bude součet ⟦a + b + c⟧, tedy největší možný
# obvod pravoúhlého trojúhelníku, jsou-li obě jeho odvěsny kratší
# než ‹max_side›.

def largest_triple(max_side):
    summary = 0
    right_angled = 0
    for a in range(max_side - 1, 0, -1):
        for b in range(a, 0, -1):
            c = a ** 2 + b ** 2
            if (a + b + c ** 0.5) < right_angled:
                break
            c_kek = round(c ** 0.5)
            if a ** 2 + b ** 2 == c_kek ** 2:
                actual = a + b + c_kek
                right_angled = actual
                if summary < actual:
                    summary = actual
    return summary


def main():
    assert largest_triple(10) == 24
    assert largest_triple(25) == 72
    assert largest_triple(100) == 288
    assert largest_triple(150) == 490
    assert largest_triple(1000) == 3290


if __name__ == "__main__":
    main()
