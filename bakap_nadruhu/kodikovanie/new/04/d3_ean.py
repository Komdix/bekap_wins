from ib111 import week_04  # noqa

# European Article Number (EAN) je systém číslování výrobků, který
# pravděpodobně znáte z čárových kódů v supermarketech. EAN funguje
# podobně jako ISBN, se kterým jste minulý týden pracovali
# v příkladu ‹04/isbn.py›, nicméně neomezuje se na knihy. V této
# ukázce budeme pokračovat v používání «tvrzení» (‹assert›) pro
# popis vstupních a výstupních podmínek funkcí. Protože budeme chtít
# převádět číselné kódy na čárové a obráceně, využijeme funkce pro
# práci s čárovými kódy, které jsme definovali v předchozí ukázce.

from d2_barcode import \
    barcode_valid, barcode_decode, barcode_encode, barcode_digits, \
    digit_count, digit_slice


def digit_compose(left: int, right: int, base: int,
                  r_size: int) -> int:
    assert digit_count(right, base) <= r_size
    return left * (base ** r_size) + right


def decimal_count(num: int) -> int:
    return digit_count(num, 10)


def decimal_slice(num: int, low: int, digits: int) -> int:
    return digit_slice(num, 10, low, digits)


def bit_compose(left: int, right: int, r_bits: int) -> int:
    return digit_compose(left, right, 2, r_bits)


def decimal_compose(left: int, right: int, r_digits: int) -> int:
    return digit_compose(left, right, 10, r_digits)


# Podobně jako v případě ISBN budeme EAN reprezentovat jako číslo.
# Jako první si zadefinujeme predikát, který bude rozhodovat,
# jedná-li se o platný EAN: postup je podobný jako pro ISBN,
# poslední cifra je kontrolní. EAN existuje v několika délkách, ale
# algoritmus pro jejich kontrolu je vždy stejný: proto dostane náš
# predikát krom samotného EAN jako parametr i očekávanou délku kódu.
# Tento predikát samotný nemá žádné vstupní podmínky.

def ean_valid(ean: int, length: int) -> bool:
    checksum = 0
    odd = True
    digits = 0

    while ean > 0:
        digits += 1
        checksum += ean % 10 * ean_digit_weight(odd)
        odd = not odd
        ean //= 10

    return digits <= length and checksum % 10 == 0


# Pomocná funkce, která popisuje váhy jednotlivých číslic v EAN
# kódu (pro účely výpočtu kontrolní číslice).

def ean_digit_weight(odd: bool) -> int:
    return 1 if odd else 3


# Další funkce, kterou budeme definovat, slouží k vytvoření platného
# EAN-13 kódu z jednotlivých komponent: prefixu GS1 (zjednodušeně
# odpovídá zemi výrobce), kódu výrobce (který je minimálně
# pěticiferný) a kódu samotného výrobku. Vstupní podmínky odpovídají
# omezením na jednotlivé komponenty. Celková délka kódu bez
# kontrolního součtu musí být 12 cifer. Funkce komponenty zkombinuje
# a přidá kontrolní cifru. Výstupní podmínkou je, že jsme vytvořili
# platný třináctimístný EAN kód (kontrolujeme ji těsně před návratem
# z funkce).

def generate_ean(gs1: int, manufacturer: int, product: int,
                 product_digits: int) -> int:
    assert 0 <= gs1 < 1000
    assert manufacturer >= 0
    assert decimal_count(product) <= product_digits
    assert decimal_count(manufacturer) + product_digits <= 10
    manufacturer_digits = 12 - product_digits - 3

    odd = False
    check = 0

    for part in [product, manufacturer, gs1]:
        while part > 0:
            check += part % 10 * ean_digit_weight(odd)
            part //= 10
            odd = not odd

    check = 10 - check % 10

    ean = decimal_compose(gs1, manufacturer, manufacturer_digits)
    ean = decimal_compose(ean, product, product_digits)
    ean = decimal_compose(ean, check, 1)

    assert ean_valid(ean, 13)
    return ean


