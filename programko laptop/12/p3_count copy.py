from ib111 import week_12  # noqa


# Napište funkci ‹count_seq›, která nad desítkovou reprezentací
# čísla ‹num› provede následující výpočet:

#  1. vybere všechny cifry, po kterých následuje alespoň ‹seq›
#     stejných cifer; pro účely této kontroly chápeme ‹num›
#     cyklicky, tzn. po poslední cifře následuje opět první,
#  2. vybrané cifry sečte a součet vrátí.

# Cykličnost v bodě 1 můžeme chápat jako nekonečné opakování ‹num›,
# např. v čísle 123 následují po cifře 2 cifry 3, 1, 2, 3, 1, atd.

# Příklady výpočtu:

#  • pro ‹num=111222› a ‹seq=2› je výsledkem 3 (1 + 2), protože po
#    první (1) a čtvrté (2) cifře následují 2 stejné cifry,
#  • pro ‹num=1111› a ‹seq=1› je výsledkem 4, protože po každé cifře
#    následuje alespoň jedna stejná cifra,
#  • pro ‹num=1234› a ‹seq=0› je výsledkem součet všech číslic,
#    totiž 10.
def int_to_str(num: int) -> str | None:
    integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        result += integers[num % 10]
        num //= 10

    return result
def str_to_int(s: str) -> int | None:
    integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for integer in integers:
        if integer == s:
            return integers.index(integer)
    return None

def count_seq(num: int, seq: int) -> int:
    num_str = int_to_str(num)
    length = len(num_str)
    total = 0

    for i in range(length):
        match_count = 0
        current_digit = num_str[i]

        # Check the next 'seq' digits
        for j in range(1, seq + 1):
            # Use modulus to cycle through the number
            next_index = (i + j) % length
            if num_str[next_index] == current_digit:
                match_count += 1
            else:
                break

        # Add to total if the condition is met
        if match_count == seq:
            total += str_to_int(current_digit)

    return total


def main() -> None:
    assert count_seq(1122, 1) == 3
    assert count_seq(111222, 2) == 3
    assert count_seq(1111, 1) == 4
    assert count_seq(1111, 3) == 4
    assert count_seq(1111, 20) == 4
    assert count_seq(1234, 1) == 0
    assert count_seq(41214, 1) == 4
    assert count_seq(1234, 0) == 10
    assert count_seq(412213334, 1) == 12
    assert count_seq(110002331, 2) == 1
    assert count_seq(222220, 4) == 2
    assert count_seq(222022, 3) == 4
    assert count_seq(41214, 0) == 12
    assert count_seq(818275977931166178424892653779931348, 1) == 38
    assert count_seq(882227597793116661784248926663779931348, 2) == 22
    assert count_seq(818275977931166178424892653779931348, 0) == 190


if __name__ == "__main__":
    main()
