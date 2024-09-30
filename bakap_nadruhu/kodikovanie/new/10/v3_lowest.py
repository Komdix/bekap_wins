from ib111 import week_10  # noqa


# V tomto příkladu máme na vstupu neprázdný řetězec desítkových číslic
# (tj. znaků ‹'0'› až ‹'9'›), který «nezačíná znakem ‹'0'›», a chceme je
# rozsekat na části tak, aby tvořily rostoucí posloupnost čísel zapsaných
# v desítkové soustavě, přitom žádná část nesmí začínat znakem ‹'0'›.
# Ze všech takových posloupností pak chceme vybrat tu, která má co nejnižší
# své poslední číslo. Vaším úkolem je napsat čistou funkci, která spočítá
# toto číslo. Funkce by měla fungovat na vstupech o řádově desítkách znaků.
#
# Příklad: Řetězec ‹"23245"› můžeme rozsekat na rostoucí posloupnosti
# následujícími způsoby: 2, 3, 245 nebo 2, 32, 45 nebo 23, 245 nebo 23245.
# Nejnižší poslední číslo je 45; volání
# ‹lowest_increasing_sequence_end("23245")› tedy vrátí ‹45›.

def lowest_increasing_sequence_end(digits: list[int]) -> int:
    pass


def main() -> None:
    assert lowest_increasing_sequence_end([2, 3, 2, 4, 5]) == 45
    assert lowest_increasing_sequence_end([2, 0, 4, 4, 5]) == 445
    assert lowest_increasing_sequence_end([3, 2, 4, 5]) == 45
    assert lowest_increasing_sequence_end([9, 0, 1]) == 901
    assert lowest_increasing_sequence_end([9, 0, 2, 1, 0]) == 210
    assert lowest_increasing_sequence_end([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert lowest_increasing_sequence_end([1, 1, 1, 1, 1,
                                           1, 1, 1, 1, 1]) == 1111
    assert lowest_increasing_sequence_end([9, 9, 9]) == 99
    assert lowest_increasing_sequence_end([9, 9]) == 99


if __name__ == '__main__':
    main()
