from ib111 import week_08, except_data_structures  # noqa


# V tomto příkladu budeme pracovat se zřetězenými seznamy. Třídy ‹Node›
# a ‹LinkedList› jsou připraveny; nijak je nemodifikujte.

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


# Implementujte proceduru, která dostane na vstup dva vzestupně seřazené
# jednosměrně zřetězené seznamy a z prvního z těchto seznamů odstraní uzly
# s hodnotami, které se vyskytují ve druhém seznamu.
# Druhý zřetězený seznam musí zůstat nezměněn.
#
# Při řešení neměňte hodnoty atributu ‹value› ani nevytvářejte nové
# uzly typu ‹Node›, tj. jediné, co můžete s uzly dělat, je měnit odkazy
# na následující uzel.
#
# Očekávané řešení má složitost lineární vůči součtu délek vstupních seznamů.
#
# V tomto příkladu je zakázáno použití Pythonovských datových struktur
# seznam, množina, slovník.
#
# Příklad: Je-li první zřetězený seznamu tvaru ‹1 → 3 → 5 → 5 → 7 → 10›
# a druhý zřetězený seznam tvaru ‹1 → 1 → 2 → 5 → 12›,
# pak procedura upraví první seznam do tvaru ‹3 → 7 → 10› (a druhý seznam
# nechá v původní podobě).

def list_diff(left: LinkedList, right: LinkedList) -> None:
    pass


