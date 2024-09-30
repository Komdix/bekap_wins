from ib111 import week_03  # noqa


# † Naprogramujte proceduru ‹partition›, která na vstup dostane
# seznam čísel ‹data› a platný index ‹idx›. Pro pohodlnost hodnotu
# ‹data[idx]› nazveme ‹pivot›.
#
# Procedura přeuspořádá seznam tak, že přesune prvky menší než
# ‹pivot› před ‹pivot› a prvky větší než ‹pivot› za ‹pivot›.
#
# Po transformaci bude tedy seznam «pomyslně» rozdělen na tři části:
#
#   • čísla menší než ‹pivot›
#   • pivot
#   • čísla větší než ‹pivot›
#
# Relativní pořadí prvků v první a poslední části není definováno,
# takže oba následovné výsledky pro seznam ‹[3, 4, 1, 2, 0]› a index
# ‹0› jsou správné: ‹[1, 0, 2, 3, 4]› nebo ‹[1, 2, 0, 3, 4]›.

def partition(data, idx):
    pass


def main():
    run_test([3, 4, 6, 2, 5], 4)
    run_test([0, 1, 3, 4, 6, 2, 5], 4)
    run_test([0, 1, 3, 4, 6, 2, 5], 2)
    run_test([0, 2, 1, 5, 6, 9], 0)
    run_test([0, 2, 1, 5, 6, 9], 3)
    run_test([6, 9, 3, 0, 1], 2)


def run_test(data, idx):
    pivot = data[idx]
    count = len(data)
    sum_ = sum(data)

    partition(data, idx)

    assert len(data) == count
    assert sum(data) == sum_

    i = 0

    while i < count and data[i] < pivot:
        i += 1
    while i < count and data[i] == pivot:
        i += 1
    while i < count and data[i] > pivot:
        i += 1

    assert i == count


if __name__ == "__main__":
    main()
