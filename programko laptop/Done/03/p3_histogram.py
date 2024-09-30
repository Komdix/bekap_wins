from ib111 import week_03  # noqa


# Napište (čistou) funkci, která pro zadaný seznam nezáporných čísel
# ‹data› vrátí nový seznam obsahující dvojice – číslo a jeho
# četnost. Výstupní seznam musí být seřazený vzestupně dle první
# složky. Můžete předpokládat, že v ‹data› se nachází pouze celá
# čísla z rozsahu [0, 100] (včetně).


def histogram(data):
    nums = data
    if data == []:
        return []
    result = []
    for i in range(101):
        a = 0
        for element in nums:
            if element == i:
                a += 1
        add = (i, a)
        if a >= 1:
            result.append(add)
    return result


def main() -> None:
    assert histogram([1, 2, 3, 2, 1]) == [(1, 2), (2, 2), (3, 1)]
    assert histogram([7, 1, 7, 1, 5]) == [(1, 2), (5, 1), (7, 2)]
    assert histogram([1, 1, 1]) == [(1, 3)]
    assert histogram([]) == []


if __name__ == "__main__":
    main()