def main() -> None:
    # left: empty
    # right: empty
    left = LinkedList()

    right = LinkedList()

    list_diff(left, right)

    node = left.head
    assert node is None

    node = right.head
    assert node is None

    # left: 1
    # right: empty
    nl0 = Node(1)
    left = LinkedList()
    left.head = nl0

    right = LinkedList()

    list_diff(left, right)

    node = left.head
    assert node == nl0  # 1
    node = node.next
    assert node is None

    node = right.head
    assert node is None

    # left: empty
    # right: 1
    left = LinkedList()

    nr0 = Node(1)
    right = LinkedList()
    right.head = nr0

    list_diff(left, right)

    node = left.head
    assert node is None

    node = right.head
    assert node == nr0  # 1
    node = node.next
    assert node is None

    # left: 1337
    # right: -7
    nl0 = Node(1337)
    left = LinkedList()
    left.head = nl0

    nr0 = Node(-7)
    right = LinkedList()
    right.head = nr0

    list_diff(left, right)

    node = left.head
    assert node == nl0  # 1337
    node = node.next
    assert node is None

    node = right.head
    assert node == nr0  # -7
    node = node.next
    assert node is None

    # left: 42
    # right: 42
    nl0 = Node(42)
    left = LinkedList()
    left.head = nl0

    nr0 = Node(42)
    right = LinkedList()
    right.head = nr0

    list_diff(left, right)

    node = left.head
    assert node is None

    node = right.head
    assert node == nr0  # 42
    node = node.next
    assert node is None

    # left: 42 -> 42
    # right: 17 -> 42 -> 100
    nl1 = Node(42)
    nl0 = Node(42)
    nl0.next = nl1
    left = LinkedList()
    left.head = nl0

    nr2 = Node(100)
    nr1 = Node(42)
    nr1.next = nr2
    nr0 = Node(17)
    nr0.next = nr1
    right = LinkedList()
    right.head = nr0

    list_diff(left, right)

    node = left.head
    assert node is None

    node = right.head
    assert node == nr0  # 17
    node = node.next
    assert node == nr1  # 42
    node = node.next
    assert node == nr2  # 100
    node = node.next
    assert node is None

    # left: 1 -> 2 -> 3
    # right: 5
    nl2 = Node(3)
    nl1 = Node(2)
    nl1.next = nl2
    nl0 = Node(1)
    nl0.next = nl1
    left = LinkedList()
    left.head = nl0

    nr0 = Node(5)
    right = LinkedList()
    right.head = nr0

    list_diff(left, right)

    node = left.head
    assert node == nl0  # 1
    node = node.next
    assert node == nl1  # 2
    node = node.next
    assert node == nl2  # 3
    node = node.next
    assert node is None

    node = right.head
    assert node == nr0  # 5
    node = node.next
    assert node is None

    # left: 1 -> 3 -> 5 -> 5 -> 7 -> 10
    # right: 1 -> 1 -> 2 -> 5 -> 12
    nl5 = Node(10)
    nl4 = Node(7)
    nl4.next = nl5
    nl3 = Node(5)
    nl3.next = nl4
    nl2 = Node(5)
    nl2.next = nl3
    nl1 = Node(3)
    nl1.next = nl2
    nl0 = Node(1)
    nl0.next = nl1
    left = LinkedList()
    left.head = nl0

    nr4 = Node(12)
    nr3 = Node(5)
    nr3.next = nr4
    nr2 = Node(2)
    nr2.next = nr3
    nr1 = Node(1)
    nr1.next = nr2
    nr0 = Node(1)
    nr0.next = nr1
    right = LinkedList()
    right.head = nr0

    list_diff(left, right)

    node = left.head
    assert node == nl1  # 3
    node = node.next
    assert node == nl4  # 7
    node = node.next
    assert node == nl5  # 10
    node = node.next
    assert node is None

    node = right.head
    assert node == nr0  # 1
    node = node.next
    assert node == nr1  # 1
    node = node.next
    assert node == nr2  # 2
    node = node.next
    assert node == nr3  # 5
    node = node.next
    assert node == nr4  # 12
    node = node.next
    assert node is None

    # left: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    # right: 2 -> 4 -> 6 -> 8
    nl6 = Node(7)
    nl5 = Node(6)
    nl5.next = nl6
    nl4 = Node(5)
    nl4.next = nl5
    nl3 = Node(4)
    nl3.next = nl4
    nl2 = Node(3)
    nl2.next = nl3
    nl1 = Node(2)
    nl1.next = nl2
    nl0 = Node(1)
    nl0.next = nl1
    left = LinkedList()
    left.head = nl0

    nr3 = Node(8)
    nr2 = Node(6)
    nr2.next = nr3
    nr1 = Node(4)
    nr1.next = nr2
    nr0 = Node(2)
    nr0.next = nr1
    right = LinkedList()
    right.head = nr0

    list_diff(left, right)

    node = left.head
    assert node == nl0  # 1
    node = node.next
    assert node == nl2  # 3
    node = node.next
    assert node == nl4  # 5
    node = node.next
    assert node == nl6  # 7
    node = node.next
    assert node is None

    node = right.head
    assert node == nr0  # 2
    node = node.next
    assert node == nr1  # 4
    node = node.next
    assert node == nr2  # 6
    node = node.next
    assert node == nr3  # 8
    node = node.next
    assert node is None

    # left: 10 -> 20 -> 30 -> 40 -> 42
    # right: 42 -> 42 -> 42
    nl4 = Node(42)
    nl3 = Node(40)
    nl3.next = nl4
    nl2 = Node(30)
    nl2.next = nl3
    nl1 = Node(20)
    nl1.next = nl2
    nl0 = Node(10)
    nl0.next = nl1
    left = LinkedList()
    left.head = nl0

    nr2 = Node(42)
    nr1 = Node(42)
    nr1.next = nr2
    nr0 = Node(42)
    nr0.next = nr1
    right = LinkedList()
    right.head = nr0

    list_diff(left, right)

    node = left.head
    assert node == nl0  # 10
    node = node.next
    assert node == nl1  # 20
    node = node.next
    assert node == nl2  # 30
    node = node.next
    assert node == nl3  # 40
    node = node.next
    assert node is None

    node = right.head
    assert node == nr0  # 42
    node = node.next
    assert node == nr1  # 42
    node = node.next
    assert node == nr2  # 42
    node = node.next
    assert node is None


if __name__ == '__main__':
    main()
