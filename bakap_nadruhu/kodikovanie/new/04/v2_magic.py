from ib111 import week_04  # noqa

# Magický čtverec je dvourozměrná matice vzájemně různých kladných celých
# čísel, pro niž platí, že součty čísel v každém řádku, každém sloupci a
# obou hlavních úhlopříčkách jsou stejné. Klasickým příkladem je magický
# čtverec 3x3:
# 8 1 6
# 3 5 7
# 4 9 2
# v němž se součty všech řádků, všech sloupců a obou diagonál rovnají 15.

# Napište predikát is_magic_square, který na vstupu dostane dvourozměrné pole
# celých čísel a ověří, že se jedná o magický čtverec.


def is_magic_square(square: list[list[int]]) -> bool:
    pass


def main() -> None:
    assert is_magic_square([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    assert is_magic_square([])
    assert is_magic_square([[1]])
    assert not is_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert not is_magic_square([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert is_magic_square([[16, 2, 3, 13], [5, 11, 10, 8],
                           [9, 7, 6, 12], [4, 14, 15, 1]])


if __name__ == "__main__":
    main()
