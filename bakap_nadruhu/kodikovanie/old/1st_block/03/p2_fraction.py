from ib111 import week_03  # noqa


# Stejně jako v ‹02/fraction.py› budete v této úloze pracovat s řetězovým
# zlomkem. Tentokrát implementujeme převod opačným směrem, na vstupu bude
# seznam koeficientů řetězového zlomku, a výstupem bude zlomek klasický.
#
# Naprogramujte tedy čistou funkci ‹continued_fraction›, ktorá dostane jako
# parametr seznam koeficientů a vrátí zlomek ve tvaru ‹(numerator,
# denominator)›.


# i dont know how to name those variables to make it more readable (yeah i know its unreadable, and probably have much better way to do)


def continued_fraction(coefficients):
    nums = coefficients
    x = 1
    length = - len(nums)
    for i in range(-1, length,-1):
        if i == -1:
            first_denom = nums[i]
        fisrt_num = nums[i-1]
        temp_result = [x,first_denom]
        calculated = [fisrt_num * first_denom ,first_denom]
        flip = [first_denom, temp_result[0] + calculated[0]]
        x = flip[0]
        first_denom = flip[1]
        temp_result = [x,first_denom]
        final = (temp_result[1],temp_result[0])
    return final


def main():
    assert continued_fraction([4, 2, 6, 7]) == (415, 93)
    assert continued_fraction([3, 4, 12, 4]) == (649, 200)
    assert continued_fraction([0, 2, 4]) == (4, 9)


if __name__ == "__main__":
    main()
