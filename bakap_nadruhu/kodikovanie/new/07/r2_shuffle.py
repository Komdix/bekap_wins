from ib111 import week_07  # noqa


# Na vstupu dostanete (standardní Pythonovský) seznam čísel
# z rozsahu ⟦⟨0, n - 1⟩⟧ takový, že každé číslo se v něm vyskytuje
# právě jednou, a který tedy popisuje permutaci. Na každém indexu
# tohoto seznamu najdete číslo, na které se má daný index permutací
# zobrazit. Vaším úkolem je ve funkci ‹shuffle› tuto permutaci
# aplikovat na vstupní zřetězený seznam (t.j. upravit odpovídajícím
# způsobem pořadí jeho uzlů). Předpokládejte, že má právě ⟦n⟧ uzlů.
#
# Nevytvářejte při řešení nové uzly ani nemodifikujte hodnoty (atribut
# ‹value›) těch existujících. Funkce rovněž nesmí modifikovat vstupní
# Pythonovský seznam ‹permutation›.
#
# Příklad:
# Je-li zadaná permutace ⟦2, 0, 1⟧, přesune se prvek z pozice 0 na
# pozici 2, z pozice 1 na pozici 0 a ten z pozice 2 na pozici 1:
#
#  ┌───┐   ┌───┐   ┌───┐
#  │ a │──▶│ b │──▶│ c │
#  └───┘   └───┘   └───┘
#    ┆ ╭┄┄┄┄┄╯ ╭┄┄┄┄┄╯
#    ╰┄┼┄┄┄┄┄┄┄┼┄┄┄┄┄┄┄╮
#      ▼       ▼       ▼
#    ┌───┐   ┌───┐   ┌───┐
#    │ b │──▶│ c │──▶│ a │
#    └───┘   └───┘   └───┘
#
# Zadané třídy nijak nemodifikujte.
# Zamyslete se nad tím, jak to udělat efektivně. Pro správné
# řešení vám postačují dva přechody vstupním zřetězeným seznamem.

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


def shuffle(permutation: list[int], linked: LinkedList) -> None:
    pass


def main() -> None:
    llist = LinkedList()

    perm: list[int] = []
    shuffle(perm, llist)
    assert perm == []

    node = llist.head
    assert node is None

    # 1 -> 2
    n1 = Node(2)
    n0 = Node(1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    perm = [0, 1]
    shuffle(perm, llist)
    assert perm == [0, 1]

    node = llist.head
    assert node == n0  # 1
    node = node.next
    assert node == n1  # 2
    node = node.next
    assert node is None

    # 1 -> 2
    n1 = Node(2)
    n0 = Node(1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    perm = [1, 0]
    shuffle(perm, llist)
    assert perm == [1, 0]

    node = llist.head
    assert node == n1  # 2
    node = node.next
    assert node == n0  # 1
    node = node.next
    assert node is None

    # 1 -> 2 -> 3
    n2 = Node(3)
    n1 = Node(2)
    n1.next = n2
    n0 = Node(1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    perm = [2, 0, 1]
    shuffle(perm, llist)
    assert perm == [2, 0, 1]

    node = llist.head
    assert node == n1  # 2
    node = node.next
    assert node == n2  # 3
    node = node.next
    assert node == n0  # 1
    node = node.next
    assert node is None

    # 0 -> 1 -> 2
    n2 = Node(2)
    n1 = Node(1)
    n1.next = n2
    n0 = Node(0)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    perm = [1, 0, 2]
    shuffle(perm, llist)
    assert perm == [1, 0, 2]

    node = llist.head
    assert node == n1  # 1
    node = node.next
    assert node == n0  # 0
    node = node.next
    assert node == n2  # 2
    node = node.next
    assert node is None

    # 1 -> 2 -> 3 -> 4
    n3 = Node(4)
    n2 = Node(3)
    n2.next = n3
    n1 = Node(2)
    n1.next = n2
    n0 = Node(1)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    perm = [0, 2, 1, 3]
    shuffle(perm, llist)
    assert perm == [0, 2, 1, 3]

    node = llist.head
    assert node == n0  # 1
    node = node.next
    assert node == n2  # 3
    node = node.next
    assert node == n1  # 2
    node = node.next
    assert node == n3  # 4
    node = node.next
    assert node is None

    # -1
    n0 = Node(-1)
    llist = LinkedList()
    llist.head = n0

    perm = [0]
    shuffle(perm, llist)
    assert perm == [0]

    node = llist.head
    assert node == n0  # -1
    node = node.next
    assert node is None

    # 0 -> 1 -> 2 -> 3 -> 4
    n4 = Node(4)
    n3 = Node(3)
    n3.next = n4
    n2 = Node(2)
    n2.next = n3
    n1 = Node(1)
    n1.next = n2
    n0 = Node(0)
    n0.next = n1
    llist = LinkedList()
    llist.head = n0

    perm = [1, 0, 4, 2, 3]
    shuffle(perm, llist)
    assert perm == [1, 0, 4, 2, 3]

    node = llist.head
    assert node == n1  # 1
    node = node.next
    assert node == n0  # 0
    node = node.next
    assert node == n3  # 3
    node = node.next
    assert node == n4  # 4
    node = node.next
    assert node == n2  # 2
    node = node.next
    assert node is None


if __name__ == "__main__":
    main()
