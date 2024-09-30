from ib111 import week_12  # noqa


# Napište čistou funkci ‹restore_sequence›, která dostane neprázdný řetězec
# složený pouze z číslic 0 a 1 a vrátí množinu všech možných
# řetězců, které vzniknou doplněním znaků čárky ‹','› do původního
# řetězce tak, aby části jimi oddělené byly dvojkové zápisy čísel
# v intervalu od ‹low› do ‹high› včetně. Hodnota ‹low› bude vždy
# alespoň 1. Rozdělení musí být takové, že žádný zápis neobsahuje
# levostranné nuly.

def restore_sequence(digits: str, low: int, high: int) -> set[str]:
    pass


def main() -> None:
    assert restore_sequence("1111", 2, 3) == {"11,11"}
    assert restore_sequence("11110", 1, 6) == \
        {"1,1,1,10", "11,1,10", "11,110", "1,1,110", "1,11,10"}
    assert restore_sequence("1111", 100, 200) == set()
    assert restore_sequence("101010", 2, 10) \
        == {"10,10,10", "10,1010", "1010,10"}
    assert restore_sequence("1001", 1, 30) == {"1001", "100,1"}
    assert restore_sequence("111101111", 0b101, 0b111) == {"111,101,111"}
    assert restore_sequence("1110101", 1, 9) == {
        "1,1,10,101",
        "11,10,101",
        "11,10,10,1",
        "1,110,101",
        "1,110,10,1",
        "1,1,10,10,1",
    }


if __name__ == '__main__':
    main()
