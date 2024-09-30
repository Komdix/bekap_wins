from ib111 import week_06  # noqa


# Představte si robotickou žábu, která umí skákat rovně dopředu
# o zadanou celočíselnou délku a otáčet se o 90° v obou směrech.
#
# Čistá funkce ‹simulate_frogbot› dostane seznam instrukcí pro robožábu,
# vykoná je a vrátí počet různých pozic, na kterých se žába během vykonávání
# instrukcí nacházela (včetně počáteční a poslední pozice). Pozor na to,
# že na některou pozici se v průběhu vykonávání instrukcí může žába dostat
# vícekrát – tuto pozici pořád započítáváme jen jednou.
#
# Jednotlivé instrukce jsou dvojice v tomto formátu:
#
#  • ‹("rotate", n)› – robožába se otočí o ⟦n⋅90°⟧ (kladný úhel
#    doprava, záporný doleva);
#  • ‹("jump", n)› – robožába poskočí o ⟦n⟧ jednotek dopředu.
#
# Zde ⟦n⟧ může být libovolné kladné celé číslo (funkce musí bez
# problémů fungovat i pro obrovská čísla).
#
# «Poznámka:» Všimněte si, že na počáteční pozici ani natočení žáby odpověď
# vůbec nezáleží.

def simulate_frogbot(instructions: list[tuple[str, int]]) -> int:
    pass


def main() -> None:
    assert simulate_frogbot([("jump", 100),
                             ("rotate", -1),
                             ("jump", 17),
                             ("rotate", 1),
                             ("rotate", 1),
                             ("jump", 42)]) == 4

    cmds = [("jump", 1), ("jump", 2), ("jump", 3), ("jump",  4)]
    assert simulate_frogbot(cmds) == 5
    assert cmds == [("jump", 1), ("jump", 2), ("jump", 3), ("jump",  4)]

    assert simulate_frogbot([("rotate", -1), ("rotate", -1),
                             ("rotate", -1)]) == 1

    cmds = [("jump", 2), ("rotate", -1), ("rotate", -1), ("jump", 2)]
    assert simulate_frogbot(cmds) == 2
    assert cmds == [("jump", 2), ("rotate", -1), ("rotate", -1), ("jump", 2)]

    assert simulate_frogbot([("jump", 7),
                             ("rotate", 1),
                             ("jump", 10000),
                             ("rotate", 1),
                             ("rotate", 1),
                             ("jump", 10000),
                             ("rotate", -1),
                             ("jump", 7),
                             ("rotate", 1)]) == 3
    assert simulate_frogbot([("jump", 5),
                             ("rotate", -1),
                             ("rotate", -1),
                             ("jump", 2),
                             ("jump", 3)]) == 3
    assert simulate_frogbot([("jump", 1),
                             ("jump", 4),
                             ("rotate", 1),
                             ("jump", 4),
                             ("rotate", 1),
                             ("jump", 2),
                             ("rotate", 1),
                             ("jump", 1),
                             ("rotate", -1),
                             ("jump", 2),
                             ("rotate", 1),
                             ("jump", 3),
                             ("jump", 17)]) == 8


if __name__ == '__main__':
    main()
