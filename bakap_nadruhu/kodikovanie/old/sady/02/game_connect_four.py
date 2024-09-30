# change a_connect_four below if your file name is different
import a_connect_four as student

Grid = list[list[str]]

# you may change the game grid size here:
SIZE = 7


def draw_line(left: str, mid: str, right: str, length: int) -> None:
    for i in range(length):
        print(left if i == 0 else mid, end="")
        print("───", end="")
    print(right)


def draw(grid: Grid) -> None:
    width = len(grid)
    matrix = student.to_matrix(grid)
    left, mid, right = "┌", "┬", "┐"
    for i, row in enumerate(matrix):
        assert len(row) == width, "Wrong row length."
        draw_line(left, mid, right, width)
        for tile in row:
            print("│", tile, end=" ")
        print("|")
        left, mid, right = "├", "┼", "┤"
    draw_line("└", "┴", "┘", width)
    for i in range(width):
        print(" " if i < 10 else "", i, end=" ")
    print()


def read_column(msg: str, size: int) -> int:
    hint = "enter column number or Q to quit."
    while True:
        resp = input(msg)
        if resp == 'Q' or resp == 'q':
            return -1

        if not resp.isdecimal():
            print("Wrong input,", hint)
            continue

        column = int(resp)
        if column >= size:
            print("Number too large,", hint)
            continue

        return column


def run_game(size: int) -> None:
    print("Both players alternate in placing tokens.")
    print("Enter Q instead of a column number to quit the game prematurely.")
    print()
    player = 'O'
    grid: Grid = [[] for _ in range(size)]
    draw(grid)
    over = False
    while not over:
        player = 'X' if player == 'O' else 'O'
        column = read_column("\nPlayer " + player + ": ", size)
        if column == -1:
            print("\nQuit.")
            return

        print()
        over = student.play(grid, player, column)
        draw(grid)
    print("\nGame over, player", player, "won.")


if __name__ == '__main__':
    run_game(SIZE)
