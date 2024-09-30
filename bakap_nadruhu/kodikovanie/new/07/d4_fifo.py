from ib111 import week_07  # noqa


# V této ukázce budeme implementovat (tentokrát neomezenou) frontu
# pomocí zřetězeného seznamu. Třída ‹Node› bude sloužit jako jeden
# uzel fronty:

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


# Třída ‹Queue› bude implementovat běžné rozhraní fronty (‹push›,
# ‹pop›) a data bude ukládat do jednoho spojitého řetězu uzlů
# (instancí třídy ‹Node›).

# Hlavu tohoto řetězu (tzn. takový uzel, z kterého lze dojít do
# všech ostatních uzlů) uložíme do atributu ‹chain›. Řetěz bude mít
# právě tolik prvků, kolik jich je uloženo ve frontě a bude ukončen
# uzlem, který má ‹next› nastavený na ‹None›. Výjimku tvoří případ,
# kdy je fronta prázdná, kdy není hodnota ‹chain› vůbec určena.

class Queue:
    def __init__(self) -> None:
        self.chain: Node | None = None
        self.insert: Node | None = None

    def push(self, value: int) -> None:
        if self.insert is None:
            self.chain = self.insert = Node(value)
        else:
            self.insert.next = Node(value)
            self.insert = self.insert.next

    def pop(self) -> int | None:
        if self.chain is None:
            return None

        value = self.chain.value
        self.chain = self.chain.next
        if self.chain is None:
            self.insert = None
        return value


# Všimněte si, že správně implementovaná fronta při žádné operaci
# «neprochází» zřetězený seznam, kterým je reprezentovaná.
# V přiložených testech si demonstrujeme zejména to, že fronta bude
# funkční i v situaci, kdy ji uměle uprostřed „rozpojíme“ –
# samozřejmě jen do chvíle, než by se takové rozpojení dostalo do
# hlavy fronty.

def main() -> None:  # demo
    queue = Queue()
    queue.push(1)
    check_count(queue, 1)
    check_value(queue.pop(), 1)
    assert queue.pop() is None
    queue.push(3)
    queue.push(5)
    queue.push(7)
    check_count(queue, 3)
    assert queue.chain is not None
    assert queue.chain.value == 3

    assert queue.chain is not None
    broken = queue.chain.next
    assert broken is not None
    lost = broken.next
    assert lost is not None
    broken.next = None

    queue.push(8)
    queue.push(9)
    check_value(queue.pop(), 3)
    broken.next = lost
    check_value(queue.pop(), 5)
    check_value(queue.pop(), 7)
    check_value(queue.pop(), 8)
    check_value(queue.pop(), 9)
    assert queue.pop() is None


def check_count(queue: Queue, count: int) -> None:
    node = queue.chain
    while node:
        node = node.next
        count -= 1
    assert count == 0


def check_value(value: int | None, expect: int) -> None:
    assert value is not None
    assert value == expect


if __name__ == '__main__':
    main()
