from ib111 import week_03  # noqa


# Naprogramujte (čistou) funkci, která ze dvou vzestupně seřazených
# seznamů čísel ‹a›, ‹b› vytvoří nový vzestupně seřazený seznam,
# který bude obsahovat všechny prvky z ‹a› i ‹b›. Nezapomeňte, že
# nesmíte modifikovat vstupní seznamy (jinak by funkce nebyla
# čistá). Pokuste se funkci naprogramovat «efektivně».

def bubblesort(merged):
    for i in range(len(merged)):
        for j in range(0, len(merged) - i - 1):
            if merged[j] > merged[j + 1]:
                swap = merged[j]
                merged[j] = merged[j + 1]
                merged[j + 1] = swap
    return merged


def merge(a, b):
    if a == [] and b == []:
        return []
    merged = []
    for element in a:
        merged.append(element)
    for element in b:
        merged.append(element)
    if a == [] or b == []:
        return merged
    merged = bubblesort(merged)
    return merged


def main():
    assert merge([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert merge([0, 2, 4, 6, 8], [1, 3, 5, 7, 9]) \
        == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge([], []) == []
    assert merge([], [1, 2]) == [1, 2]
    assert merge([1, 2], []) == [1, 2]
    assert merge([1, 5, 10], [-1, 2, 3, 4, 6, 10, 11]) \
        == [-1, 1, 2, 3, 4, 5, 6, 10, 10, 11]


if __name__ == "__main__":
    main()
