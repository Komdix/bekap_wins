from ib111 import week_02  # noqa


# Kladné celé číslo se nazývá ⟦k⟧-parazitní v soustavě o základu ⟦b⟧ (kde
# ⟦b⟧ je celé číslo vetší než 1 a ⟦k⟧ je celé číslo v rozsahu 1 až ⟦b - 1⟧),
# pokud jeho ⟦k⟧-násobek vznikne tak, že jeho poslední (nejpravější) číslici
# v zápisu v soustavě o základu ⟦b⟧ přesuneme na první pozici. Například
# číslo ⟦179487⟧ je 4-parazitní v desítkové soustavě, protože platí
# ⟦179487 · 4 = 717948⟧; číslo ⟦32⟧ je 2-parazitní v trojkové soustavě,
# protože ⟦32 = (1012)₃⟧, ⟦32 · 2 = 64⟧ a ⟦64 = (2101)₃⟧.
#
# Napište čistou funkci ‹is_parasitic›, která zjistí, zda je zadané číslo
# ‹num› ⟦k⟧-parazitní v soustavě o základu ‹base› pro nějaké ⟦k⟧ – pokud ano,
# takové ⟦k⟧ vrátí; jinak vrátí ‹None›.


def is_parasitic(num, base):
    pass


def main() -> None:
    assert is_parasitic(1, 10) == 1
    assert is_parasitic(8, 7) == 1
    assert is_parasitic(63245, 42) == 1
    assert is_parasitic(179487, 10) == 4
    assert is_parasitic(12345, 10) is None
    assert is_parasitic(105263157894736842, 10) == 2
    assert is_parasitic(142857, 10) == 5
    assert is_parasitic(26144, 7) == 4
    assert is_parasitic(26144, 8) is None
    assert is_parasitic(314314, 12) == 8
    assert is_parasitic(83886, 16) == 11
    assert is_parasitic(
        1016949152542372881355932203389830508474576271186440677966, 10) == 6


if __name__ == "__main__":
    main()
