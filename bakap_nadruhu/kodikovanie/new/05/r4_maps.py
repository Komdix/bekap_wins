from ib111 import week_05  # noqa


# V tomto příkladu budeme pracovat se slovníky. Slovník může mimo
# jiné reprezentovat zobrazení: klíč se zobrazí na příslušnou
# hodnotu. Naprogramujte čistou funkci ‹image›, které předáme
# slovník ‹f›, který reprezentuje zobrazení, a množinu ‹values›.
# Výsledkem bude obraz množiny ‹values› – tedy množina hodnot, na
# které se hodnoty z množiny ‹values› zobrazí.

def image(f: dict[int, int], values: set[int]) -> set[int]:
    pass


# Podobně funkce ‹preimage› spočítá vzor zadané množiny ‹values›
# (množinu hodnot, které ‹f› zobrazí na některý prvek množiny
# ‹values›):

def preimage(f: dict[int, int], values: set[int]) -> set[int]:
    pass


# Dále naprogramujte čistou funkci ‹compose›, které vstupem budou
# dvě zobrazení (slovníky) ‹f› a ‹g› a výsledkem bude slovník, který
# reprezentuje zobrazení ‹f ∘ g›. Vstupní podmínkou je, že ‹f› je
# definováno pro každou hodnotu z obrazu ‹g›.


def compose(f: dict[int, int], g: dict[int, int]) -> dict[int, int]:
    pass


# Konečně naprogramujte čistou funkci ‹kernel›, které vstupem bude
# zobrazení (slovník) ‹f› a výsledkem bude relace ekvivalence ⟦R⟧
# (množina dvojic) taková, že ⟦(x, y) ∈ R⟧ právě když ⟦f(x) = f(y)⟧.


def kernel(f: dict[int, int]) -> set[tuple[int, int]]:
    pass


def main() -> None:
    f = {1: 1, 2: 2}
    g = {1: 2, 2: 1}
    h = {1: 2, 2: 2}

    assert image(f, {1}) == {1}
    assert image(g, {1}) == {2}
    assert image(h, {1, 2}) == {2}

    assert preimage(f, {1}) == {1}
    assert preimage(f, {1, 2}) == {1, 2}
    assert preimage(g, {1}) == {2}
    assert preimage(h, {2}) == {1, 2}

    assert compose(f, g) == g
    assert compose(g, f) == g
    assert compose(h, g) == h
    assert compose(h, h) == h
    assert compose(g, g) == f

    assert kernel(f) == {(1, 1), (2, 2)}
    assert kernel(g) == {(1, 1), (2, 2)}
    assert kernel(h) == {(1, 1), (2, 2), (1, 2), (2, 1)}

    f = {1: 1, 2: 1, 3: 2}
    assert kernel(f) == {(1, 1), (2, 2), (3, 3),
                         (1, 2), (2, 1)}


if __name__ == '__main__':
    main()
