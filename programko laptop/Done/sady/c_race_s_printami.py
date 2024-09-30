from ib111 import week_01  # noqa


# Uvažujme hru čtyř hráčů s následujícími pravidly:
#
# • herní plán je jednorozměrný, s neomezenou délkou a vyznačeným startovním
#   políčkem;
# • každý hráč má jednu figurku, na začátku umístěnou na startovním políčku;
# • hráči střídavě hází kostkou a posunují své figurky o hozené číslo;
# • pokud by hráčova figurka měla vstoupit na políčko obsazené figurkou
#   jiného hráče, tato figurka je „vykopnuta“ (jako v Člověče, nezlob se)
#   zpět na start.
#
# Situaci na herním plánu budeme reprezentovat pomocí nezáporného celého čísla
# tak, že jeho zápis v pětkové soustavě reprezentuje obsazenost jednotlivých
# políček bez startovního políčka. Číslice 0 reprezentuje prázdné políčko,
# číslice 1–4 pak reprezentují obsazenost figurkou konkrétního hráče. Pohyb
# figurek přitom v pětkovém zápisu probíhá „zprava doleva“, tedy směrem od
# nižších řádů k vyšším.
#
# Příklady:
#
#  ┌───────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
#  │start: 1234│   │   │   │   │   │   │   │   │   │   │   │ …
#  └───────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
#
# Všechny figurky jsou na startu – stav reprezentovaný číslem 0.
#
#  ┌───────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
#  │start: 1 3 │   │ 2 │   │   │   │ 4 │   │   │   │   │   │ …
#  └───────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
#
# Figurky hráčů 1 a 3 jsou na startu, figurka hráče 2 je dvě políčka od startu,
# figurka hráče 4 je šest políček od startu. Tento stav je reprezentovaný
# číslem ⟦(400020)₅ = 4 · 5⁵ + 2 · 5¹ = 12510⟧.
#
#
# Napište čistou funkci ‹play›, která na plánu reprezentovaném číslem ‹arena›
# provede jeden tah hráče ‹player› o zadaný hod kostkou ‹throw› a vrátí
# číslo reprezentující nový stav hry.
#
# Předpokládejte, že ‹arena› je validní stav hry (tj. nezáporné celé číslo,
# v jehož pětkovém zápisu se objevuje každá z číslic 1–4 nejvýše jednou),
# že ‹player› je jedno z čísel 1, 2, 3, 4 a že ‹throw› je kladné celé číslo.
# (Nemusí být nijak shora omezené; předpokládejte, že máme kostky s různě
# velkými čísly.)


def position(arena, player):

    pos = 0
    n = arena
    test = 0

    while n > 0:
        # print(n,'nko')
        control = n % 5
        n //=5
        test += control * 10 ** pos
        # print(control,'control',player)
        # if control == player and pos == 0:
        #     return 0
        if control == player:
            
            # print(pos,'pozicia kokota')
            return pos
        # print(pos,'pozicia kokota')
        pos += 1
    return -1


def control_player(arena, position):

    n = arena
    pos = 0

    while n > 0:
        control = n % 5
        n //= 5

        if position == pos:
            return control
        
        pos +=1
    return 0


# t = control_player(84770, 7)
# print(t, 'kontrola')


def play(arena, player, throw):

    if arena == 0:
        base = player * 5 ** (throw - 1)
        return base

    test = 0
    pos = 0
    n = arena

    while n > 0:
        control = n % 5
        n //=5
        test += control * 10 ** pos
        pos += 1
    # print(test,'v patkovej_1')
    # print(arena)

    position_of_player = position(arena, player)
    # print(position_of_player,'stara')
    new_position = position_of_player + throw 
    # print(new_position, 'nova')
    control = control_player(arena, new_position)
    # control_0 = control_player(arena, new_position )
    # print(control_0 , 'vyhadzuje')
    # print(control, 'vyhadzuje')

    if arena == player:
        new_arena = arena - player + player * (5 ** new_position)
        # print(new_arena, 'new')
        return new_arena




    if position_of_player == -1:
        if control == 0:
            new_arena = arena + (player  * (5 ** (new_position )))
            # print('0 a nevyhodil')
        else:
            new_arena = arena - control * (5 ** (new_position )) + player * (5 ** (new_position ))
            # print('0 a vyhodil')
            # print()

    else:
        if control == 0:
            new_arena = arena - (player * (5 ** position_of_player)) + (player * (5 ** new_position))
            # print('nevyhodil')
        else:
            new_arena = arena - control * (5 ** new_position) - player * (5 ** position_of_player) + player * (5 ** new_position) 
            # print('vyhodil')

    
    # print(new_arena, 'new')
    return new_arena


# test = 0
# pos = 0
# n = play(12510, 1, 2)

# while n > 0:
#     control = n % 5
#     n //=5
#     test += control * 10 ** pos
#     pos += 1
    
# print(test,'v patkovej')
assert play(11, 1, 1) == 5
# print(t)
# for i in range(5):
#     for j in range(1,4):
#         for k in range(1,5):
#             a = 0
#             b = j
#             c = k
#             print(a,b,c)
#             t = play(a, b, c)
#             print(t, "result")
#             test = 0
#             pos = 0
#             n = t

#             while n > 0:
#                 control = n % 5
#                 n //=5
#                 test += control * 10 ** pos
#                 pos += 1
#             print(test,'v patkovej')
def main():
    for p in range(1, 5):
        assert play(0, p, 1) == p

    assert play(11, 3, 3) == 86
    assert play(84770, 4, 5) == 147250
    assert play(84770, 3, 4) == 240645
    assert play(12510, 1, 2) == 12505


if __name__ == '__main__':
    main()
