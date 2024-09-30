from ib111 import week_11  # noqa


# Představte si robota, který se umí pohybovat rovně dopředu o zadanou
# celočíselnou délku, otáčet se o 90° v obou směrech a případně za sebou
# nechávat stopu (tj. označovat místa, přes která jde).
#
# Pozici robota reprezentujeme dvojicí celých čísel; první souřadnice je
# x-ová (záporná čísla jsou na západ od počátku, kladná na východ), druhá
# souřadnice je y-ová (záporná čísla jsou na sever, kladná na jih).
# Na začátku je na souřadnicích (0, 0), je otočen k východu a je ve stavu,
# že za sebou nezanechává stopu.
#
# Funkce ‹simulate_paintbot› přečte ze zadaného souboru seznam instrukcí
# pro robota a bude je vykonávat do chvíle, než robot při pohybu narazí na
# vlastní stopu, tj. «vejde» na již označené místo.
#
# Funkce vrátí robotovu poslední pozici (tedy tu, na které narazil na
# vlastní stopu, nebo tu, kde skončil s vykonáváním poslední instrukce).
# Předpokládejte, že zadaný textový soubor není prázdný a obsahuje
# následující typy instrukcí (vždy jedna instrukce na řádku, žádné extra
# mezery na začátku ani na konci řádku):
#
#  • ‹rotate left› – robot se otočí o 90° doleva;
#  • ‹rotate right› – robot se otočí o 90° doprava;
#  • ‹walk k› – robot popojde o ‹k› jednotek dopředu, kde ‹k› je
#    právě jedna římská číslice (tabulka níže; pokud je robot ve
#    stavu, že za sebou zanechává stopu, tak označí všechna místa,
#    kterými projde, včetně toho posledního, kam došel);
#  • ‹toggle› – pokud za sebou robot zanechával stopu, tak odteď nebude;
#    v opačném případě stopu zanechávat začne (počínaje aktuální pozicí).
#
# Zde ‹k› může být jedno z:
#  • ‹I› = 1 krok,
#  • ‹V› = 5 kroků,
#  • ‹X› = 10 kroků,
#  • ‹L› = 50 kroků,
#  • ‹C› = 100 kroků,
#  • ‹D› = 500 kroků,
#  • ‹M› = 1000 kroků.
#
# Smíte předpokládat, že celkový počet polí, které robot v průběhu
# vykonávání instrukcí projde, je menší než milion.

def simulate_paintbot(filename: str) -> tuple[int, int]:
    pass


def main() -> None:
    # Running this test function will create a file with the following name;
    # if such a file exists, it will be overwritten!
    test_filename = "__ib111_tmp_file__"

    test_cases = [
        ("walk X\n"
         "rotate left\n"
         "walk X\nwalk X\n"
         "rotate right\n"
         "walk X\nwalk X\nwalk X\n",
         40, -20),
        ("walk M\n"
         "walk D\n"
         "walk C\n"
         "walk L\n"
         "walk X\n"
         "walk V\n"
         "walk I\n",
         1666, 0),
        ("toggle\n"
         "rotate left\n"
         "walk X\nwalk V\nwalk I\nwalk I\n"
         "rotate right\n"
         "walk V\nwalk I\nwalk I\n"
         "rotate right\n"
         "walk I\nwalk I\nwalk I\n"
         "rotate right\n"
         "walk C\n"
         "rotate left\n"
         "walk D\n",
         0, -14),
        ("toggle\n"
         "walk C\n"
         "rotate right\n"
         "rotate right\n"
         "walk V\n",
         99, 0),
        ("walk C\n"
         "rotate right\n"
         "toggle\n"
         "rotate right\n"
         "walk V\n",
         95, 0),
        ("toggle\n"
         "walk V\n"
         "toggle\n"
         "walk X\nwalk V\nwalk I\nwalk I\n"
         "rotate left\n"
         "walk X\nwalk V\nwalk I\nwalk I\n"
         "rotate left\n"
         "walk X\nwalk V\nwalk I\nwalk I\n"
         "rotate left\n"
         "walk M\n"
         "rotate right\n"
         "walk X\nwalk X\nwalk X\nwalk X\nwalk I\nwalk I"
         "rotate left\n"
         "toggle\n"
         "walk C\nwalk C\nwalk V\nwalk I\nwalk I\n"
         "rotate right\n"
         "walk X\nwalk X\nwalk X\n",
         5, 0),
        ("walk V\n"
         "rotate right\n"
         "toggle\n"
         "walk I\nwalk I\n"
         "rotate right\n"
         "walk I\nwalk I\n"
         "rotate right\n"
         "walk V\n"
         "toggle\n"
         "rotate left\n"
         "walk I\nwalk I\nwalk I\n"
         "rotate right\n"
         "walk I\nwalk I\n"
         "rotate right\n"
         "walk I\n"
         "rotate right\n"
         "walk V\n"
         "rotate right\n"
         "walk I\n"
         "rotate left\n"
         "rotate left\n"
         "walk X\nwalk X\nwalk V\nwalk I\nwalk I\n",
         3, 0),
        ("toggle\n"
         "toggle\n"
         "walk I\nwalk I\nwalk I\n"
         "rotate left\n"
         "rotate left\n"
         "walk C\n",
         0, 0),
    ]

    for content, x, y in test_cases:
        with open(test_filename, "w") as file:
            file.write(content)

        assert simulate_paintbot(test_filename) == (x, y)


if __name__ == '__main__':
    main()
