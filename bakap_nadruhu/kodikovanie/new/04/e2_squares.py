from ib111 import week_04  # noqa
from math import isclose


# Otypujte následující funkce tak, aby prošla typová kontrola
# s přiloženými testy.


def slope(x, y, average_x, average_y):
    dividend = 0
    divisor = 0

    for i in range(len(x)):
        dividend += ((x[i] - average_x) * (y[i] - average_y))
        divisor += (x[i] - average_x) ** 2

    if divisor == 0:
        return None

    return dividend / divisor


def deviations(x, y, alpha, beta):
    res = []
    for i in range(len(x)):
        res.append(abs(y[i] - beta * x[i] - alpha))
    return res


def least_squares(x, y):
    average_x = float(sum(x)) / len(x)
    average_y = float(sum(y)) / len(y)

    beta = slope(x, y, average_x, average_y)
    if beta is None:
        return None

    alpha = average_y - beta * average_x

    return (alpha, beta, deviations(x, y, alpha, beta))


def main() -> None:
    assert check([1, 2], [3, 4], (2, 1, [0, 0]))
    assert check([1, 2, 3], [3, 4, 5], (2, 1, [0, 0, 0]))
    assert least_squares([1, 1, 1], [3, 4, 5]) is None
    assert check([1, 2, 3], [2, 2, 2], (2, 0, [0, 0, 0]))
    assert check([1, 2, 3], [1, 4, 1], (2, 0, [1, 2, 1]))
    assert check([1, 2, 3], [1, 2, 4],
                 (-2.0 / 3.0, 3.0 / 2.0,
                  [1.0 / 6.0, 1.0 / 3.0, 1.0 / 6.0]))


def check(x: list[float], y: list[float],
          expect: tuple[float, float, list[float]]) -> bool:
    result = least_squares(x, y)
    if result is None:
        return False
    (alpha1, beta1, r1) = result
    (alpha2, beta2, r2) = expect
    if not isclose(alpha1, alpha2) or not isclose(beta1, beta2):
        return False
    for i in range(len(r1)):
        if not isclose(r1[i], r2[i]):
            return False
    return True


if __name__ == "__main__":
    main()  # mypy-only exercise, this should already pass
