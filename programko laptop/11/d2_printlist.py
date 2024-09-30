from ib111 import week_11  # noqa


# V této ukázce se zaměříme na rekurzivní procedury pro práci
# s výstupem. Konkrétně se budeme zabývat vnořenými odrážkovými
# seznamy, které budeme v programu reprezentovat jako seznam objektů
# typu ‹Item›. Každá odrážka (instance ‹Item›) v takovém seznamu má
# nějaký vlastní text (atribut ‹text›) a případně seznam pododrážek
# (atribut ‹sublists›).

class Item:
    def __init__(self, text: str):
        self.text: str = text
        self.sublists: list[Item] = []


# V parametru ‹itemize› budeme proceduře ‹print_itemize_rec›
# předávat relevantní odrážkový seznam, v parametru ‹prefix› budeme
# uchovávat řetězec, který vypíšeme před každou jednotlivou
# odrážkou: tím budeme realizovat zanoření, které by mělo ve výstupu
# vypadat takto:
#
#     - odrážka 1
#      - odrážka druhé úrovně
#      - další odrážka druhé úrovně
#     - odrážka 2
#      - zanořená odrážka
#       - ještě zanořenějši odrážka
#
# Na této proceduře je zajímavé také to, že bázový případ není
# zmíněn explicitně: pozorný čtenář si ale jistě všimne, že odrážka,
# která již žádné pododrážky nemá, bude mít seznam ‹sublists›
# prázdný. Na prázdném seznamu ale procedura ‹print_itemize_rec›
# neudělá vůbec nic: cyklus v jejím těle se ani jednou neprovede.
#
# Výstup postupně sestavujeme v seznamu ‹lines›, který si předáváme
# pomocným parametrem.

def format_itemize(itemize: list[Item], prefix: str,
                   lines: list[str]) -> None:
    for i in itemize:
        lines.append(prefix + '- ' + i.text + "\n")
        format_itemize(i.sublists, prefix + ' ', lines)


# Procedura ‹print_itemize› pomocí procedury ‹format_itemize›
# vytvoří seznam řádků a tyto uloží do souboru: krom otevření
# souboru pro zápis se stará také o nastartování rekurze.

def print_itemize(itemize: list[Item], path: str) -> None:
    lines: list[str] = []
    format_itemize(itemize, '', lines)
    with open(path, 'w') as out:
        for line in lines:
            out.write(line)


# Tím je ukázka kompletní. Program jako obvykle otestujeme na
# jednoduchém vstupu.

def main() -> None:  # demo
    path = 'zt.print_itemize.txt'
    itemize = [Item('foo'), Item('bar'), Item('wibble')]
    itemize[1].sublists.extend([Item('baz'), Item('quux')])
    itemize[1].sublists[0].sublists.append(Item('baz 2'))
    itemize[2].sublists.extend([Item('quuux')])
    print_itemize(itemize, path)
    assert open(path).read() == ('- foo\n'
                                 '- bar\n'
                                 ' - baz\n'
                                 '  - baz 2\n'
                                 ' - quux\n'
                                 '- wibble\n'
                                 ' - quuux\n')


if __name__ == '__main__':
    main()
