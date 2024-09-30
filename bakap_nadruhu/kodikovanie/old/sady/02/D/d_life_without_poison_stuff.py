from ib111 import week_06  # noqa

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


def neighbors(position: Position) -> list[Position]:
    x, y = position
    lst_neighbors = []
    for add_x in [-1, 0, 1]:
        for add_y in [-1, 0, 1]:
            if add_x == 0 and add_y == 0:
                continue
            neighbor_pos = (x + add_x, y + add_y)
            lst_neighbors.append(neighbor_pos)
    return lst_neighbors


def evolution_step(position, state:dict, poison):
    alive = [1, 2]
    dead = [3, 4, 5]
    clear = 6
    neighbors_all = neighbors(position)
    neighbors_alive = 0
    for element in neighbors_all:
        controlled = state.get(element)
        if controlled == 1 or controlled == 2:
            neighbors_alive += 1

    main_cell = state.get(position)

    for element in neighbors_all:
        if element in poison:
            return 3
        
            
    if position in poison:
        return 3

    if main_cell in alive:
        if neighbors_alive >= 3 and neighbors_alive <= 5:
            return main_cell
        else:
            return 3
    elif main_cell in dead:
        return main_cell + 1
    elif main_cell == clear:
        return None  
    elif main_cell == 0 or main_cell is None:
        if neighbors_alive == 3:
            blue = 0
            orange = 0
            for element in neighbors_all:
                neighbor = state.get(element)
                if neighbor == 1:
                    blue += 1
                if neighbor == 2:
                    orange += 1

            if blue >= 2:
                return 1
            if orange >= 2:
                return 2

        return None


def evolve(initial: State, poison: set[Position],
           generations: int) -> State:
    current = initial.copy()
    for _ in range(generations):
        lst_current = list(current.keys())
        next_state = {}
        all_pos = set(current.keys())
        born = set()
        for element in lst_current:
            lst_add = neighbors(element)
            for neighbor in lst_add:
                born.add(neighbor)
        for element in born:
            able_of_birth = evolution_step(element, current, poison)
            if (able_of_birth == 1 or able_of_birth == 2) and element not in all_pos:
                all_pos.add(element)

        for position in all_pos:
            kek = evolution_step(position, current, poison)
            if kek is not None:
                next_state[position] = kek

        current = next_state
    return current


# square = {(3, 3): 1, (3, 4): 2, (4, 4): 1, (4, 3): 2}

# # assert evolve(square, set(), 1000) == square

# s =  evolve(square, {(3, 3)}, 5) 

#     # == {(3, 3): 3, (3, 4): 3, (4, 4): 3, (4, 3): 3}

# Pro vizualizaci je vám k dispozici soubor ‹game_life.py›, který vložte do
# stejného adresáře, jako je soubor s vaším řešením. Na začátku tohoto souboru
# jsou parametry vizualizace (velikost buněk, rychlost vývoje), popis
# iniciálního stavu světa a „otrávených“ pozic. Vizualizace volá vaši funkci
# evolve s parametrem ‹generations› vždy nastaveným na 1.


def main() -> None:
    square = {(3, 3): 1, (3, 4): 2, (4, 4): 1, (4, 3): 2}

    # assert evolve(square, set(), 1000) == square

    assert evolve(square, {(3, 3)}, 1) \
        == {(3, 3): 3, (3, 4): 3, (4, 4): 3, (4, 3): 3}

    planet = {(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 0): 1,
              (0, -1): 1, (1, -1): 3}
    
    assert evolve(planet, set(), 10) \
        == {(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 0): 1,
            (2, 0): 6, (1, -1): 5, (0, -1): 4, (-1, 0): 3, (-1, 1): 1}
    assert planet == {(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 0): 1,
              (0, -1): 1, (1, -1): 3}

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
    
    assert collision_out_of_sync == {
        (-20, -2): 1, (-20, -1): 1, (-19, -1): 1, (-18, -1): 1, (-19, 0): 1,
        (-18, 0): 1, (-20, 1): 1, (-19, 1): 1, (-18, 1): 1, (-20, 2): 1,
        (21, -1): 2, (20, -1): 2, (19, -1): 2, (19, 0): 2, (18, 0): 2,
        (21, 1): 2, (20, 1): 2, (19, 1): 2
    }

if __name__ == '__main__':
    main()
