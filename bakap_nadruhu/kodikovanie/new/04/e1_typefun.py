from ib111 import week_04  # noqa
from math import pi, isclose

# Otypujte následující funkce tak, aby prošla typová kontrola
# s přiloženými testy.


# Funkce ‹degrees› konvertuje radiány na stupně.

def degrees(radians):
    return (radians * 180) / pi


# Funkce ‹to_list› rozdělí číslo na číslice o daném základu.

def to_list(num, base):
    digits = []
    result = []

    while num > 0:
        digits.append(num % base)
        num //= base

    for i in range(len(digits)):
        result.append(digits[-i - 1])

    return result


# Funkce ‹diagonal› vytvoří seznam obsahující prvky na diagonále
# matice ‹matrix›.

def diagonal(matrix):
    diag = []
    for i in range(len(matrix)):
        diag.append(matrix[i][i])
    return diag


# Funkci ‹with_id› je v parametru ‹elements› předán seznam dvojic
# (celočíselný klíč, řetězec). Funkce najde prvek s klíčem ‹id_› a
# vrátí odpovídající řetězec.

def with_id(elements, id_):
    for element_id, val in elements:
        if id_ == element_id:
            return val
    return None


# Funkce ‹update_students› v seznamu studentů, zadaných trojicemi
# (učo, jméno a volitelně rok ukončení studia) všem studentům, kteří
# ještě nemají studium ukončené, nastaví rok ukončení studia na
# zadaný.

def update_students(students, end):

    result = []

    for uco, name, graduated in students:
        if graduated is None:
            graduated = end
        result.append((uco, name, graduated))

    return result


# Predikát ‹is_increasing› je pravdivý, pokud je seznam celých čísel
# ‹seq› rostoucí.

def is_increasing(seq):
    for i in range(1, len(seq)):
        if seq[i - 1] >= seq[i]:
            return False
    return True


def main() -> None:
    assert isclose(degrees(pi), 180)
    assert isclose(degrees(pi / 6), 30)

    assert diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 5, 9]

    assert to_list(123, 10) == [1, 2, 3]

    assert with_id([(1, 'a'), (2, 'b'), (3, 'c')], 2) == 'b'

    assert update_students([(123456, "Adam", 2018),
                            (123457, "Eva", None)], 2020) == \
        [(123456, "Adam", 2018),
         (123457, "Eva", 2020)]

    assert is_increasing([1, 2, 3])
    assert not is_increasing([1, 3, 2])


if __name__ == "__main__":
    main()  # mypy-only exercise, this should already pass
