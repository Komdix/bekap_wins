from random import randint
import tkinter as tk

# change d_life below if your file name is different
import d_life as student

# game parameters; feel free to change them
WIDTH, HEIGHT = 1200, 1000  # pixels
CELL_SIZE = 10  # pixels
DELAY = 100  # ms

XMID, YMID = (WIDTH - CELL_SIZE) // 2, (HEIGHT - CELL_SIZE) // 2

COLOURS = [
    'lime',  # poison positions
    'blue',
    'orange',
    '#696969',
    '#7e7e7e',
    '#949494',
    '#a9a9a9',
]

Position = tuple[int, int]
State = dict[Position, int]


def init() -> tuple[State, set[Position]]:
    # if a specific initial state is desired, change this
    # note that (0, 0) is approximately in the middle of the window

    # by default, we create some random cells
    cols = WIDTH // CELL_SIZE
    rows = HEIGHT // CELL_SIZE

    xmin, xmax = -cols // 2 + 10, cols // 2 - 10
    ymin, ymax = -rows // 2 + 10, rows // 2 - 10

    state = {}
    for _ in range((xmax - xmin) * (ymax - ymin) // 2):
        x = randint(xmin, xmax)
        y = randint(ymin, ymax)
        state[x, y] = randint(1, 2)

    poison = set()
    for _ in range(10):
        poison.add((randint(xmin, xmax), randint(ymin, ymax)))

    return state, poison


class Game:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.state, self.poison = init()
        self.refresh()

    def draw_cell(self, x: int, y: int, c: int) -> None:
        self.canvas.create_rectangle(
            XMID + x * CELL_SIZE, YMID + y * CELL_SIZE,
            XMID + (x + 1) * CELL_SIZE, YMID + (y + 1) * CELL_SIZE,
            fill=COLOURS[c],
        )

    def refresh(self) -> None:
        self.canvas.delete('all')
        for (x, y), s in self.state.items():
            assert 1 <= s <= 6
            self.draw_cell(x, y, s)

        for x, y in self.poison:
            self.draw_cell(x, y, 0)

        self.root.after(DELAY, self.next_step)

    def next_step(self) -> None:
        self.state = student.evolve(self.state, self.poison, 1)
        self.refresh()


def main() -> None:
    game = Game()
    game.root.mainloop()


if __name__ == '__main__':
    main()
