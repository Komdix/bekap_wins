from ib111 import week_10  # noqa


# Napište čistou funkci, která najde libovolnou podmnožinu zadané množiny
# kladných celých čísel ‹nums›, součet jejíchž prvků je přesně
# ‹total›. Pokud taková podmnožina neexistuje, funkce vrátí ‹None›.
#
# Při řešení přemýšlejte, jestli některé výpočty neprovádíte opakovaně
# a jak byste se tomu mohli vyhnout.


def subset_sum(nums: set[int], total: int) -> set[int] | None:
    pass


def main() -> None:
    assert subset_sum(set(), 5) is None

    nums = {1, 2, 3}
    assert subset_sum(nums, 7) is None
    assert nums == {1, 2, 3}

    assert subset_sum({1}, 1) == {1}
    assert subset_sum({1, 2, 3}, 5) == {2, 3}

    nums = {5, 10, 12, 13}
    assert subset_sum(nums, 27) == {5, 10, 12}
    assert nums == {5, 10, 12, 13}

    assert subset_sum({2022, 2021, 2020, 2019, 2018}, 5050) is None
    assert subset_sum({2, 3, 4, 804, 390, 11, 597, 598}, 1204) \
        == {2, 3, 4, 597, 598}


if __name__ == '__main__':
    main()
