from ib111 import week_08  # noqa


# Implementujte čistou funkci ‹frequency_sort›, která podle
# frekvencí výskytu seřadí hodnoty v seznamu ‹values›. Hodnoty se
# stejnou frekvencí výskytu nechť jsou seřazeny vzestupně podle
# hodnoty samotné. Výsledný seznam bude obsahovat každou hodnotu
# právě jednou.

def frequency_sort(values: list[int]) -> list[int]:
    unique = []
    frequencies = []
    for element in values:
        if element not in unique:
            unique.append(element)
            frequencies.append(1)
        else:
            index = unique.index(element)
            frequencies[index] += 1

    for i in range(1, len(frequencies)):
        current_val = unique[i]
        current_freq = frequencies[i]
        j = i - 1
        while j > -1 and (frequencies[j] < current_freq or
                          (frequencies[j] == current_freq
                           and unique[j] > current_val)):

            frequencies[j + 1] = frequencies[j]
            unique[j + 1] = unique[j]
            j -= 1

        frequencies[j + 1] = current_freq
        unique[j + 1] = current_val

    return unique


def main() -> None:
    # assert frequency_sort([]) == []
    # assert frequency_sort([1]) == [1]
    assert frequency_sort([1, 3, 2, 4]) == [1, 2, 3, 4]
    # assert frequency_sort([5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]) == [5, 6, 3, 2]
    # assert frequency_sort([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5,
    #                        5, 4, 4, 4, 4, 4, 4]) == [4, 3, 2, 5, 1]
    # records = [1, 2, 2, 2, 3, 3]
    # assert frequency_sort(records) == [2, 3, 1]
    # assert records == [1, 2, 2, 2, 3, 3]


if __name__ == "__main__":
    main()
