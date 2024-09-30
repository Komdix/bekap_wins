from ib111 import week_08, except_data_structures  # noqa


# V tomto příkladu budeme pracovat se zřetězenými seznamy. Třídy ‹Node›
# a ‹LinkedList› jsou připraveny; nijak je nemodifikujte.

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


# Implementujte proceduru, která dostane na vstup vzestupně seřazený
# jednosměrně zřetězený seznam, z tohoto seznamu odstraní všechny duplikáty
# (uzly se stejnými hodnotami) tak, že v něm nechá vždy pouze první výskyt.
# Odstraněné uzly funkce spojí do nového zřetězeného seznamu (se zachováním
# jejich pořadí) a ten vrátí.
#
# Při řešení neměňte hodnoty atributu ‹value› ani nevytvářejte nové
# uzly typu ‹Node›, tj. jediné, co můžete s uzly dělat, je měnit odkazy
# na následující uzel.
#
# V tomto příkladu je zakázáno použití Pythonovských datových struktur
# seznam, množina, slovník.
#
# Příklad: Je-li zřetězený seznamu tvaru ‹1 → 2 → 2 → 2 → 7 → 7 → 10›,
# pak procedura modifikuje tento seznam do tvaru ‹1 → 2 → 7 → 10› a vrátí
# zřetězený seznam tvaru ‹2 → 2 → 7›.

def remove_duplicates(llist: LinkedList) -> LinkedList:
    pass


def main() -> None:
    llist = LinkedList()

    result = remove_duplicates(llist)

    node = llist.head
    assert node is None

    node = result.head
    assert node is None

    # 1
    n0 = Node(1)
    llist = LinkedList()
    llist.head = n0

    result = remove_duplicates(llist)

    node = llist.head
    assert node == n0  # 1
    node = node.next
    assert node is None

    node = result.head
    assert node is None

    # -7 -> 1337
    n1 = Node(1337)
    n0 = Node(-7)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = remove_duplicates(llist)

    node = llist.head
    assert node == n0  # -7
    node = node.next
    assert node == n1  # 1337
    node = node.next
    assert node is None

    node = result.head
    assert node is None

    # 17 -> 17
    n1 = Node(17)
    n0 = Node(17)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = remove_duplicates(llist)

    node = llist.head
    assert node == n0  # 17
    node = node.next
    assert node is None

    node = result.head
    assert node == n1  # 17
    node = node.next
    assert node is None

    # 1 -> 1 -> 3
    n2 = Node(3)
    n1 = Node(1)
    n1.next = n2
    n0 = Node(1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = remove_duplicates(llist)

    node = llist.head
    assert node == n0  # 1
    node = node.next
    assert node == n2  # 3
    node = node.next
    assert node is None

    node = result.head
    assert node == n1  # 1
    node = node.next
    assert node is None

    # -15 -> -5 -> -5
    n2 = Node(-5)
    n1 = Node(-5)
    n1.next = n2
    n0 = Node(-15)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = remove_duplicates(llist)

    node = llist.head
    assert node == n0  # -15
    node = node.next
    assert node == n1  # -5
    node = node.next
    assert node is None

    node = result.head
    assert node == n2  # -5
    node = node.next
    assert node is None

    # 1 -> 2 -> 2 -> 2 -> 7 -> 7 -> 10
    n6 = Node(10)
    n5 = Node(7)
    n5.next = n6
    n4 = Node(7)
    n4.next = n5
    n3 = Node(2)
    n3.next = n4
    n2 = Node(2)
    n2.next = n3
    n1 = Node(2)
    n1.next = n2
    n0 = Node(1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = remove_duplicates(llist)

    node = llist.head
    assert node == n0  # 1
    node = node.next
    assert node == n1  # 2
    node = node.next
    assert node == n4  # 7
    node = node.next
    assert node == n6  # 10
    node = node.next
    assert node is None

    node = result.head
    assert node == n2  # 2
    node = node.next
    assert node == n3  # 2
    node = node.next
    assert node == n5  # 7
    node = node.next
    assert node is None


if __name__ == '__main__':
    main()
