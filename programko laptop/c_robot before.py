from ib111 import week_06  # noqa

# Představte si, že máme plán ve tvaru neomezené čtvercové sítě, na níž jsou
# položeny čtvercové dílky s nákresy ulic či křižovatek (něco jako kartičky ve
# hře Carcassone). Tyto dílky budeme reprezentovat jako množiny směrů, kterými
# je možné dílek opustit. Tedy např. dílek ‹{NORTH, SOUTH}› je ulice, která
# vede severojižním směrem, dílek ‹{EAST, SOUTH, WEST}› je křižovatka ve
# tvaru T, dílek ‹{EAST}› je slepá ulice (z toho dílku je možné se posunout
# pouze na východ, ale nikam jinam). Dovolujeme i prázdnou množinu, což je
# dílek, z nějž se nedá pohnout nikam.

Heading = int
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
Tile = set[Heading]

# Situaci na čtvercové síti popisujeme pomocí slovníku, jehož klíči jsou
# souřadnice a hodnotami dílky. Na souřadnicích, které ve slovníku nejsou,
# se žádný dílek nenachází. Souřadnice jsou ve formátu ‹(x, y)›, přičemž
# ‹x› se zvyšuje směrem na východ a ‹y› směrem na jih.

Position = tuple[int, int]
Plan = dict[Position, Tile]


# Napište nejprve predikát ‹is_correct›, který vrátí ‹True› právě tehdy, pokud
# na sebe všechny položené dílky správně navazují. Tedy je-li možno dílek
# nějakým směrem opustit, pak v tomto směru o jednu pozici vedle leží další
# dílek, a navíc je z tohoto dílku možné se zase vrátit.


def is_correct(plan: Plan) -> bool:
    headings = list(plan.values())
    if plan == {} or headings == []:
        return True
    for element in plan.keys():
        x, y = element
        directions = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
        oposite = [SOUTH, WEST, NORTH, EAST]
        ways = plan[element]
        for way in ways:
            move = oposite[way]
            if directions[way] not in plan or \
               move not in plan[directions[way]]:
                return False
    return True


# Dále implementujte čistou funkci ‹run›, která bude simulovat pohyb robota
# po plánu a vrátí jeho poslední pozici. Předpokládejte přitom, že plán je
# korektní (ve smyslu predikátu ‹is_correct› výše) a že robotova počáteční
# pozice je na některém z položených dílků. Robot se pohybuje podle
# následujících pravidel:
#
# • Na počáteční pozici si robot vybere první ze směrů, kterým je možné se
#   pohnout z počátečního dílku, a to v pořadí sever, východ, jih, západ.
#   Pokud se z počáteční pozice není možné pohnout vůbec, funkce končí.
# • V dalších krocích robot preferuje setrvat v původním směru (tj. pokud může
#   jít rovně, půjde rovně). Není-li to možné, pohne se robot jiným ze směrů na
#   aktuálním dílku – nikdy se ovšem nevrací směrem, kterým přišel (pokud dojde
#   do slepé ulice, zastaví) a má-li více možností, vybere si tu, která pro něj
#   znamená otočení doprava.
# • Pokud robot přijde na dílek, kde už někdy v minulosti byl, zastaví.


Been_to = list[Position]


def run(plan: Plan, start: Position) -> Position:
    x, y = start
    been_to = [start]
    directions = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    last_way = None
    pos = start
    for i in range(4):
        if i in plan[pos]:
            last_way = i
            pos = directions[i]
            been_to.append(pos)
            break
    if last_way is None:
        return start

    while pos in plan:
        x, y = pos
        last_pos = pos
        directions = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

        if last_way in plan[pos]:
            pos = directions[last_way]
            if pos in been_to:

                return pos
            been_to.append(pos)
            continue
        if last_way != 3:
            last_way += 1
        else:
            last_way = 0
        if last_way in plan[pos]:
            pos = directions[last_way]
            if pos in been_to:
                return pos
            been_to.append(pos)
            continue
        if last_way >= 2:
            last_way -= 2
        else:
            last_way += 2
        if last_way in plan[pos]:
            pos = directions[last_way]
            if pos in been_to:
                return pos
            been_to.append(pos)

        elif pos == last_pos or (pos in been_to and pos != been_to[-1]):
            return pos
    return pos


def main() -> None:
    assert is_correct({})
    assert is_correct({(1, 1): set()})
    assert is_correct({(1, 1): {NORTH}, (1, 0): {SOUTH}})
    assert is_correct({
        (3, 3): {NORTH, WEST},
        (2, 2): {SOUTH, EAST},
        (3, 2): {SOUTH, WEST},
        (2, 3): {NORTH, EAST},
    })

    assert not is_correct({(7, 7): {WEST}})
    assert not is_correct({(7, 7): {WEST}, (6, 7): set()})
    assert not is_correct({
        (3, 3): {NORTH, WEST},
        (2, 2): {SOUTH, EAST},
        (3, 2): {SOUTH, WEST},
        (2, 3): {NORTH},
    })

    plan = {
        (-2, -2): {EAST, SOUTH},
        (-1, -2): {EAST, WEST},
        (0, -2): {SOUTH, WEST},
        (-5, -1): {SOUTH},
        (-2, -1): {NORTH, SOUTH},
        (0, -1): {NORTH, SOUTH},
        (5, -1): {EAST, SOUTH},
        (6, -1): {SOUTH, WEST},
        (-5, 0): {NORTH, EAST, SOUTH},
        (-4, 0): {EAST, WEST},
        (-3, 0): {EAST, WEST},
        (-2, 0): {NORTH, EAST, WEST},
        (-1, 0): {EAST, WEST},
        (0, 0): {NORTH, EAST, SOUTH, WEST},
        (1, 0): {EAST, WEST},
        (2, 0): {EAST, SOUTH, WEST},
        (3, 0): {EAST, WEST},
        (4, 0): {EAST, WEST},
        (5, 0): {NORTH, EAST, WEST},
        (6, 0): {NORTH, WEST},
        (-5, 1): {NORTH},
        (0, 1): {NORTH, SOUTH},
        (2, 1): {NORTH, SOUTH},
        (-1, 2): {EAST},
        (0, 2): {NORTH, EAST, WEST},
        (1, 2): {EAST, WEST},
        (2, 2): {NORTH, WEST},
    }

    assert run({(0, 0): set()}, (0, 0)) == (0, 0)
    assert run({(1, 1): {NORTH}, (1, 0): {SOUTH}}, (1, 1)) == (1, 0)
    assert run({(1, 1): {NORTH}, (1, 0): {SOUTH}}, (1, 0)) == (1, 1)

    assert is_correct(plan)

    assert run(plan, (0, 0)) == (-5, -1)
    assert run(plan, (-5, -1)) == (-5, 1)
    assert run(plan, (-4, 0)) == (5, 0)
    assert run(plan, (0, 1)) == (-5, -1)
    assert run(plan, (-1, 2)) == (5, 0)

    plan[2, 0] = {WEST, SOUTH}
    plan[3, 0] = {EAST}

    assert is_correct(plan)

    assert run(plan, (-4, 0)) == (-1, 2)
    assert run(plan, (1, 2)) == (-5, -1)


if __name__ == '__main__':
    main()
