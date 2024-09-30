# from ib111 import week_06  # noqa

# Hru «Life¹» už jste si možná zkusili implementovat v rámci rozšířených
# příkladů ve čtvrté kapitole. V tomto úkolu budete implementovat její trochu
# složitější verzi. Místo jednoho života budeme simulovat souboj dvou různých
# organismů (modré a oranžové buňky), pozice po úmrtí buňky bude po několik kol
# neobyvatelná a budeme mít trochu jiná pravidla pro to, kdy buňky vznikají
# a zanikají. Kromě toho bude náš „svět“ neomezený a bude obsahovat „otrávené“
# oblasti, kde žádné buňky nepřežijí.
#
# ¹ ‹https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life›
#
# Stav „světa“ je dán slovníkem, jehož klíči jsou 2D souřadnice a hodnotami
# čísla od jedné do šesti:
#
# • číslo 1 reprezentuje živou modrou buňku,
# • číslo 2 reprezentuje živou oranžovou buňku,
# • čísla 3 až 6 reprezentují pozici, kde dříve zemřela buňka
#   (čím větší číslo, tím víc času od úmrtí buňky uplynulo).
#
# Pozice, které nejsou obsaženy ve slovníku, jsou prázdné.

Position = tuple[int, int]
State = dict[Position, int]

# Stejně jako ve hře Life, za «okolí» pozice považujeme sousední pozice
# ve všech osmi směrech, tj. včetně diagonál.
# Základní pravidla vývoje světa jsou následující:
#
# • Pokud jsou v okolí prázdné pozice přesně tři živé buňky, vznikne zde
#   v dalším kole buňka nová. Barva nové buňky odpovídá většinové barvě
#   živých buněk v okolí. Jinak zůstává prázdná pozice prázdnou.
# • Pokud je v okolí živé buňky tři až pět živých buněk (na barvě nezáleží),
#   buňka zůstane živou i v dalším kole (a ponechá si svou barvu).
#   V opačném případě buňka umře a stav této pozice v dalším kole bude číslo 3.
# • Má-li pozice stav 3 až 5, pak v dalším kole bude mít stav o jedna větší.
# • Má-li pozice stav 6, v dalším kole bude prázdná.
#
# „Otrávené“ pozice jsou zadány extra (jako množina) a mění základní pravidla
# tak, že živé buňky na otrávených pozicích «a v jejich okolí» vždy zemřou
# a na těchto pozicích (otrávených a jejich okolí) nikdy nevzniknou nové buňky.


# Napište čistou funkci ‹evolve›, která dostane počáteční stav světa ‹initial›,
# množinu „otrávených“ pozic ‹poison› a počet kol ‹generations› a vrátí stav
# světa po zadaném počtu kol.


def get_neighbors(position: Position) -> list[Position]:
    x, y = position
    neighbors = []
    for add_x in [-1, 0, 1]:
        for add_y in [-1, 0, 1]:
            if add_x == 0 and add_y == 0:
                continue
            neighbor_position = (x + add_x, y + add_y)
            neighbors.append(neighbor_position)
    return neighbors


def evolve_cell(position, state, poison):
    neighbors = get_neighbors(position)
    live_neighbors = sum(state.get(neighbor, 0) in [1, 2] for neighbor in neighbors)
    cell = state.get(position, 0)

    # Handle poisoned positions
    if position in poison or any(neighbor in poison for neighbor in neighbors):
        return 3 if cell in [1, 2] else 0

    # Evolution rules
    if cell in [1, 2]:  # Live cell rules
        return cell if 3 <= live_neighbors <= 5 else 3
    elif cell in [3, 4, 5]:  # Dead cell evolving
        return cell + 1
    elif cell == 6:  # Cell becomes empty
        return 0
    elif cell == 0:  # Empty space rules
        if live_neighbors == 3:
            neighbor_colors = [state.get(neighbor) for neighbor in neighbors if state.get(neighbor) in [1, 2]]
            return max(set(neighbor_colors), key=neighbor_colors.count)
        return 0

    