# Následují dvě funkce pro konverzi mezi číselným a čárovým kódem.
# První dostane na vstupu platnou číselnou reprezentaci EAN-8 (tuto
# vstupní podmínku kontroluje první příkaz ‹assert›). Výstupní
# podmínkou naopak je, že funkce vytvoří platný čárový kód – tuto
# kontrolujeme, jak je obvyklé, těsně před návratem.

def ean8_to_barcode(ean: int) -> int:
    assert ean_valid(ean, 8)
    left = barcode_encode(decimal_slice(ean, 4, 4), 'L')
    right = barcode_encode(decimal_slice(ean, 0, 4), 'R')

    barcode = 0
    barcode = bit_compose(barcode, 0b101, 3)
    barcode = bit_compose(barcode, left, 7 * 4)
    barcode = bit_compose(barcode, 0b01010, 5)
    barcode = bit_compose(barcode, right, 7 * 4)
    barcode = bit_compose(barcode, 0b101, 3)

    assert barcode_valid(barcode, 8, 'L', 'R')
    return barcode


# Poslední funkce v tomto souboru slouží pro opačnou konverzi:
# z čárového kódu vytvoří číselnou reprezentaci. Vstupní podmínkou
# je, že čárový kód je platný a kóduje 8 číslic; toto díky predikátu
# ‹barcode_valid› lehce ověříme. Nicméně si musíme dát pozor na
# «výstupní» podmínku: mohlo by se zdát, že analogicky k předchozímu
# případu by bylo rozumné požadovat platnost číselného EAN.

# Není tomu tak: byla-li splněna vstupní podmínka (čárový kód
# ‹barcode› je platný), funkce musí svoji výstupní podmínku «vždy
# splnit». Musíme si ale uvědomit, že existují platné osmičíslicové
# čárové kódy, které «nekódují» platný EAN-8. Proto je výstupní
# podmínka platnosti EAN kódu příliš silná – nedokážeme ji
# zabezpečit.

# Jako vhodné řešení se jeví v případě, kdy na vstupu dostaneme
# čárový kód reprezentující neplatný EAN, vrátit hodnotu ‹None›:
# výstupní podmínku tak zeslabíme jen minimálně. Bude vždy platit,
# že výstupem je buď platný EAN-8 (a to vždy, když je to možné),
# nebo hodnota ‹None› (pouze v případech, kdy vstup reprezentoval
# neplatný EAN-8). Ze zápisu návratové hodnoty je zřejmé, že tato
# výstupní podmínka je splněna, nemá tedy smysl ji dodatečně
# kontrolovat příkazem ‹assert›.

def barcode_to_ean8(barcode: int) -> int | None:
    assert barcode_valid(barcode, 8, 'L', 'R')
    left, right = barcode_digits(barcode)
    ean = decimal_compose(barcode_decode(left, 'L'),
                          barcode_decode(right, 'R'), 4)
    if not ean_valid(ean, 8):
        return None
    return ean


def main() -> None:  # demo
    week_04

    assert ean_valid(12345670, 8)
    assert ean_valid(1122334455666, 13)
    assert not ean_valid(12345674, 8)
    assert not ean_valid(1122334455664, 13)
    assert generate_ean(123, 123212, 123, 3) == 1231232121235
    assert generate_ean(444, 12345, 1111, 4) == 4441234511119
    assert ean8_to_barcode(12345670) == 0x5324dea354ea11395
    assert ean8_to_barcode(11112228) == 0x53264c9956cd9b245
    assert barcode_to_ean8(0x5324dea354ea11395) == 12345670
    assert barcode_to_ean8(0x53264c9956cd9b245) == 11112228
    assert barcode_to_ean8(0x53264c9956cd9b395) is None


if __name__ == '__main__':
    main()
