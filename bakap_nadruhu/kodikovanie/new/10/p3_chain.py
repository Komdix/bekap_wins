from ib111 import week_10  # noqa


# Napište predikát, který dostane na vstupu množinu čísel ⟦M⟧ a
# délku ⟦n⟧ a rozhodne, existuje-li navazující posloupnost čísel
# délky právě ⟦n⟧. Navazující posloupnost je taková, kde každé další
# číslo začíná v jedenáctkovém zápisu stejnou číslicí, jakou končí
# předchozí. Čísla se v posloupnosti nesmí opakovat.

def elven_chain(numbers: set[int], length: int) -> bool:
    pass


def main() -> None:
    assert elven_chain(set(), 0)
    assert elven_chain({1}, 1)
    assert elven_chain({146, 12}, 2)
    assert elven_chain({146, 23}, 2)
    assert not elven_chain({146, 11}, 2)
    assert not elven_chain({146, 13}, 2)
    assert not elven_chain({2, 13}, 3)

    numbers = {146, 12}
    assert elven_chain(numbers, 2)
    assert numbers == {146, 12}


if __name__ == '__main__':
    main()
