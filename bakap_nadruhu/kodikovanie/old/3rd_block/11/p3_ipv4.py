from ib111 import week_11  # noqa


# V této úloze se budeme zabývat adresami protokolu IP verze 4,
# které sestávají ze 4 čísel oddělených tečkami, například
# ‹192.0.2.0› (více informací o IPv4 naleznete například na
# Wikipedii). Adresy budeme reprezentovat řetězci.

# Napište predikát, kterého hodnota bude ‹True›, představuje-li jeho
# parametr validní IPv4 adresu. Daná IPv4 adresa je validní právě
# tehdy, když je tvořená čtyřmi dekadickými čísly od 0 až 255
# (včetně) oddělenými tečkou (pro jednoduchost v této úloze
# připouštíme pouze kanonický tvar IPv4 adres).

def str_to_int(s: str) -> int | None:
    integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for integer in integers:
        if integer == s:
            return integers.index(integer)
    return None


def ipv4_validate(address: str) -> bool:
    parts = address.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if part == "":
            return False

        control = []

        for num in part:
            digit = str_to_int(num)
            if digit is None:
                return False
            control.append(digit)

        number = 0
        control.reverse()

        for i in range(len(control)):
            number += (control[i] * 10 ** i)
        if not 0 <= number <= 255:
            return False

    return True


# Dále napište čistou funkci, která vypočte číselnou hodnotu dané
# adresy.  Konverze IPv4 adresy na její číselnou hodnotu je podobná
# konverzi binárního zápisu čísla na dekadický s tím rozdílem, že
# u IPv4 adresy pracujeme se základem 256. Hodnota adresy
# ‹192.0.2.0› je tedy ⟦192⋅256³ + 0⋅256² + 2⋅256¹ + 0⋅256⁰ =
# 3 221 225 984⟧. Můžete počítat s tím, že vstupem bude vždy validní
# IPv4 adresa ve výše popsaném kanonickém tvaru.

def ipv4_value(address: str) -> int | None:
    Parts = address.split(".")
    value = 0
    exponent = 0
    Parts.reverse()

    for part in Parts:
        part_value = 0
        control = []

        for num in part:
            digit = str_to_int(num)
            if digit is None:
                return None
            control.append(digit)

        control.reverse()

        for j in range(len(control)):
            part_value += control[j] * 10 ** j

        value += part_value * (256 ** exponent)
        exponent += 1

    return value


def main() -> None:
    assert ipv4_validate("192.0.2.0")
    assert ipv4_validate("5.5.5.5")
    assert ipv4_validate("255.255.255.255")
    assert ipv4_validate("0.0.0.0")
    assert not ipv4_validate("a.5.5.5")
    assert not ipv4_validate("0.0.0.č")
    assert not ipv4_validate("256.4.3.2")
    assert not ipv4_validate("1.2.3.-1")
    assert not ipv4_validate("2.2.2.")
    assert not ipv4_validate("2.2.2")
    assert not ipv4_validate("5.5.5.5.5")

    assert ipv4_value("192.0.2.0") == 3221225984
    assert ipv4_value("0.0.0.0") == 0
    assert ipv4_value("255.255.255.255") == 4294967295
    assert ipv4_value("1.1.1.1") == 16843009
    assert ipv4_value("12.0.55.200") == 201340872


if __name__ == "__main__":
    main()
