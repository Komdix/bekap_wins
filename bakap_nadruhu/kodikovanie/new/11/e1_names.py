from ib111 import week_11  # noqa
import os


# Napište podprogram ‹names_sorted›, který ze souboru s cestou
# ‹filename› načte jména, seřadí je primárně podle příjmení,
# sekundárně podle křestního jména a seřazená jména vrátí jako
# seznam řetězců.
#
# Soubor je ve formátu CSV vždy se dvěma sloupci: jméno a příjmení.
# Soubor může obsahovat prázdné řádky – tyto ignorujte.

def names_sorted(filename: str) -> list[str]:
    pass


# Dále napište proceduru ‹format_names›, která uloží jména ze
# souboru s cestou ‹source› seřazená primárně podle příjmení,
# sekundárně podle křestního jména do souboru s cestou ‹dest›.
# Vstupní i výstupní soubor budou ve formátu CSV.

def format_names(source: str, dest: str) -> None:
    pass


def main() -> None:
    f_simple = 'zz.names_simple.csv'
    e_simple = ['Klara Koci', 'Bedrich Novak', 'Jan Novak']

    f_long = 'zz.names_long.csv'
    e_long = ['Kral Beran', 'Kvetoslav Beran', 'Jaromir Kral',
              'Marian Kral', 'Zdenek Kral', 'Havel Kubik',
              'Vendelin Kubik', 'Jaromir Malek', 'Zdenek Nemec',
              'Havel Rypal']

    assert names_sorted(f_simple) == e_simple
    assert names_sorted(f_long) == e_long

    assert test_format(f_simple, e_simple)
    assert test_format(f_long, e_long)


def test_format(source: str, expect: list[str]) -> bool:
    dest = 'names-testfile.csv'
    if os.path.exists(dest):
        os.remove(dest)

    format_names(source, dest)
    assert os.path.exists(dest)

    with open(dest, 'r') as result:
        assert [line.rstrip() for line in result] == \
               [x.replace(' ', ',') for x in expect]

    if os.path.exists(dest):
        os.remove(dest)

    return True


if __name__ == '__main__':
    main()
