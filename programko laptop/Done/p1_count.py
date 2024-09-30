from ib111 import week_08  # noqa


# Implementujte čistou funkci ‹count_in_sorted›, která ve vzestupně
# seřazeném seznamu ‹records› co nejefektivněji spočte počet výskytů
# hodnoty ‹value›. K hodnotám v ‹records› přistupujte použitím
# metody ‹get›: např. ‹records.get(7)› vrátí hodnotu na indexu 7.
# Délku seznamu získáte voláním ‹records.size()›.
# Dobré řešení úlohy je logaritmické časové složitosti.


def count_in_sorted(records: 'CountingList', value: int) -> int:
    first = records.get(0)
    lnght = records.size()
    last = records.get(lnght - 1)
    if last < value:
        return 0
    if first == last:
        return records.size()

    higher = lnght
    lower = 0

    pointer = lnght - 1
    num = lnght - 1

    while last != value:
        pointer //= 2
        if pointer == 0:
            pointer += 1
        higher_value = records.get(num)
        one_smaller = records.get(num - 1)

        if higher_value <= value:
            num += pointer
        elif higher_value > value and one_smaller == value:
            higher = num
            break
        else:
            num -= pointer

    pointer = lnght - 1
    num = 0
    while first != value:
        pointer //= 2
        if pointer == 0:
            pointer += 1

        lower_value = records.get(num)
        one_bigger = records.get(num + 1)
        if lower_value >= value:
            num -= pointer
        elif lower_value < value and one_bigger == value:
            lower = num
            break
        else:
            num += pointer

    lnght_value = (higher - 1) - (lower)

    if first == value:
        lnght_value += 1

    return lnght_value


def main() -> None:
    assert count_in_sorted(CountingList([1, 2, 2, 5]), 2) == 2
    assert count_in_sorted(CountingList([1, 2, 2, 5]), 1) == 1
    assert count_in_sorted(CountingList([1, 2, 2, 2, 2]), 2) == 4
    assert count_in_sorted(CountingList([2, 2, 2, 3]), 2) == 3
    assert count_in_sorted(CountingList([1, 2, 2, 5]), 10) == 0
    big_1 = CountingList([x // 3 for x in range(1000)])
    big_2 = CountingList([x // 7 for x in range(1000)])
    assert count_in_sorted(big_1, 180) == 3
    assert big_1.access_count() < 100
    assert count_in_sorted(big_2, 90) == 7
    assert big_2.access_count() < 100
    big_3 = CountingList([1, 1] + [2 for i in range(1000)] + [3, 3])
    assert count_in_sorted(big_3, 2) == 1000
    assert big_3.access_count() < 100


class CountingList:

    def __init__(self, items: list[int]):
        self.__items = items
        self.__count = 0

    def get(self, index: int) -> int:
        self.__count += 1
        return self.__items[index]

    def size(self) -> int:
        return len(self.__items)

    def access_count(self) -> int:
        return self.__count


if __name__ == "__main__":
    main()
