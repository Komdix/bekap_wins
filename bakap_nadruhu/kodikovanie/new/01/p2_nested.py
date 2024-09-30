from ib111 import week_01  # noqa


# Napište funkci ‹nested›, která spočítá ‹n›-tý člen posloupnosti
# (počítáno od 0), která vznikne napojením postupně se
# prodlužujících prefixů přirozených čísel.
#
# Nechť ⟦Aᵢ⟧ je posloupnost čísel ⟦1⟧ až ⟦i⟧:
#
#  ⟦ A₁ → 1
#    A₂ → 1, 2
#    A₃ → 1, 2, 3
#    A₄ → 1, 2, 3, 4
#    A₅ → 1, 2, 3, 4, 5 ⟧
#
# Hledaná posloupnost ⟦B⟧ vznikne napojením posloupností ⟦A₁⟧, ⟦A₂⟧,
# ⟦A₃⟧ … (do nekonečna) za sebe:
#
#  ⟦ B  → 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, … ⟧
#
# Vaším úkolem je najít ‹n›-tý prvek posloupnosti ⟦B⟧.


def nested(n):
    count = 0
    sequence = 1
    while count < n:
        if (count + sequence) > n:
            return n - count + 1
        count += sequence
        sequence += 1
    return 1


# Dále napište funkci ‹nested_sum›, která spočítá sumu prvních ‹n› členů
# této posloupnosti.


def nested_sum(n):
    count = 0
    result = 0
    previous_sum = 0
    mid_res = 0
    sequence = 1
    while count < n:
        if (count + sequence) > n:
            result += ((n - count) * (1 + n - count)) // 2
            return result
        mid_res += previous_sum + sequence
        result += mid_res
        count += sequence
        sequence += 1
    return None


def main():
    assert nested(0) == 1
    assert nested(1) == 1
    assert nested(2) == 2
    assert nested(8) == 3
    assert nested(9) == 4
    assert nested(25) == 5
    assert nested(130) == 11

    assert nested_sum(2) == 2
    assert nested_sum(5) == 7
    assert nested_sum(13) == 26
    assert nested_sum(30) == 87
    assert nested_sum(100) == 500


if __name__ == "__main__":
    main()
