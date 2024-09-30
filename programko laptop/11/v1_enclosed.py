from ib111 import week_11  # noqa


# V tomto příkladu budeme pracovat s textovými soubory, v nichž nás budou
# zajímat kulaté, hranaté a složené závorky.
# Napište funkci ‹count_fully_enclosed›, která v případě, že je obsah souboru
# korektně uzávorkován, vrátí počet nezávorkových znaků, které jsou uzavřeny
# do všech tří typů závorek. Znaky konce řádku přitom nepočítáme.
# Není-li obsah souboru korektně uzávorkován, funkce vrátí ‹None›.
#
# Příklad:
# Je-li na vstupu soubor s tímto obsahem:
#
#     a + (((
#     b - c) + d)
#     [{{(x, y)}}])
#
# (písmeno a stojí na začátku řádku),
# pak má funkce vrátit číslo 4, protože jsou zde celkem čtyři nezávorkové
# znaky, které jsou uzavřeny do všech tří typů závorek
# (jsou to znaky ‹x, y› – za čárkou je mezera).

def count_fully_enclosed(filename: str) -> int | None:
    pass


def main() -> None:
    # Running this test function will create a file with the following name;
    # if such a file exists, it will be overwritten!
    test_filename = "__ib111_tmp_file__"

    test_cases = [
        ("a + (((\n"
         "b - c) + d)\n"
         "[{(x, y)}])\n",
         4),
        ("[]\n", 0),
        ("[({ in \n })] out\n[({ in {}[] } out {in\n})]\n", 12),
        ("this file has no brackets\n", 0),
        ("((([[[{{{)}}]]])))\n", None),
        ("{{{}}}(\n[\n{\n}\n]\n)\n()[[]]\n", 0),
        ("{{{}}(\n[\n{\n}\n]\n)\n[(x[]x)]}\n", 2),
    ]

    for content, result in test_cases:
        with open(test_filename, "w") as file:
            file.write(content)

        assert count_fully_enclosed(test_filename) == result


if __name__ == '__main__':
    main()
