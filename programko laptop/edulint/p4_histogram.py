from ib111 import week_06  # noqa


# Napište (čistou) funkci, která na vstupu dostane signál ‹data›
# reprezentovaný seznamem celočíselných amplitud (vzorků).
# Výsledkem bude statistika tohoto signálu, kterou vytvoří
# následujícím způsobem:

#  1. funkce signál nejdříve očistí od všech vzorků s amplitudou
#     větší než ‹max_amplitude› a menších než ‹min_amplitude›,
#  2. následně jej převzorkuje tak, že sloučí každých ‹bucket›
#     vzorků (poslední vzorek může být nekompletní) do jednoho
#     vypočtením jejich průměru a jeho následným zaokrouhlením
#     (pomocí vestavěné funkce ‹round›),
#  3. nakonec spočítá, kolikrát se v upraveném signálu objevují
#     jednotlivé amplitudy, a vrátí slovník, kde klíč bude amplituda
#     a hodnota bude počet jejích výskytů.


def filter(data: list[int], max_amplitude: int,
           min_amplitude: int) -> list[int]:
    copy_of_data = data.copy()
    for item in data:
        if item < min_amplitude or item > max_amplitude:
            copy_of_data.pop(copy_of_data.index(item))
    return copy_of_data


def packets(data: list[int], start: int, end: int) -> list[int]:
    lst: list[int] = []
    packet: float = 0.0
    for i in range(start, end):
        packet += data[i]
    packet /= end - start
    lst.append(round(packet))
    return lst


def count(lst_data: list[int]) -> dict[int, int]:
    seen: dict[int, int] = {}
    for element in lst_data:
        if element in seen:
            seen[element] += 1
        else:
            seen[element] = 1
    return seen


def histogram(data: list[int], max_amplitude: int,
              min_amplitude: int, bucket: int) -> dict[int, int]:
    data_filtered = filter(data, max_amplitude, min_amplitude)
    if data_filtered == [] or data == []:
        return {}
    steps = len(data_filtered) // bucket
    remaining = (len(data_filtered) % bucket) + 1
    lst = []
    for i in range(steps):
        start = i * bucket
        lst.extend(packets(data_filtered, start, start + bucket))
    last = 0.0
    if remaining != 1:
        for i in range(-1, - remaining, -1):
            last += data_filtered[i]
        last /= remaining - 1
        lst.append(round(last))
    result = count(lst)
    return result


def main() -> None:
    data = [1, 1, 1]
    assert histogram(data, 5, 0, 1) == {1: 3}
    assert data == [1, 1, 1]

    assert histogram([1, 1, 1, 1], 5, 0, 2) == {1: 2}
    assert histogram([1, 2, 3, 4, 5], 5, 2, 2) == {2: 1, 4: 1}
    assert histogram([1, 2, 9, 2, 10, 1, 1, 1, 1], 8, 1, 3) == {2: 1, 1: 2}

    data = []
    assert histogram([], 1, 2, 5) == {}
    assert data == []

    assert histogram([1, 1, 1, 8, 8, 8], 5, 3, 10) == {}
    assert histogram([1, 2, 3, 4], 2, 5, 3) == {}
    assert histogram([1, 2, 3, 4, 5], 10, 1, 7) == {3: 1}
    assert histogram([0], 0, 1, 1) == []


if __name__ == '__main__':
    main()
