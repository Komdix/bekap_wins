from ib111 import week_05  # noqa


# Vaším úkolem je naprogramovat tzv. „hru života“ – jednoduchý
# dvourozměrný celulární automat. Simulace běží na čtvercové síti,
# kde každá buňka je mrtvá (hodnota 0) nebo živá (hodnota 1).
# V každém kroku se přepočte hodnota všech buněk, a to podle toho,
# zda byly v předchozím kroku živé a kolik měly živých sousedů
# (z celkem osmi, tzn. včetně úhlopříčných):
#
# │  stav │ živí sousedé │ výsledek │
# ├───────┼──────────────┼──────────┤
# │  živá │          0–1 │    mrtvá │
# │  živá │          2–3 │     živá │
# │  živá │          4–8 │    mrtvá │
# │┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│
# │ mrtvá │          0–2 │    mrtvá │
# │ mrtvá │            3 │     živá │
# │ mrtvá │          4-8 │    mrtvá │

# Příklad krátkého výpočtu:
#
#  ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │ ○ │ ○ │ ○ │ → │ ○ │   │   │ → │ ○ │   │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
#
# Jiný (periodický) výpočet je například:
#
#  ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
#  │   │   │   │   │   │ ○ │   │   │   │   │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │ ○ │ ○ │ ○ │ → │   │ ○ │   │ → │ ○ │ ○ │ ○ │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │   │   │   │   │   │ ○ │   │   │   │   │   │
#  └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
#
# Napište čistou funkci, která dostane jako parametry počáteční stav
# hry (jako množinu dvojic, která reprezentuje souřadnice živých
# buněk) a počet kroků, a vrátí stav hry po odpovídajícím počtu
# kroků.


def life(cells: set[tuple[int, int]],
         n: int) -> set[tuple[int, int]]:
    pass


def main() -> None:
    assert life(set(), 3) == set()
    assert life({(0, 0)}, 1) == set()
    block = {(0, 0), (1, 1), (0, 1), (1, 0)}

    blinker_0 = {(0, -1), (0, 0), (0, 1)}
    blinker_1 = {(-1, 0), (0, 0), (1, 0)}
    glider = blinker_1.copy()
    glider.add((1, -1))
    glider.add((0, -2))

    for i in range(20):
        assert life(block, i) == block, life(block, i)

    for i in range(20):
        expect = blinker_0 if i % 2 == 0 else blinker_1
        assert life(blinker_0, i) == expect

    for i in range(0, 40, 4):
        expect = set()
        for x, y in glider:
            expect.add((x + i // 4, y + i // 4))
        assert life(glider, i) == expect, (i, life(glider, i), expect)


if __name__ == "__main__":
    main()
