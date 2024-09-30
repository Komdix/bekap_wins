from ib111 import week_07  # noqa


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


# Napište čistou funkci, která sestaví zřetězený seznam, který bude
# obsahovat hodnoty, které se nachází ve vstupním seznamu na
# zadaných indexech. Pořadí hodnot zachovejte. Předpokládejte, že
# indexy v seznamu ‹indices› jsou platné a vzestupně seřazené.
# K implementaci této funkce Vám stačí jeden průchod seznamy
# ‹indices› a ‹linked›.

def select(indices: list[int], linked: LinkedList) -> LinkedList:
    pass


def main() -> None:
    assert select_test([], [], [])
    assert select_test([], [1, 2, 3], [])
    assert select_test([0, 2], [1, 2, 3], [1, 3])
    assert select_test([1], [1, 2, 3], [2])
    assert select_test([0, 1, 2], [1, 2, 3], [1, 2, 3])
    assert select_test([0, 2], [-1, -2, 3], [-1, 3])
    assert select_test([0, 2], [1, 2, 3], [1, 3])
    assert select_test([0, 3, 4], [0, 1, 2, 3, 4], [0, 3, 4])
    assert select_test([0, 1], [1, 2, 3], [1, 2])


def build_linked(nums: list[int]) -> LinkedList:
    result = LinkedList()

    if len(nums) == 0:
        return result

    result.head = Node(nums[0])
    tail = result.head

    for i in range(1, len(nums)):
        tail.next = Node(nums[i])
        tail = tail.next

    return result


def check_list_content(to_check: LinkedList,
                       expected_content: list[int]) -> bool:
    curr_idx = 0
    curr_node = to_check.head

    while curr_node is not None:
        if len(expected_content) == curr_idx:
            return False

        if curr_node.value != expected_content[curr_idx]:
            return False

        curr_node = curr_node.next
        curr_idx += 1

    return len(expected_content) == curr_idx


def select_test(chosen_idxs: list[int],
                list_nums: list[int],
                expected_content: list[int]) -> bool:
    test_list = build_linked(list_nums)
    select_res = select(chosen_idxs, test_list)

    if not check_list_content(test_list, list_nums):
        return False

    return check_list_content(select_res, expected_content)


if __name__ == "__main__":
    main()