# def evolve(initial: State, poison: set[Position],
#            generations: int) -> State:
def evolve(initial: State, poison: set[Position], generations: int) -> State:
    current_state = initial.copy()
    for _ in range(generations):
        new_state = {}
        for position in set(current_state.keys()) | {neighbor for pos in current_state.keys() for neighbor in get_neighbors(pos)}:
            new_state[position] = evolve_cell(position, current_state, poison)
        current_state = new_state
    return current_state


# Pro vizualizaci je vám k dispozici soubor ‹game_life.py›, který vložte do
# stejného adresáře, jako je soubor s vaším řešením. Na začátku tohoto souboru
# jsou parametry vizualizace (velikost buněk, rychlost vývoje), popis
# iniciálního stavu světa a „otrávených“ pozic. Vizualizace volá vaši funkci
# evolve s parametrem ‹generations› vždy nastaveným na 1.


def main() -> None:
    square = {(3, 3): 1, (3, 4): 2, (4, 4): 1, (4, 3): 2}

    assert evolve(square, set(), 1000) == square

    assert evolve(square, {(3, 3)}, 1) \
        == {(3, 3): 3, (3, 4): 3, (4, 4): 3, (4, 3): 3}

    planet = {(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 0): 1,
              (0, -1): 1, (1, -1): 3}

    assert evolve(planet, set(), 10) \
        == {(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 0): 1,
            (2, 0): 6, (1, -1): 5, (0, -1): 4, (-1, 0): 3, (-1, 1): 1}

    ship = {(0, 0): 1, (0, 1): 1,
            (-1, 0): 1, (-1, 1): 1, (-1, 2): 1,
            (1, 0): 1, (1, 1): 1, (1, 2): 1,
            (-2, 2): 1, (2, 2): 1}

    assert evolve(ship, {(2, -19)}, 42) \
        == {(-1, -17): 6, (1, -17): 6, (0, -18): 6, (-2, -17): 6}

    assert evolve(ship, {(3, -19)}, 1000) \
        == {(-1, -496): 5, (0, -497): 6, (-1, -497): 3, (1, -497): 5,
            (0, -498): 4, (-2, -496): 6, (-1, -498): 1, (1, -498): 3,
            (0, -499): 1, (-2, -497): 4, (-1, -499): 1, (1, -499): 1,
            (0, -500): 1, (-2, -498): 1, (-1, -500): 1, (1, -500): 1}

    collision = {(-20, -2): 1, (-20, -1): 1, (-19, -1): 1, (-18, -1): 1,
                 (-19, 0): 1, (-18, 0): 1, (-20, 1): 1, (-19, 1): 1,
                 (-18, 1): 1, (-20, 2): 1, (21, -2): 2, (21, -1): 2,
                 (20, -1): 2, (19, -1): 2, (20, 0): 2, (19, 0): 2,
                 (21, 1): 2, (20, 1): 2, (19, 1): 2, (21, 2): 2}

    assert evolve(collision, set(), 46) == {}

    collision_out_of_sync = {
        (-20, -2): 1, (-20, -1): 1, (-19, -1): 1, (-18, -1): 1, (-19, 0): 1,
        (-18, 0): 1, (-20, 1): 1, (-19, 1): 1, (-18, 1): 1, (-20, 2): 1,
        (21, -1): 2, (20, -1): 2, (19, -1): 2, (19, 0): 2, (18, 0): 2,
        (21, 1): 2, (20, 1): 2, (19, 1): 2
    }

    assert evolve(collision_out_of_sync, set(), 100) \
        == {(-1, -3): 1, (-1, 3): 1, (-1, -4): 1, (-1, 4): 1,
            (-2, -4): 1, (-2, -3): 1, (-2, 3): 1, (-2, 4): 1}


if __name__ == '__main__':
    main()
