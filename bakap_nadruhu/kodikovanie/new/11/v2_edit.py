from ib111 import week_11  # noqa


# V tomto příkladu budeme pracovat s textovými soubory, které budou
# obsahovat následující editační značky (dvouznakové; první znak je vždy
# symbol stříšky ‹^›):
#
#  • ‹^H› znamená „smazat předchozí znak“ (pokud žádný předchozí znak
#    není, nestane se nic);
#  • ‹^U› má význam podle toho, kde se nachází; pokud se nachází na začátku
#    řádku, znamená „vrátit se na konec předchozího řádku“, pokud se
#    nachází jinde, znamená „smazat vše od začátku řádku“;`
#  • ‹^W› znamená „smazat předchozí slovo na tomto řádku“ (včetně
#    případných mezer, které stojí mezi posledním slovem a značkou
#    ‹^W›; pokud žádné předchozí slovo na aktuálním řádku není,
#    chová se jako ‹^U›).
#
# Slovo zde definujeme jako libovolnou posloupnost nemezerových znaků (tedy
# např. řetězec ‹"␣␣␣Hello,␣world!␣␣"› obsahuje dvě slova – mezery zde
# zdůrazňujeme znakem ‹␣›). Smíte předpokládat, že se v souboru nevyskytují
# jiné bílé znaky než mezery a konce řádků.
#
# Napište funkci ‹apply_edit_marks›, která přečte soubor s editačními
# značkami a vrátí řetězec, který vznikne tak, že se všechny úpravy
# naznačené editačními značkami provedou. Úpravy se provádějí postupně od
# prvního řádku a zleva doprava, tedy se např. značka ‹^U› může dostat na
# začátek řádku předchozími úpravami a pak se chová tak, jak se má chovat
# na začátku řádku. Smíte předpokládat, že se symbol stříšky ‹^› v souboru
# nevyskytuje jinde než ve výše uvedených značkách.
#
# Příklad:
# Je-li na vstupu soubor s tímto obsahem:
#
#     Hello, world^W^H^H!
#     How are you tonight?
#     ^U^Wtoday?
#     Everything is
#     awesome^U good ^W^H^U okay, i^HI guess.  ^Whope.
#
# (první písmeno ‹H› stojí na začátku řádku),
# pak funkce vrátí řetězec:
#
# ‹"Hello!\nHow are you today?\nEverything is okay, I hope.\n"›
#
# (‹\n› zde reprezentuje znak konce řádku, jak je nejen v Pythonu obvyklé).

def apply_edit_marks(filename: str) -> str:
    pass


def main() -> None:
    # Running this test function will create a file with the following name;
    # if such a file exists, it will be overwritten!
    test_filename = "__ib111_tmp_file__"

    # Add your own, if you want.
    test_cases = [
        ("Hello, world^W^H^H!\n"
         "How are you tonight?\n"
         "^U^Wtoday?\n"
         "Everything is\n"
         "awesome^U good ^W^H^U okay, i^HI guess.  ^Whope.\n",
         "Hello!\nHow are you today?\nEverything is okay, I hope.\n"),
        ("Backspaces don't work^H^H^H^H^H^H^H^H^H^Hare fine!\n",
         "Backspaces are fine!\n"),
        ("  To delete the  last  word, simply write the_caret_symbol and W  \n"
         "  ^W^W^W^W^W^W^W^W^W^Wor not to delete,\n"
         "that is the question!\n",
         "  To delete or not to delete,\nthat is the question!\n"),
        (" Deleteing ^U Deleting whole lines is possible. \n"
         "^U So is returning back.\n",
         " Deleting whole lines is possible.  So is returning back.\n"),
        (" ### ^W DE ^W DO ^W LES ^W ### ^H^H\n"
         " ^U deletes only this line ^U\n",
         "     ##\n\n"),
        ("Live\nlong\nand\nprosper.^W^W^W^W^W^W^W\n"
         "Live\nlong\nand\nprosper.^U^U^U^U^U^U^U\n",
         "\n\n"),
        ("^U does nothing\n"
         "    ^W^W^W does something\n"
         "^H also does something\n\n\n",
         " does  does something also does something\n\n\n"),
    ]

    for content, expect in test_cases:
        with open(test_filename, "w") as file:
            file.write(content)
        result = apply_edit_marks(test_filename)

        assert expect == result, \
            "\ninput: " + repr(content) + \
            "\nexpected: " + repr(expect) + \
            "\nbut got: " + repr(result)


if __name__ == '__main__':
    main()
