from ib111 import week_06  # noqa


# Představte si robota, který se umí pohybovat dopředu a dozadu a otáčet
# se o 90° v obou směrech. Pozici robota reprezentujeme dvojicí celých čísel;
# první souřadnice je ⟦x⟧-ová (záporná čísla jsou na západ od
# počátku, kladná na východ), druhá souřadnice je ⟦y⟧-ová (záporná
# čísla jsou na sever, kladná na jih).
#
# Čistá funkce ‹simulate_robot› dostane seznam instrukcí pro robota,
# vykoná je a vrátí finální pozici robota. Na začátku je robot na
# souřadnicích (0, 0) a je otočen směrem k severu. Jednotlivé
# instrukce jsou dvojice v tomto formátu:
#
#  • ‹("rotate", n)› – robot se otočí o ⟦n⋅90°⟧ doprava (pro záporná
#    ⟦n⟧ doleva);
#  • ‹("forward", n)› – robot se posune o ⟦n⟧ kroků dopředu;
#  • ‹("backward", n)› – robot se posune o ⟦n⟧ kroků dozadu;
#  • ‹("undo", n)› – robot zruší efekt posledních ⟦n⟧ provedených
#    instrukcí.
#
# U příkazů jiných než ‹rotate› je ‹n› vždy nezáporné celé číslo.
# Instrukce ‹undo› může být použita vícekrát a je tak možno rušit
# efekt více instrukcí, např. posloupnost instrukcí ‹forward 3›,
# ‹backward 7›, ‹undo 1›, ‹undo 1› způsobí, že robot bude stát na
# své počáteční pozici. Smíte předpokládat, že k instrukci ‹undo n›
# nedojde ve chvíli, kdy zbývá méně než ⟦n⟧ předchozích instrukcí.
# Zejména tedy ‹undo 1› nemůže stát na začátku souboru (ale ‹undo 0›
# ano).

def simulate_robot(instructions: list[tuple[str, int]]) \
        -> tuple[int, int]:
    pass


def main() -> None:
    assert simulate_robot([("forward", 100),
                           ("rotate", -1),
                           ("backward", 17),
                           ("rotate", 1),
                           ("rotate", 1),
                           ("rotate", 1),
                           ("undo", 1),
                           ("forward", 42)]) == (59, -100)
    assert simulate_robot([("forward", 1),
                           ("forward", 2),
                           ("forward", 5),
                           ("forward", 6),
                           ("undo", 1),
                           ("undo", 1),
                           ("forward", 3),
                           ("forward", 4)]) == (0, -10)

    cmds = [("rotate", -1), ("rotate", -1), ("rotate", -1)]
    assert simulate_robot(cmds) == (0, 0)
    assert cmds == [("rotate", -1), ("rotate", -1), ("rotate", -1)]

    cmds = [("backward", 1),
            ("backward", 2),
            ("rotate", -1),
            ("undo", 1),
            ("backward", 3),
            ("backward", 4)]
    assert simulate_robot(cmds) == (0, 10)
    assert cmds == [("backward", 1),
                    ("backward", 2),
                    ("rotate", -1),
                    ("undo", 1),
                    ("backward", 3),
                    ("backward", 4)]

    assert simulate_robot([("forward", 10000), ("backward", 10000)]) == (0, 0)
    assert simulate_robot([("rotate", -1), ("backward", 7)]) == (7, 0)
    assert simulate_robot([("forward", 100),
                           ("rotate", -1),
                           ("backward", 42),
                           ("undo", 2),
                           ("forward", 2022),
                           ("undo", 1),
                           ("undo", 1),
                           ("rotate", 1),
                           ("backward", 7)]) == (-7, 0)


if __name__ == '__main__':
    main()
