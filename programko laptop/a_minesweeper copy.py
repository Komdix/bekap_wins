
Position = tuple[int, int]

UNKNOWN = -1
EXPLODED = -2
DESTROYED = -3


class Minesweeper:

    def __init__(self, width: int, height: int,
                 mines: dict[Position, int]):
        self.width = width
        self.height = height
        self.mines = mines.copy()
        self.score = 0
        self.status = [[UNKNOWN for _ in range(width)] for _ in range(height)]
        self.known: set[Position] = set()


    def uncover(self, x: int, y: int) -> None:
        status = self.status[y][x]
        if status != UNKNOWN:
            return None
        if (x, y) in self.known:
            return None
        if (x, y) in self.mines:
            self.explode(x, y, self.mines[(x, y)])
        else:
            self.score += 1
            count = self.mines_around(x, y)
            self.status[y][x] = count
            self.known.add((x, y))
            if count == 0:
                self.uncover_neighbors(x, y)
            return None
        return None


    def cords_add(x, y, add_x, add_y):
        if add_x == 0 and add_y == 0:
            return
        new_x = x + add_x
        new_y = y + add_y


    def mines_around(self, x: int, y: int) -> int:
        count = 0
        for add_x in [-1, 0, 1]:
            for add_y in [-1, 0, 1]:
                if add_x == 0 and add_y == 0:
                    continue
                new_x = x + add_x
                new_y = y + add_y
                if 0 <= new_x < self.width and 0 <= new_y < self.height and \
                    (new_x, new_y) in self.mines:
                        count += 1
        return count

    def uncover_neighbors(self, x: int, y: int) -> None:
        for add_x in [-1, 0, 1]:
            for add_y in [-1, 0, 1]:
                if add_x == 0 and add_y == 0:
                    continue
                new_x = x + add_x
                new_y = y + add_y
                if 0 <= new_x < self.width and 0 <= new_y < self.height and \
                    (new_x, new_y) not in self.known:
                        self.score += 1
                        count = self.mines_around(new_x, new_y)
                        self.status[new_y][new_x] = count
                        self.known.add((new_x, new_y))

                        if count == 0:
                            self.uncover_neighbors(new_x, new_y)

    def explode(self, x: int, y: int, power: int) -> None:
        self.score -= 10
        self.status[y][x] = EXPLODED
        self.known.add((x, y))

        for add_x in range(- power, power + 1):
            for add_y in range(- power, power + 1):
                new_x = x + add_x
                new_y = y + add_y

                if 0 <= new_x < self.width and 0 <= new_y < self.height:
                    if (new_x, new_y) not in self.known and \
                        (new_x, new_y) in self.mines:
                            self.known.add((new_x, new_y))
                            self.explode(new_x, new_y, self.mines[(new_x,
                                                                   new_y)])
                    if self.status[new_y][new_x] != EXPLODED:
                        self.known.add((new_x, new_y))
                        self.status[new_y][new_x] = DESTROYED


def main() -> None:
    U, E, D = UNKNOWN, EXPLODED, DESTROYED
    mines = {(2, 2): 5, (4, 5): 1, (6, 1): 0, (6, 3): 1, (6, 4): 3}

    ms = Minesweeper(8, 6, mines)
    assert ms.score == 0
    assert ms.status == [
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
    ]

    ms.uncover(1, 1)
    assert ms.score == 1
    assert ms.status == [
        [U, U, U, U, U, U, U, U],
        [U, 1, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
    ]

    ms.uncover(0, 0)
    assert ms.score == 33
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, 1, 0, 1, U, U],
        [0, 1, U, 1, 0, 2, U, U],
        [0, 1, 1, 1, 0, 2, U, U],
        [0, 0, 0, 1, 1, 3, U, U],
        [0, 0, 0, 1, U, U, U, U],
    ]

    ms.uncover(5, 4)
    assert ms.score == 33
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, 1, 0, 1, U, U],
        [0, 1, U, 1, 0, 2, U, U],
        [0, 1, 1, 1, 0, 2, U, U],
        [0, 0, 0, 1, 1, 3, U, U],
        [0, 0, 0, 1, U, U, U, U],
    ]

    ms.uncover(4, 5)
    assert ms.score == 23
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, 1, 0, 1, U, U],
        [0, 1, U, 1, 0, 2, U, U],
        [0, 1, 1, 1, 0, 2, U, U],
        [0, 0, 0, D, D, D, U, U],
        [0, 0, 0, D, E, D, U, U],
    ]
    ms.uncover(5, 5)
    assert ms.score == 23
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, 1, 0, 1, U, U],
        [0, 1, U, 1, 0, 2, U, U],
        [0, 1, 1, 1, 0, 2, U, U],
        [0, 0, 0, D, D, D, U, U],
        [0, 0, 0, D, E, D, U, U],
    ]

    ms.uncover(6, 3)
    assert ms.score == -7
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, D, D, D, E, D],
        [0, 1, U, D, D, D, D, D],
        [0, 1, 1, D, D, D, E, D],
        [0, 0, 0, D, D, D, E, D],
        [0, 0, 0, D, E, D, D, D],
    ]

    assert mines == {(2, 2): 5, (4, 5): 1, (6, 1): 0, (6, 3): 1, (6, 4): 3}


if __name__ == '__main__':
    main()