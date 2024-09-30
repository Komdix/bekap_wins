from ib111 import week_07, except_data_structures  # noqa


# V této úloze budete implementovat jednoduchý zřetězený seznam
# s dodatečnou vlastností, že jeho prvky jsou vždy vzestupně
# seřazené.

# Třída ‹Node› reprezentuje jeden uzel seznamu, a má dva atributy:
# hodnotu typu ‹int› a odkaz na další uzel ‹next›.
# Tuto třídu nijak nemodifikujte.

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


# Následující třída reprezentuje seřazený, zřetězený seznam.
# Implementujte naznačené metody ‹insert› a ‹get_greatest_in›.
#
# V tomto příkladu je zakázáno použití Pythonovských datových struktur
# seznam, množina, slovník.

class SortedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    # Metoda ‹insert› vloží do seznamu nový prvek. Nezapomeňte, že
    # seznam musí být vždy seřazený. Metoda by měla projít celý seznam
    # nejvíce jednou.

    def insert(self, value: int) -> None:
        pass

    # Následující metoda vrátí největší prvek seznamu, jehož hodnoty
    # spadají do oboustranně uzavřeného intervalu [‹value›, ‹value› + ‹dist›].
    # Pokud žádný takový prvek není, vrátí ‹None›.
    # V případech, kdy se tomu lze vyhnout, neprocházejte seznam zbytečně celý.

    def get_greatest_in(self, value: int, dist: int) -> int | None:
        pass


def main() -> None:
    test_insert()
    test_get()


def test_get() -> None:
    s_list = SortedList()
    assert s_list.get_greatest_in(0, 1000) is None
    s_list.insert(1)
    assert s_list.get_greatest_in(0, 10) == 1
    assert s_list.get_greatest_in(0, 0) is None
    assert s_list.get_greatest_in(1, 0) == 1
    s_list.insert(15)
    assert s_list.get_greatest_in(0, 10) == 1
    s_list.insert(5)
    assert s_list.get_greatest_in(0, 10) == 5
    assert s_list.get_greatest_in(0, 15) == 15

    for num in [12, 56, 21, 43]:
        s_list.insert(num)

    assert s_list.get_greatest_in(10, 25) == 21
    assert s_list.get_greatest_in(10, 10) == 15
    assert s_list.get_greatest_in(10, 2) == 12
    assert s_list.get_greatest_in(10, 0) is None


def test_insert() -> None:
    s_list = SortedList()
    s_list.insert(4)
    assert s_list.head is not None
    assert s_list.head.value == 4
    s_list.insert(5)
    assert s_list.head.value == 4
    assert s_list.head.next is not None
    assert s_list.head.next.value == 5
    s_list.insert(3)
    assert s_list.head.value == 3
    assert s_list.head.next.value == 4
    assert s_list.head.next.next is not None
    assert s_list.head.next.next.value == 5

    s_list = SortedList()
    assert s_list.head is None
    s_list.insert(1)
    s_list.insert(0)
    s_list.insert(-1)
    s_list.insert(5)
    assert s_list.head is not None
    assert s_list.head.value == -1
    assert s_list.head.next is not None
    assert s_list.head.next.value == 0
    assert s_list.head.next.next is not None
    assert s_list.head.next.next.value == 1
    assert s_list.head.next.next.next is not None
    assert s_list.head.next.next.next.value == 5


if __name__ == "__main__":
    main()
