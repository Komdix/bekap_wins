from ib111 import week_08  # noqa
from d1_countsort import is_permutation, is_sorted, all_lists


# V této ukázce si ukážeme další řadicí algoritmus, tentokrát budeme
# ale řadit «zřetězené» seznamy, které nelze efektivně indexovat.
# Jejich výhodou je naopak možnost levně vkládat hodnoty doprostřed:
# proto si na nich demonstrujeme tzv. «insertion sort», neboli
# řazení vkládáním. Myšlenka tohoto algoritmu je také velmi
# jednoduchá:
#
#  1. vytvoříme prázdný «výstupní seznam»,
#  2. prvky postupně odebíráme ze začátku vstupního seznamu,
#  3. pro každý odebraný vstupní prvek najdeme ve vznikajícím
#     výstupním seznamu správné místo a tam ho vložíme.
#
# Nejprve si definujeme složený datový typ, kterým budeme
# reprezentovat zřetězené seznamy:

class Node:
    def __init__(self, value: int):
        self.next: Node | None = None
        self.value = value


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


# Nyní již můžeme přistoupit k samotnému zápisu algoritmu pro řazení
# vkládáním. Oproti předchozí ukázce bude algoritmus realizovat
# «procedura». Nazveme ji ‹insert_sort›, a bude přesně kopírovat
# postup z úvodního odstavce. Abychom zachovali jednoduchou a jasnou
# strukturu hlavního výpočtu, veškeré pomocné výpočty oddělíme do
# pomocných procedur.

def insert_sort(records: LinkedList) -> None:
    out = LinkedList()
    while records.head is not None:
        to_insert = remove_head(records)
        insert_sorted(out, to_insert)

    # V seznamu ‹out› máme nyní seřazený výsledek, naším úkolem ale
    # bylo přeuspořádat stávající seznam ‹records›, který je nyní
    # prázdný. Proto do něj „převěsíme“ celý seznam ‹out›.
    records.head = out.head


# První pomocná «procedura», ‹remove_head›, oddělí hlavu neprázdného
# seznamu, a vrátí ji jako samostatný (izolovaný) uzel.

def remove_head(lst: LinkedList) -> Node:
    assert lst.head is not None
    result = lst.head
    lst.head = lst.head.next
    result.next = None
    return result


# Další pomocná «procedura», ‹insert_sorted›, vloží uzel do
# seřazeného seznamu, a to tak, že výsledný seznam zůstane seřazený
# (jeho délka se přitom zvýší o jedna). Více explicitně, procedura
# ‹insert_sorted› má tyto vstupní podmínky:
#
#  • ‹out› je seřazený zřetězený seznam (může být prázdný),
#  • ‹node› je uzel, který není součástí ‹out›.
#
# Výstupní podmínkou je:
#
#  • ‹out› je seřazený seznam a ‹node› je součástí ‹out›.
#
# Samotné vložení uzlu je jednoduché: „těžká“ část této procedury je
# nalézt vhodné místo, kam uzel vložit. Tuto část oddělíme do
# pomocné «čisté funkce», ‹find_position›, která vrátí dvojici uzlů,
# «mezi které» budeme uzel vkládat. Jeden, nebo i oba vrácené uzly
# mohou být ‹None›.

def insert_sorted(out: LinkedList, node: Node) -> None:
    before, after = find_position(out, node.value)
    if before is None:
        out.head = node
    else:
        before.next = node
    node.next = after


# Zbývá nám definovat poslední, a v podstatě i nejsložitější,
# podprogram. Na rozdíl od těch předchozích se bude jednat o «čistou
# funkci»: vstupní seznam nebudeme nijak měnit. Tato funkce má
# následující vstupní podmínku:
#
#  • ‹items› je seřazený zřetězený seznam,
#  • ‹value› může ale nemusí být v seznamu přítomna.
#
# Nazveme-li složky návratové hodnoty ‹before› a ‹after›, výstupní
# podmínku můžeme popsat takto:
#
#  • ‹before› i ‹after› jsou ‹None› a ‹items› je prázdný, «nebo»
#  • ‹before› je ‹None› a ‹value <= after.value›, «nebo»
#  • ‹after› je ‹None› a ‹before.value <= value›, «nebo»
#  • ‹before.value <= value <= after.value›.

def find_position(items: LinkedList, value: int) \
        -> tuple[Node | None, Node | None]:
    before = None
    after = items.head

    while after is not None and value >= after.value:
        before = after
        after = after.next

    return (before, after)


# Tím je definice procedury ‹insert_sort› a jejích pomocných
# podprogramů hotova. Zbývá nám proceduru otestovat: na to budeme
# potřebovat další dvě pomocné funkce (obě budou čisté):
# ‹to_linked_list› která z klasického Pythonovského seznamu vytvoří
# seznam zřetězený, a funkce ‹to_python_list› která provede konverzi
# opačnou.

def to_linked_list(items: list[int]) -> LinkedList:
    out = LinkedList()
    for i in range(len(items) - 1, -1, -1):
        node = Node(items[i])
        node.next = out.head
        out.head = node
    return out


def to_python_list(items: LinkedList) -> list[int]:
    ptr = items.head
    out = []
    while ptr is not None:
        out.append(ptr.value)
        ptr = ptr.next
    return out


# Stejně jako v předchozí ukázce budeme proceduru ‹insert_sort›
# testovat pro všechny seznamy z parametrické rodiny. Přípustné
# kombinace parametrů nám bude generovat funkce ‹test_parameters›,
# jako seznam trojic: nejmenší a největší číslo, které se objeví, a
# celková délka seznamu.

def test_parameters() -> list[tuple[int, int, int]]:
    result = []
    for high in range(10):
        for low in range(high):
            for count in range(1, 5):
                result.append((low, high, count))
    return result


# Funkce ‹main› podle parametrů z ‹test_parameters› vygeneruje
# všechny odpovídající «seřazené» seznamy, a pro každý seřazený
# seznam ověří, že procedura ‹insert_sort› korektně seřadí všechny
# jeho permutace.

def main() -> None:  # demo
    for low, high, count in test_parameters():
        for records in all_lists(low, high, count, True, []):
            linked = to_linked_list(records)
            insert_sort(linked)
            result = to_python_list(linked)
            assert is_sorted(result)
            assert is_permutation(result, records)


if __name__ == '__main__':
    main()
