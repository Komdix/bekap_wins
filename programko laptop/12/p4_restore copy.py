from ib111 import week_12  # noqa


# Napište čistou funkci ‹restore_sequence›, která dostane neprázdný řetězec
# složený pouze z číslic 0 a 1 a vrátí množinu všech možných
# řetězců, které vzniknou doplněním znaků čárky ‹','› do původního
# řetězce tak, aby části jimi oddělené byly dvojkové zápisy čísel
# v intervalu od ‹low› do ‹high› včetně. Hodnota ‹low› bude vždy
# alespoň 1. Rozdělení musí být takové, že žádný zápis neobsahuje
# levostranné nuly.
def str_to_int(s: str):
    integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for integer in integers:
        if integer == s:
            return integers.index(integer)
    return None

def binary_str_to_int(binary_str: str) -> int:
    """ Convert a binary string to an integer. """
    result = 0
    for char in binary_str:
        result = result * 2 + (str_to_int(char) if char in ['0', '1'] else 0)
    return result

# Updating is_valid function accordingly
def is_valid(binary_str: str, low: int, high: int) -> bool:
    """ Check if the binary string is a valid number in the range and without leading zeros. """
    if not binary_str or (binary_str[0] == '0' and binary_str != "0"):
        return False
    num = binary_str_to_int(binary_str)
    return low <= num <= high


def backtrack(index: int, current: str, path: str, digits: str, low: int, high: int, results: set[str]) -> None:
    """ Use backtracking to find all valid sequences. """
    if index == len(digits):
        if current == "" or is_valid(current, low, high):
            results.add(path)
        return

    # Continue without adding a comma
    backtrack(index + 1, current + digits[index], path + digits[index], digits, low, high, results)

    # Try adding a comma here if current segment is valid and recurse
    if is_valid(current, low, high):
        next_path = path + ',' if path else path
        backtrack(index + 1, digits[index], next_path + digits[index], digits, low, high, results)


def restore_sequence(digits: str, low: int, high: int) -> set[str]:
    results = set()
    backtrack(1, digits[0], digits[0], digits, low, high, results)
    return results


def main() -> None:
    assert restore_sequence("1111", 2, 3) == {"11,11"}
    assert restore_sequence("11110", 1, 6) == \
        {"1,1,1,10", "11,1,10", "11,110", "1,1,110", "1,11,10"}
    assert restore_sequence("1111", 100, 200) == set()
    assert restore_sequence("101010", 2, 10) \
        == {"10,10,10", "10,1010", "1010,10"}
    assert restore_sequence("1001", 1, 30) == {"1001", "100,1"}
    assert restore_sequence("111101111", 0b101, 0b111) == {"111,101,111"}
    assert restore_sequence("1110101", 1, 9) == {
        "1,1,10,101",
        "11,10,101",
        "11,10,10,1",
        "1,110,101",
        "1,110,10,1",
        "1,1,10,10,1",
    }


if __name__ == '__main__':
    main()
