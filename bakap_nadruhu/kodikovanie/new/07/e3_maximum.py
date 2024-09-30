from ib111 import week_07  # noqa


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


# Napište čistou funkci, která najde největší hodnotu uloženou ve
# vstupním zřetězeném seznamu, případně ‹None› je-li vstupní seznam
# prázdný.

def maximum(num_list: LinkedList) -> int | None:
    pass


def main() -> None:
    test_list = LinkedList()
    assert maximum(test_list) is None
    test_list.head = Node(5)
    assert maximum(test_list) == 5
    test_list.head.next = Node(3)
    assert maximum(test_list) == 5
    test_list.head.next.next = Node(10)
    assert maximum(test_list) == 10
    test_list.head.next.next.next = Node(3)
    assert maximum(test_list) == 10
    test_list.head = Node(-5)
    assert maximum(test_list) == -5
    test_list.head.next = Node(-5)
    assert maximum(test_list) == -5
    test_list.head.next.next = Node(0)
    assert maximum(test_list) == 0


if __name__ == "__main__":
    main()
