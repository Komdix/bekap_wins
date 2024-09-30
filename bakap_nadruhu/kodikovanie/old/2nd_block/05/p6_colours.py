from ib111 import week_05  # noqa

# V tomto příkladu budeme pracovat s RGB kódy různých barev. Tyto
# kódy jsou uloženy ve slovníku, kde klíčem je řetězec - název
# barvy, a hodnota je trojice celých čísel, které představují
# hodnoty červené, zelené a modré složky.
#
# Vaším úkolem je napsat čistou funkci, která na vstupu dostane
# slovník barev a trojici celých čísel z rozsahu 0–255 a vrátí
# množinu názvů, které jsou zadané trojici nejblíže (množina bude
# obsahovat více prvků pouze v případě, že několik různých barev je
# od té zadané stejně daleko).
#
# Blízkost barev budeme měřit pomocí tzv. Manhattanské vzdálenosti,
# která je dána součtem absolutních hodnot rozdílů na jednotlivých
# souřadnicích. Například pro trojice
#
#     A = (150, 0, 65)
#     B = (120, 30, 100)
#
# je Manhattanská vzdálenost rovna
#
#    |150 - 120| + |0 - 30| + |65 - 100| = 30 + 30 + 35 = 95


Colour = tuple[int, int, int]


def distance(color_1: Colour, color_2: Colour) -> int:
    R1, G1, B1 = color_1
    R2, G2, B2 = color_2
    color = abs(R1 - R2) + abs(G1 - G2) + abs(B1 - B2)
    return color


def nearest_colour(names: dict[str, Colour], colour: Colour) -> set[str]:
    distances = []
    result = []
    nearest = 800
    for element in names.items():
        name, color_RGB = element
        distances.append((name, distance(colour, color_RGB)))
    for element_distance in distances:
        name, distance_of_color = element_distance
        if distance_of_color == nearest:
            result.append(name)
            nearest = distance_of_color
        elif distance_of_color < nearest:
            nearest = distance_of_color
            result = [name]
    return set(result)


def main() -> None:
    names = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128),
        'cyan': (0, 255, 255),
        'magenta': (255, 0, 255),
        'lime': (50, 205, 50),
        'pink': (255, 192, 203),
        'teal': (0, 128, 128),
        'lavender': (230, 230, 250),
        'maroon': (128, 0, 0),
        'navy': (0, 0, 128),
        'olive': (128, 128, 0),
        'silver': (192, 192, 192),
        'grey': (128, 128, 128),
        'orange': (255, 165, 0),
        'brown': (165, 42, 42),
        'fuchsia': (255, 0, 255),
        'violet': (238, 130, 238),
        'indigo': (75, 0, 130),
        'gold': (255, 215, 0),
        'peachpuff': (255, 218, 185),
        'darkorange': (255, 140, 0),
        'chartreuse': (127, 255, 0),
        'lightpink': (255, 182, 193),
        'skyblue': (135, 206, 235),
        'darkgreen': (0, 100, 0),
    }

    rgb = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }

    assert nearest_colour(names, (1, 1, 1)) == {'black'}
    assert nearest_colour(names, (254, 254, 254)) == {'white'}
    assert nearest_colour(rgb, (1, 1, 1)) == \
        {'red', 'green', 'blue'}


if __name__ == "__main__":
    main()
