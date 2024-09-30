from ib111 import week_10  # noqa


# Napište predikát, který rozhodne, zda lze dané číslo ‹num› napsat
# jako součet ⟦∑ᵢ₌₁ⁿaᵢ²⟧, kde ⟦n⟧ je zadáno parametrem ‹count› a
# ⟦aᵢ⟧ jsou po dvou různá kladná čísla. Jinými slovy, lze ‹num›
# zapsat jako součet ‹count› druhých mocnin různých kladných čísel?

def custom_int_sqrt(num):
    sqrt = 0
    while (sqrt + 1) ** 2 <= num:
        sqrt += 1
    return sqrt

def find_squares(current_sum, start, depth, num, count):
    if depth == count:
        return current_sum == num

    for i in range(start, custom_int_sqrt(num) + 1):
        if find_squares(current_sum + i ** 2, i + 1, depth + 1, num, count):
            return True

    return False

def is_sum_of_squares(num: int, count: int) -> bool:
    return find_squares(0, 1, 0, num, count)


def main() -> None:
    assert is_sum_of_squares(42, 3)
    assert not is_sum_of_squares(42, 2)
    assert not is_sum_of_squares(18, 2)
    assert not is_sum_of_squares(100, 3)
    assert is_sum_of_squares(100, 5)
    assert not is_sum_of_squares(1000, 13)


if __name__ == '__main__':
    main()
