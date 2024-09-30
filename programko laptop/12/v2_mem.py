from ib111 import week_12  # noqa


# Mějme jednoduchý programovací jazyk, jehož (jednoznakové) instrukce
# se vyhodnocují nad neomezenou pamětí. Paměť indexujeme celými čísly,
# přičemž každá paměťová buňka drží jedno celé číslo; na začátku obsahují
# všechny buňky v paměti číslo 0. V průběhu vykonávání programu si
# pamatujeme «index aktuální buňky»; na začátku je to 0.
# Instrukce jazyka jsou následující:
#
#  • ‹'<'› – snížíme *index aktuální buňky* o 1;
#  • ‹'>'› – zvýšíme *index aktuální buňky* o 1;
#  • ‹'+'› – zvýšíme hodnotu aktuální buňky o 1;
#  • ‹'-'› – snížíme hodnotu aktuální buňky o 1;
#  • ‹'['› – je-li hodnota aktuální buňky rovna nule,
#    skočíme «za» odpovídající znak ‹']'›;
#  • ‹']'› – skočíme **na** odpovídající znak ‹'['›.
#
# O programu předpokládáme, že je vzhledem ke znakům ‹'['› a ‹']'› dobře
# uzávorkovaný. Není-li výše řečeno jinak, po provedení instrukce se
# přesuneme na instrukci následující. Program končí ve chvíli, kdy by další
# provedená instrukce měla ležet za jeho koncem.
#
# Provedení každé jednotlivé instrukce by nemělo trvat příliš dlouho
# (ideálně by mělo být skoro konstantní; zejména by nemělo záviset na délce
# programu). Je v pořádku si něco předpočítat, než začnete provádět instrukce
# programu.
#
# Napište čistou funkci ‹execute›, která vyhodnotí zadaný program a vrátí obsah
# paměťových buněk jako slovník. Při testování ignorujeme paměťové buňky, které
# obsahují hodnotu 0, tedy např. slovníky ‹{1: 0, 2: 3}› a ‹{2: 3}› jsou
# z hlediska testů ekvivalentní.

def execute(program: str) -> dict[int, int]:
    pass


def main() -> None:
    assert normalize_mem(execute(
        "++++++++++++++++++++++++++++++++++++++++++"
    )) == {0: 42}

    assert normalize_mem(execute(
        "--<+++>+>+>+>++++++[-]"
    )) == {-1: 3, 0: -1, 1: 1, 2: 1}

    assert normalize_mem(execute(
        "+++++++>+[<]>-[[>]<[->>+<<]>>[-<+<+>>]<+[<]>-]"
    )) == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}

    assert normalize_mem(execute(
        "++++++[->+++++++[->+<]<]"
    )) == {2: 42}

    assert normalize_mem(execute(
        "++++++++>+<[->[->+<]>[-<++>]<<]"
    )) == {1: 256}

    assert normalize_mem(execute(
        "[+>+[[-<<+>>>+<]<[->>+<<]<[->>+<<]>>>]]"
    )) == {}

    assert normalize_mem(execute(
        "+++++++++++++++++>>+++++<<[->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]>[-]>[-]"
    )) == {3: 2, 4: 3}

    # think about the time it takes to execute instructions here!
    assert normalize_mem(execute(
        "++++++++++++++++++++++++++++++++++++++++++"
        "[<+>->[++++++++++++++++++++++++++++++++++++++++++]<]"
    )) == {-1: 42}


def normalize_mem(mem: dict[int, int]) -> dict[int, int]:
    new = {}
    for k, v in mem.items():
        if v != 0:
            new[k] = v
    return new


if __name__ == '__main__':
    main()
