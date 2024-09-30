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


# Implementujte proceduru ‹sort_linked_list›, která vzestupně seřadí
# zadaný zřetězený seznam. Nevytvářejte přitom žádné nové uzly ani
# nemodifikujte hodnoty (atributy ‹value›) těch existujících.
# Seřazení je třeba provést pouze pomocí změn atributů ‹next› (a ‹head›).
#
# Není třeba vymýšlet nějaké optimalizace, kvadratické řešení je zde
# v pořádku.
#
# V tomto příkladu je zakázáno použití Pythonovských datových struktur
# seznam, množina, slovník.


def sort_linked_list(llist: LinkedList) -> None:
    pass


def main() -> None:
    llist = LinkedList()

    sort_linked_list(llist)

    node = llist.head
    assert node is None

    # 1
    n0 = Node(1)
    llist = LinkedList()
    llist.head = n0

    sort_linked_list(llist)

    node = llist.head
    assert node == n0  # 1
    node = node.next
    assert node is None

    # 1 -> 1
    n1 = Node(1)
    n0 = Node(1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    sort_linked_list(llist)

    node = llist.head
    assert node == n0 or node == n1  # 1
    node = node.next
    assert node == n0 or node == n1  # 1
    node = node.next
    assert node is None

    # 6 -> 3 -> 7
    n2 = Node(7)
    n1 = Node(3)
    n1.next = n2
    n0 = Node(6)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    sort_linked_list(llist)

    node = llist.head
    assert node == n1  # 3
    node = node.next
    assert node == n0  # 6
    node = node.next
    assert node == n2  # 7
    node = node.next
    assert node is None

    # 6 -> 2 -> 0 -> 2 -> 6
    n4 = Node(6)
    n3 = Node(2)
    n3.next = n4
    n2 = Node(0)
    n2.next = n3
    n1 = Node(2)
    n1.next = n2
    n0 = Node(6)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    sort_linked_list(llist)

    node = llist.head
    assert node == n2  # 0
    node = node.next
    assert node == n1 or node == n3  # 2
    node = node.next
    assert node == n1 or node == n3  # 2
    node = node.next
    assert node == n0 or node == n4  # 6
    node = node.next
    assert node == n0 or node == n4  # 6
    node = node.next
    assert node is None

    # 0 -> 9 -> 17 -> 3 -> 5 -> 7
    n5 = Node(7)
    n4 = Node(5)
    n4.next = n5
    n3 = Node(3)
    n3.next = n4
    n2 = Node(17)
    n2.next = n3
    n1 = Node(9)
    n1.next = n2
    n0 = Node(0)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    sort_linked_list(llist)

    node = llist.head
    assert node == n0  # 0
    node = node.next
    assert node == n3  # 3
    node = node.next
    assert node == n4  # 5
    node = node.next
    assert node == n5  # 7
    node = node.next
    assert node == n1  # 9
    node = node.next
    assert node == n2  # 17
    node = node.next
    assert node is None

    # 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1
    n8 = Node(1)
    n7 = Node(2)
    n7.next = n8
    n6 = Node(3)
    n6.next = n7
    n5 = Node(4)
    n5.next = n6
    n4 = Node(5)
    n4.next = n5
    n3 = Node(6)
    n3.next = n4
    n2 = Node(7)
    n2.next = n3
    n1 = Node(8)
    n1.next = n2
    n0 = Node(9)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    sort_linked_list(llist)

    node = llist.head
    assert node == n8  # 1
    node = node.next
    assert node == n7  # 2
    node = node.next
    assert node == n6  # 3
    node = node.next
    assert node == n5  # 4
    node = node.next
    assert node == n4  # 5
    node = node.next
    assert node == n3  # 6
    node = node.next
    assert node == n2  # 7
    node = node.next
    assert node == n1  # 8
    node = node.next
    assert node == n0  # 9
    node = node.next
    assert node is None


if __name__ == '__main__':
    main()
