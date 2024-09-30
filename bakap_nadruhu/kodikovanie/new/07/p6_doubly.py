from ib111 import week_07  # noqa


# † V této úloze budeme programovat dvojitě zřetězený seznam, který se
# podobá jednoduše zřetězenému seznamu, který již dobře znáte. Jak
# napovídá už název, každý uzel bude připojen do řetězu na obě
# strany, tzn. krom následovníka si bude pamatovat i svého
# předchůdce.

# Oproti seznamu zřetězenému jednoduše se v tom dvojitém lépe
# odebírají prvky: z libovolného místa seznamu (tedy zejména na obou
# koncích) lze totiž odebrat prvek bez toho, abychom museli seznam
# jakkoliv procházet. A proto i Vaše implementace uvedených metod
# (kromě ‹search›) by měla fungovat bez jakéhokoliv procházení seznamu.

class Node:
    def __init__(self, init_val: int) -> None:
        self.value = init_val
        self.next: Node | None = None
        self.prev: Node | None = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    # Metoda ‹append› přidá novou hodnotu na konec seznamu.

    def append(self, value: int) -> None:
        pass

    # Metoda ‹prepend› naopak vloží novou hodnotu na začátek. Na
    # rozdíl od zabudovaného typu ‹list› je toto v principu levná
    # operace.

    def prepend(self, value: int) -> None:
        pass

    # Metoda ‹remove› odstraní ze seznamu libovolný uzel.

    def remove(self, node: Node) -> None:
        pass

    # Konečně metoda ‹search› najde první uzel s danou hodnotu.
    # Když takový uzel neexistuje, vrátí ‹None›.

    def search(self, value: int) -> Node | None:
        pass


def main() -> None:
    test_insertion()
    test_remove()


def remove(d_list: DoubleLinkedList, value: int) -> None:
    node = d_list.search(value)
    assert node is not None
    d_list.remove(node)
    assert d_list.search(value) is None


def test_remove() -> None:
    elems = [4, 2, 6, 8, -3, 11]
    for chosen in elems:
        d_list = DoubleLinkedList()
        for elem in elems:
            d_list.append(elem)

        remove(d_list, chosen)

        for elem in elems:
            if elem != chosen:
                assert d_list.search(elem) is not None

    d_list = DoubleLinkedList()
    for elem in elems:
        d_list.append(elem)

    for elem in elems:
        remove(d_list, elem)

    for elem in elems:
        assert d_list.search(elem) is None


def test_insertion() -> None:
    d_list = DoubleLinkedList()
    for i in [1, 3, 17, 11, 7, 9]:
        d_list.append(i)
        d_list.prepend(i - 1)
    assert d_list.search(1) is not None
    assert d_list.search(4) is None
    assert d_list.search(14) is None

    node = d_list.search(11)
    assert node is not None
    assert node.value == 11

    assert node.prev is d_list.search(17)
    assert node.next is d_list.search(7)

    node = d_list.search(3)
    assert node is not None
    assert node.next is d_list.search(17)

    head, tail = d_list.head, d_list.tail
    assert tail is not None
    assert head is not None
    node = head.next
    assert node is not None

    assert d_list.search(7) is tail.prev
    assert d_list.search(8) is head
    assert d_list.search(6) is head.next
    assert d_list.search(10) is node.next


if __name__ == "__main__":
    main()
