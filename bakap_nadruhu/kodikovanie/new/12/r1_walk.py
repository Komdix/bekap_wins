from ib111 import week_12  # noqa

# V této úloze budeme implementovat simulaci procházky po 2D mřížce.
# Pro reprezentaci pozice v mřížce budeme používat uspořádanou
# dvojici ⟦(x, y)⟧.

Position = tuple[int, int]

# Cesta procházky je zadaná jako řetězec ‹path›, který se skládá
# z příkazů ‹←› / ‹→› pro pohyb doleva a doprava (po ose ⟦x⟧) a ‹↑›
# / ‹↓› pro pohyb nahoru a dolů (po ose ⟦y⟧). Souřadnice rostou ve
# směru doprava na ⟦x⟧-ové ose a nahoru na ⟦y⟧-ové ose.

# Napište čistou funkci ‹walk›, která vrátí finální pozici pro
# procházku ‹path› z počáteční pozice ‹start›.


def walk(path: str, start: Position) -> Position:
    pass


# Dále napište čistou funkci ‹meet›, která vrátí pro dvojici cest
# ‹path_1›, ‹path_2› a počátků ‹start_1› a ‹start_2›, první pozici
# na které se procházky potkají. Procházky se provádí synchronně,
# tj. kroky se vykonávají najednou pro obě procházky. Pokud se
# procházky nepotkají, funkce vrátí ‹None›.

def meet(path_1: str, path_2: str, start_1: Position,
         start_2: Position) -> Position | None:
    pass


def main() -> None:
    assert walk("→→", (0, 0)) == (2, 0)
    assert walk("←↑→↓", (0, 0)) == (0, 0)
    assert walk("←←↑↑→↑↑→→↓→→→↑↑", (2, 3)) == (6, 8)
    assert walk("↑←↑→↑→", (-1, -3)) == (0, 0)

    assert meet("→→", "←←", (-1, 0), (1, 0)) == (0, 0)
    assert meet("←", "↓", (1, 0), (0, 1)) == (0, 0)

    assert meet("←↑→↓", "→↓←↑", (1, 0), (0, 1)) is None
    assert meet("↓↓↓↓↓↓", "↓↓↓↓↓↓", (1, 0), (0, 0)) is None

    assert meet("→↓→↓→↑←←→↓↓→", "↑→→↓→↓→↓→↑→←←",
                (2, 2), (-1, 1)) == (4, 0)


if __name__ == '__main__':
    main()
