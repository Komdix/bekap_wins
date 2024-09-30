from ib111 import week_12  # noqa


# Tabulkové procesory často pro označení sloupců používají znaky anglické
# abecedy, přičemž po vyčerpání 26 možností ‹A› až ‹Z› se pokračuje
# ‹AA›, ‹AB›, ..., ‹ZZ›, ‹AAA›, ‹AAB›, ...
#
# Čistá funkce ‹spreadsheet_column› dostane jako parametr index sloupce
# (nezáporné celé číslo, indexujeme od 0) a vrátí řetězec příslušný danému
# sloupci. Indexu 2 tedy odpovídá řetězec ‹"C"›, indexu 27 řetězec ‹"AB"›,
# indexu 16383 řetězec ‹"XFD"›.
#
# Funkce musí rozumně rychle fungovat pro libovolně velká čísla.

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def spreadsheet_column(index):
    pass


def main() -> None:
    assert spreadsheet_column(2) == "C"
    assert spreadsheet_column(27) == "AB"
    assert spreadsheet_column(16383) == "XFD"
    assert spreadsheet_column(23383) == "AHOJ"
    assert spreadsheet_column(16168) == "WWW"
    assert spreadsheet_column(1297169788) == "DEDOLES"
    assert spreadsheet_column(17627) == "ZAZ"


if __name__ == '__main__':
    main()
