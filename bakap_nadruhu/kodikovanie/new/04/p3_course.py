from ib111 import week_04  # noqa

# V této úloze bude Vaším úkolem implementovat a otypovat
# následující funkce, které implementují dotazy na školní kurzy.
# Kurz je reprezentován seznamem dvojic (student, známka), přičemž
# student je trojice (učo, jméno, semestr) a známka je řetězec
# z rozsahu ‹A› až ‹F›.


# Funkce ‹failed› vrátí seznam studentů kurzu ‹course›, kteří z něj
# mají známku ‹F›.

def failed(course):
    pass


# Funkce ‹count_passed› vrátí počet studentů, kteří úspěšně ukončili
# kurz ‹course›, tedy z něj nemají známku ‹F›. Parametr ‹semester›
# je volitelný: je-li specifikován (není ‹None›), funkce vrátí počet
# úspěšných studentů v daném semestru, jinak vrátí počet všech
# úspěšných studentů.

def count_passed(course, semester):
    pass


# Funkce ‹student_grade› vrátí známku studenta s učem ‹uco›. Pokud
# takový student v kurzu ‹course› není, vrací ‹None›.

def student_grade(uco, course):
    pass


def main() -> None:
    s1 = (311799, "Dennis Ritchie", 1)
    s2 = (121436, "George Boole", 3)
    s3 = (463522, "Ada Lovelace", 3)
    s4 = (336100, "Alonzo Church", 2)
    s5 = (378500, "Noam Chomsky", 1)
    s6 = (473521, "Donald Knuth", 1)

    ib111 = [(s1, "F"), (s2, "A"), (s4, "E"), (s6, "F")]
    ib001 = [(s2, "D"), (s4, "C"), (s3, "F"), (s5, "D"), (s6, "B")]
    ib002 = [(s6, "A"), (s1, "B"), (s3, "A"), (s4, "C"), (s5, "A")]

    failed_ib111 = failed(ib111)
    failed_ib001 = failed(ib001)

    # Test failed
    assert failed_ib111 == [s1, s6] or failed_ib111 == [s6, s1]
    assert failed_ib001 == [s3]
    assert failed(ib002) == []

    # Test count_passed
    assert count_passed(ib111, None) == 2
    assert count_passed(ib001, None) == 4
    assert count_passed(ib002, None) == 5
    assert count_passed(ib002, 1) == 3
    assert count_passed(ib001, 3) == 1
    assert count_passed(ib111, 3) == 1

    # Test student_grade
    assert student_grade(311799, ib111) == "F"
    assert student_grade(311799, ib001) is None
    assert student_grade(311799, ib002) == "B"
    assert student_grade(463522, ib111) is None
    assert student_grade(463522, ib001) == "F"
    assert student_grade(463522, ib002) == "A"
    assert student_grade(473521, ib111) == "F"
    assert student_grade(473521, ib001) == "B"


if __name__ == "__main__":
    main()
