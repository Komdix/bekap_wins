from ib111 import week_05  # noqa


# Vaším prvním úkolem je napsat predikát ‹sum_to_exactly›, který
# rozhodne, zda se v seznamu ‹left› nachází nějaký prvek ‹x› a
# v seznamu ‹right› nějaký prvek ‹y› tak, že platí ‹x + y == to›.

# Řešení, kde bude počet kroků výpočtu úměrný součinu délek obou
# seznamů, je vyhovující.¹

def sum_to_exactly(left: list[int], right: list[int], to: int) -> bool:
    pass


# Dále napište predikát ‹sum_to_at_least›, který rozhodne, zda se
# v seznamu ‹left› nachází nějaký prvek ‹x› a v seznamu ‹right›
# nějaký prvek ‹y› tak, že platí ‹x + y >= to›. V tomto případě
# vyžadujeme složitost lineární vzhledem k délce delšího seznamu.

def sum_to_at_least(left: list[int], right: list[int], at_least: int) -> bool:
    pass


# ¹ Existuje lepší řešení tohoto příkladu se složitostí ⟦n⋅log n⟧
#   vzhledem k délce většího seznamu. Toto řešení ale vyžaduje
#   seřazení seznamů.

def main() -> None:
    l1: list[int] = []
    l2 = [1, 20, 1, 3, -32, 5, 12, 4, 2, 33]
    l3 = [3, 232, 5, 2, 45, 34, 22, 4, 44]

    # na rozumném počítači by všechny testy měly proběhnout
    # během pár sekund, má-li vaše řešení správnou složitost
    huge = [i for i in range(500000)]

    assert sum_to_exactly(l2, l3, 77)
    assert sum_to_exactly(l2, l3, 200)
    assert sum_to_exactly(huge, l2, 30)
    assert sum_to_exactly(l2, huge, 109090)
    assert not sum_to_exactly(l1, l2, 32)
    assert not sum_to_exactly(l2, l3, 150)
    assert not sum_to_exactly(huge, l2, 2000000)

    assert sum_to_at_least(l2, l3, 240)
    assert sum_to_at_least(huge, l2, 1000)
    assert sum_to_at_least(l3, huge, 400000)
    assert sum_to_at_least(huge, huge, 400000)
    assert not sum_to_at_least(l2, l3, 1000)
    assert not sum_to_at_least(l1, l3, 20)
    assert not sum_to_at_least(l2, l1, 20)
    assert not sum_to_at_least(huge, huge, 3000000)


if __name__ == "__main__":
    main()
