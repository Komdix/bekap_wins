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
    a = 0
    b = 0
    c = 0
    max_sucet = -1
    sucet = 0
    none = 0
    while c != - 1:
        for i in range(max_side):
            if a != max_side + 1 or b != max_side:
                b = i
                medzi_sucet = a ** 2 + b ** 2
                c = round(medzi_sucet ** 0.5)
                if c ** 2 == a ** 2 + b ** 2:
                    sucet = a + b + c
                    if sucet > max_sucet and (a < max_side and b < max_side):
                        print("kek", a, b, c)
                        max_sucet = sucet
        if a != max_side - 1:
            a += 1
        else:
            print(max_sucet, a , b, c, max_side)
            return max_sucet
    print(none)
    return none


def main():
    # assert largest_triple(10) == 24
    # assert largest_triple(25) == 72
    # assert largest_triple(100) == 288
    # assert largest_triple(150) == 490
    # assert largest_triple(1000) == 3290
    assert largest_triple(8) == 12



if __name__ == "__main__":
    main()
