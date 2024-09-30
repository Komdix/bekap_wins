from ib111 import week_03  # noqa


# Pojmem „náhorní plošina“ označíme v seznamu celých čísel souvislou
# podposloupnost alespoň dvou stejných prvků, která ani z jedné
# strany nesousedí s vyšším prvkem.

# Čistá funkce ‹rightmost_plateau› dostane na vstup neprázdný seznam
# celých čísel a pokud tento seznam obsahuje alespoň jednu náhorní
# plošinu, tak vrátí index prvního prvku nejpravější náhorní plošiny
# v seznamu; v opačném případě vrátí číslo ‹-1›.

def rightmost_plateau(heights):
    pass


# Příklad: Volání ‹rightmost_plateau([2, 2, 4, 5, 5, 2])› vrátí ‹3›, protože
# seznam obsahuje jednu náhorní plošinu tvořenou čísly ‹5›, první prvek této
# plošiny je na indexu ‹3›.
# Volání ‹rightmost_plateau([3, 3, 2, 4, 4])› vrátí ‹3›, protože zadaný seznam
# obsahuje dvě náhorní plošiny, první prvek té nejpravější je na indexu 3.
# Volání ‹rightmost_plateau([2, 2, 3, 3, 4])› vrátí ‹-1›, protože zadaný seznam
# neobsahuje žádnou náhorní plošinu.

def main() -> None:
    heights = [2, 2, 4, 5, 5, 2]
    assert rightmost_plateau(heights) == 3
    assert heights == [2, 2, 4, 5, 5, 2]

    heights = [2, 2, 3, 3, 4]
    assert rightmost_plateau(heights) == -1

    heights = [7]
    assert rightmost_plateau(heights) == -1

    heights = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert rightmost_plateau(heights) == 6
    assert heights == [1, 1, 1, 2, 2, 2, 3, 3, 3]

    heights = [9, 9, 9, 9, 9, 0, 0, -9, -9, -9]
    assert rightmost_plateau(heights) == 0

    heights = [2, 1, 1, 1, 1, 1, 1, 2]
    assert rightmost_plateau(heights) == -1


if __name__ == '__main__':
    main()
