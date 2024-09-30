from ib111 import week_07, except_data_structures  # noqa


# Tyto třídy pro reprezentaci zřetězeného seznamu máte již připraveny.
# Nijak je nemodifikujte.

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


# Napište čistou funkci ‹filter_linked›, která vytvoří nový
# zřetězený seznam, který vznikne z toho vstupního (‹num_list›)
# vynecháním všech uzlů s hodnotou menší než ‹lower_bound›.
# Pro naprogramování této funkce Vám postačuje jeden průchod vstupním seznamem.
#
# V tomto příkladu je zakázáno použití Pythonovských datových struktur
# seznam, množina, slovník.

def filter_linked(lower_bound: int,
                  num_list: LinkedList) -> LinkedList:
    pass


def main() -> None:
    # llist: empty
    llist = LinkedList()

    result = filter_linked(0, llist)

    node = result.head
    assert node is None

    # llist: 1 -> 1
    n1 = Node(1)
    n0 = Node(1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = filter_linked(0, llist)

    node = llist.head
    assert node == n0  # 1
    node = node.next
    assert node == n1  # 1
    node = node.next
    assert node is None

    node = result.head
    assert node is not None
    assert node.value == 1
    node = node.next
    assert node is not None
    assert node.value == 1
    node = node.next
    assert node is None

    # llist: -1 -> 1 -> -1
    n2 = Node(-1)
    n1 = Node(1)
    n1.next = n2
    n0 = Node(-1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = filter_linked(0, llist)

    node = result.head
    assert node is not None
    assert node.value == 1
    node = node.next
    assert node is None

    # llist: 0 -> 0 -> 0
    n2 = Node(0)
    n1 = Node(0)
    n1.next = n2
    n0 = Node(0)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = filter_linked(1, llist)

    node = llist.head
    assert node == n0  # 0
    node = node.next
    assert node == n1  # 0
    node = node.next
    assert node == n2  # 0
    node = node.next
    assert node is None

    node = result.head
    assert node is None

    # llist: -1 -> 1 -> -2 -> 2 -> -3 -> 0
    n5 = Node(0)
    n4 = Node(-3)
    n4.next = n5
    n3 = Node(2)
    n3.next = n4
    n2 = Node(-2)
    n2.next = n3
    n1 = Node(1)
    n1.next = n2
    n0 = Node(-1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = filter_linked(1, llist)

    node = result.head
    assert node is not None
    assert node.value == 1
    node = node.next
    assert node is not None
    assert node.value == 2
    node = node.next
    assert node is None

    # llist: -2 -> -3 -> 0 -> 3
    n3 = Node(3)
    n2 = Node(0)
    n2.next = n3
    n1 = Node(-3)
    n1.next = n2
    n0 = Node(-2)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = filter_linked(1, llist)

    node = result.head
    assert node is not None
    assert node.value == 3
    node = node.next
    assert node is None

    # llist: 1024 -> -257
    n1 = Node(-257)
    n0 = Node(1024)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = filter_linked(2000, llist)

    node = result.head
    assert node is None

    # llist: -2 -> -3 -> 0 -> 3
    n3 = Node(3)
    n2 = Node(0)
    n2.next = n3
    n1 = Node(-3)
    n1.next = n2
    n0 = Node(-2)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    result = filter_linked(-2, llist)

    node = result.head
    assert node is not None
    assert node.value == -2
    node = node.next
    assert node is not None
    assert node.value == 0
    node = node.next
    assert node is not None
    assert node.value == 3
    node = node.next
    assert node is None


if __name__ == "__main__":
    main()
