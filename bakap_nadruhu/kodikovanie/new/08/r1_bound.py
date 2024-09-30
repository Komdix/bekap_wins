from ib111 import week_08  # noqa


# Implementujte funkci ‹left_bound›, která ve vzestupně seřazeném
# seznamu ‹values› co nejefektivněji najde index prvního výskytu
# hodnoty ‹target›. Pokud se hodnota v seznamu nenachází, vrátí
# ‹None›. V této úloze je lineární řešení neefektivní.

def left_bound(values: list[int], target: int) -> int | None:
    pass


def main() -> None:
    assert left_bound([1, 2, 3, 4, 5], 2) == 1
    assert left_bound([1, 2, 2, 2, 2], 2) == 1
    assert left_bound([2, 2, 2, 2, 2], 2) == 0
    assert left_bound([2, 2, 2, 2, 3], 2) == 0
    assert left_bound([1, 2, 3, 4, 5], 5) == 4
    assert left_bound([1, 2, 3, 4, 5], 7) is None


if __name__ == "__main__":
    main()
