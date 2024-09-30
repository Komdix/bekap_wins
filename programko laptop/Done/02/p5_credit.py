from ib111 import week_02  # noqa


# Napište predikát, který ověří, zda je číslo korektní číslo
# platební karty.  Číslo platební karty ověříte podle Luhnova
# algoritmu:
#
#  1. zdvojnásobte hodnotu každé druhé cifry zprava; je-li výsledek
#     větší než 9, odečtěte od něj hodnotu 9,
#  2. sečtěte všechna takto získaná čísla a cifry na lichých
#     pozicích (kromě první cifry zprava, která slouží jako
#     kontrolní součet),
#  3. číslo karty je platné právě tehdy, je-li po přičtení kontrolní
#     cifry celkový součet dělitelný 10.
#
# Například pro číslo 28316 je kontrolní cifra 6 a součet je: ⟦2 +
# (2⋅8 - 9) + 3 + 2⋅1 = 2 + 7 + 3 + 2 = 14⟧. Po přičtení kontrolní
# cifry je celkový součet ⟦20⟧. Protože je beze zbytku dělitelný
# deseti, číslo karty je platné.


def get_digit(number, k):
    return (number // 10 ** k) % 10


def is_valid_card(number):
    num = 0
    pocet = 0
    sucet = 0
    n = number
    while n > 0:
        pocet += 1
        n //= 10
    for i in range(1, pocet, 2):
        num = get_digit(number, i) * 2
        if num > 9:
            num -= 9
        else:
            pass
        sucet += num
    for i in range(2, pocet, 2):
        num = get_digit(number, i)
        sucet += num
    control = get_digit(number, 0)
    final = sucet + control
    return final % 10 == 0


def main():
    assert is_valid_card(28316)
    assert is_valid_card(4556737586899855)
    assert is_valid_card(4929599116478604)
    assert is_valid_card(4929300836739668)
    assert not is_valid_card(4929300835539668)
    assert not is_valid_card(4929300836739328)
    assert not is_valid_card(5101180000000000007)

    assert is_valid_card(5294967072531977)
    assert is_valid_card(5354598557505686)
    assert is_valid_card(2720993849498580)


if __name__ == "__main__":
    main()
