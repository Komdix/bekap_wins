from ib111 import week_03  # noqa


# V této úloze naprogramujeme trojici (čistých) funkcí, které slouží
# pro práci s číselnými soustavami. Reprezentaci čísla v nějaké
# číselné soustavě budeme ukládat jako dvojici ‹(base, digits)›, kde
# ‹base› je hodnota typu ‹int›, která reprezentuje základ soustavy,
# a ‹digits› je seznam cifer v této soustavě, kde každý prvek je
# hodnota typu ‹int›, která spadá do rozsahu [0, ‹base› - 1]. Index
# seznamu ‹digits› odpovídá příslušné mocnině ‹base›. Například:
#
#  • ‹(10, [2, 9])› je zápis v desítkové soustavě a interpretujeme
#    jej jako ‹2 * 1 + 9 * 10›, co odpovídá číslu ‹92›
#  • ‹(7, [2, 1])› je zápis v sedmičkové soustavě a kóduje
#    ‹2 * 1 + 1 * 7 = 9›

# První funkce implementuje převod čísla ‹number› do ciferné
# reprezentace v soustavě se základem ‹base›:

def to_digits(number, base):
    n = number
    lst = []
    while n > 0:
        reduction = n
        n = n // base
        reduction = reduction - (n * base )
        lst.append(reduction)
    return(base, lst)


# Další funkce provádí převod opačným směrem, z ciferné
# reprezentace ‹number› vytvoří hodnotu typu ‹int›:

def from_digits(number):
    base, lst = number
    num = lst[0] * 1
    for i in range(1,len(lst)):
        num += lst[i] * base
    return num
    


# Konečně funkce ‹convert_digits› převede ciferný zápis z jedné
# soustavy do jiné soustavy. Nápověda: tato funkce je velmi
# jednoduchá.

def convert_digits(number, base):
    num = from_digits(number)
    converted = to_digits(num, base)
    return converted







s = convert_digits((16, [1, 2]), 10)
print(s)

