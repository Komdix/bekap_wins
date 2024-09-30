from ib111 import week_01  # noqa


# Uvažujme posloupnost ⟦aᵢ⟧ druhých mocnin kladných sudých čísel ⟦aᵢ = 4i²⟧.
# Napište funkci, která vrátí sumu prvních ‹n› členů této posloupnosti
# ⟦sₙ = ∑ᵢ₌₁ⁿ aᵢ = ∑ᵢ₌₁ⁿ 4i²⟧.

def even(n):
    pass


def main():
    assert even(1) == 4
    assert even(2) == 20
    assert even(3) == 56
    assert even(4) == 120
    assert even(10) == 1540
    assert even(134) == 3244140


if __name__ == "__main__":
    main()
