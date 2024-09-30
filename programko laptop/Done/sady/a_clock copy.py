from ib111 import week_00  # noqa
from turtle import forward, backward, right, left, \
     penup, pendown, setheading, done
from math import pi, sin


# Napište proceduru ‹clock›, která pomocí želví grafiky vykreslí ciferník
# hodin s ručičkami v následující podobě:
#
# • ciferník má tvar dvanáctiúhelníku postaveného „na špičku“ s délkou
#   strany rovnou ‹side›, vrcholy dvanáctiúhelníku tedy odpovídají číslicím;
# • ručičky ukazují čas zadaný ve formátu UNIX Epoch Time, tj. jako
#   počet sekund od 1. 1. 1970, 0.00:00, v parametru ‹epoch_time›;
# • sekundová ručička je znázorněna čarou o délce 1,8násobku ‹side›;
# • minutová ručička je znázorněna prázdným obdélníkem o délce
#   1,6násobku ‹side› a šířce dvacetiny ‹side›;
# • hodinová ručička je znázorněna prázdným obdélníkem o délce
#   1,4násobku ‹side› a šířce desetiny ‹side›;
# • pro ručičky ve tvaru obdélníku platí, že vzdálenost mezi středem ciferníku
#   a kratší stranou obdélníku je polovina jeho šířky.
#
# Parametr ‹epoch_time› je vždy celé číslo, parametr ‹side› je kladné „reálné“
# číslo (typu ‹float›).
#
# Minutová a hodinová ručička se neposunují skokově, ale (v rámci možností)
# spojitě, tj. například v čase 13.30:00 je hodinová ručička přesně
# v polovině úhlu mezi jedničkou a dvojkou.
#
# Testovací prostředí želví grafiky podporuje pouze procedury ‹forward›,
# ‹backward›, ‹right›, ‹left›, ‹penup›, ‹pendown›, ‹setheading›.
# Použití procedur ‹speed›, ‹delay› a ‹done› se sice nepovažuje za chybu,
# ale budou v testech ignorovány, tj. «nebudou mít žádný efekt».


def draw_sec(lenght):
    forward(lenght)
    backward(lenght)


def draw_other(length, width):
    penup()
    backward(width/2)
    pendown()
    right(90)
    forward(width/2)
    left(90)
    forward(length)
    left(90)
    forward(width)
    left(90)
    forward(length)
    left(90)
    forward(width/2)
    left(90)
    penup()
    forward(width/2)
    pendown()


def draw_polygon(side):

    diameter = side / (2 * sin(pi / 12))

    penup()
    left(90)
    forward(diameter)
    pendown()
    right(75)
    for i in range(12):
        right(30)
        forward(side)
    left(75)
    penup()
    backward(diameter)
    pendown()


def clock(epoch_time, side):

    sec_length = 1.8 * side
    minutes_length = 1.6 * side
    minutes_width = 0.05 * side
    hours_length = 1.4 * side
    hours_width = 0.1 * side

    time = epoch_time % 43200
    hours = time // 3600
    minutes = time // 60 % 60
    sec = time - (hours * 3600 + minutes * 60)

    draw_polygon(side)

    sec_angle = (float(sec)/60.0) * 360
    min_angle = ((float(minutes) / 60.0) * 360) + ((float(sec) / 3600) * 360)
    hours_angle = ((float(hours) / 12) * 360) + ((float(minutes) / 720)*360)

    right(sec_angle)
    draw_sec(sec_length)
    setheading(90)
    right(hours_angle)
    draw_other(hours_length, hours_width)
    setheading(90)
    right(min_angle)
    draw_other(minutes_length, minutes_width)
    setheading(90)


def main():
    clock(1661081862, 150.0)
    done()


if __name__ == '__main__':
    main()
