from ib111 import week_08  # noqa


# Implementujte čistou funkci ‹frequency_sort›, která podle
# frekvencí výskytu seřadí hodnoty v seznamu ‹values›. Hodnoty se
# stejnou frekvencí výskytu nechť jsou seřazeny vzestupně podle
# hodnoty samotné. Výsledný seznam bude obsahovat každou hodnotu
# právě jednou.
def insert_sort(lst_sort_max: list[int]) -> list[int]:
    lnght = len(lst_sort_max) - 1
    for i in range(1, lnght):
        current = lst_sort_max[i]
        j = i
        while j < lnght and lst_sort_max[j + 1] < current:
            lst_sort_max[j] = lst_sort_max[j - 1]
            j += 1
            lst_sort_max[j] = current
    return lst_sort_max


def frequency_sort(values: list[int]) -> list[int]:
    count: dict[int, int] = {}
    # lst = list(count)
    print(values)
    for element in values:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
    print(count)
    # lst_sorted = insert_sort()
    lst_sort_max = []
    while count != {}:
        lst_max = list(count.values())  
        lst_keys = list(count.keys())
        lst_sort_max.append(lst_keys[max(lst_max)])
        for i in range(lst_max.count(max(lst_max))):
            print(i)  

    # lst_sorted_freq = []
    # while lst_sorted != []:
    #     lst_sorted_freq.append(lst_sorted[-1])
    #     lst_sorted.pop()

    # print(lst_sorted)
    # for _ in range(len(lst)):

        





    # for element in values:
    #     if element not in lst:
    #         lst.append(element)
    # for element in lst:
    #     values.count(element)



def main() -> None:
    # assert frequency_sort([]) == []
    # assert frequency_sort([1]) == [1]
    assert frequency_sort([1, 3, 2, 4]) == [1, 2, 3, 4]
    assert frequency_sort([5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]) == [5, 6, 3, 2]
    assert frequency_sort([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5,
                           5, 4, 4, 4, 4, 4, 4]) == [4, 3, 2, 5, 1]
    records = [1, 2, 2, 2, 3, 3]
    assert frequency_sort(records) == [2, 3, 1]
    assert records == [1, 2, 2, 2, 3, 3]


if __name__ == "__main__":
    main()
