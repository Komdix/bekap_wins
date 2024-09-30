from ib111 import week_03  # noqa


# Mějme seznam nezáporných celých čísel reprezentující výšky ve 2D
# terénu.  Plošinou v tomto seznamu nazveme maximální souvislý úsek
# stejné výšky délky alespoň 2.
#
# Čistá funkce ‹flats› dostane na vstupu takový seznam a vrátí
# seznam, v němž je každá plošina reprezentovaná její výškou, a to
# ve stejném pořadí, v jakém jsou plošiny v původním seznamu.

def flats(heights):
    pass


# Příklad: Volání ‹flats([2, 2, 4, 5, 4, 4, 3])› vrátí ‹[2, 4]›.
# Volání ‹flats([1, 2, 2, 10, 2, 9, 3, 3, 2, 2])› vrátí ‹[2, 3, 2]›.

def main() -> None:
    heights = [2, 2, 4, 5, 4, 4, 3]
    assert flats(heights) == [2, 4]
    assert heights == [2, 2, 4, 5, 4, 4, 3]

    heights = [1, 2, 3, 5, 4, 7, 2, 1]
    assert flats(heights) == []

    heights = [1, 2, 2, 10, 2, 9, 3, 3, 2, 2]
    assert flats(heights) == [2, 3, 2]

    heights = [0, 0, 1, 1, 2, 2, 0, 2, 2, 0, 2]
    assert flats(heights) == [0, 1, 2, 2]
    assert heights == [0, 0, 1, 1, 2, 2, 0, 2, 2, 0, 2]

    heights = []
    assert flats(heights) == []


if __name__ == '__main__':
    main()
