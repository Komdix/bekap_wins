from ib111 import week_10  # noqa


# Napište čistou funkci, která ze vstupního seznamu vytvoří seznam
# všech jeho permutací (tedy seznamů takových, že jsou tvořena
# stejnými hodnotami v libovolném pořadí). Výsledný seznam permutací
# nechť je uspořádán lexikograficky.

# Nápověda: řešení se znatelně zjednoduší, budete-li celou dobu
# pracovat se seřazenou verzí vstupního seznamu (seřazení je nakonec
# také jen permutace). Dobré řešení pak vytvoří každou permutaci
# pouze jednou a také je vytvoří rovnou ve správném pořadí.


def permutations(word: list[int]) -> list[list[int]]:
    if len(word) <= 1:
        return [word]

    lst = word.copy()
    lst.sort()
    result = []

    for i in range(len(lst)):
        if i > 0 and lst[i] == lst[i - 1]:
            continue
        remains = []

        for j in range(len(lst)):
            if j != i:
                remains.append(lst[j])

        for permutation in permutations(remains):
            result.append([lst[i]] + permutation)

    return result


def main() -> None:
    assert permutations([]) == [[]]
    assert permutations([1, 1]) == [[1, 1]]
    assert permutations([1, 2]) == [[1, 2], [2, 1]]
    assert permutations([3, 1, 2]) == [[1, 2, 3],
                                       [1, 3, 2],
                                       [2, 1, 3],
                                       [2, 3, 1],
                                       [3, 1, 2],
                                       [3, 2, 1]]


if __name__ == '__main__':
    main()
