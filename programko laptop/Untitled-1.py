# def fool(s):
#     y = 0
#     while s > 0:
#         s -= 2
#         y += 1
#     return y
# print(fool(10000000))

def f1(x: int) -> None:
    i = 7
    while i <= x:
        print(i)
        i += 3

def f2(x: int) -> None:
    for i in range(7, x, 3):
        print(i)

def f3(x: int) -> None:
    for i in range(7, x + 1, 3):
        print(i)

o = 16


# f1(15)
f2(o)
f3(o)

1.
a = 0
row = [a for _ in range(2)]
mat = [row for _ in range(2)]
a = 1
mat[0][0] = 7
Které výrazy se na konci tohoto programu vyhodnotí na True?
(Právě dvě správné odpovědi.)
a == 1
mat == [[7, 0], [0, 0]]
mat == [[7, 1], [7, 1]]
mat == [[7, 0], [7, 0]]
a == 7
mat == [[7, 7], [7, 7]]

2.
from turtle import forward, right

def lines(data: list[float]) -> None:
    for i, size in enumerate(data):
        size *= i
        forward(size)
        right(30)
Je tato funkce čistá? Pokud ne, proč?
(Právě jedna správná odpověď.)
Není čistá, protože modifikuje parametr data.
Je čistá.
Není čistá, protože pracuje s čísly typu float.
Není čistá, protože má návratový typ None.
Není čistá, protože pro stejné vstupy může vrátit různé výstupy.
Není čistá, protože má nějaký jiný vedlejší efekt.


3.
def magic_sort(lists: list[list[int]]) -> list[list[int]]:
    magic = [(len(s), i) for i, s in enumerate(lists)]
    magic.sort()
    return [lists[i] for _, i in magic]
Co bude hodnotou výrazu magic_sort([[1, 2, 3], [], [1, 2], [9], [1, 3, 7], [2]])?
(Právě jedna správná odpověď.)
[[], [2], [9], [1, 2], [1, 2, 3], [1, 3, 7]]
[(0, 1), (1, 3), (1, 5), (2, 2), (3, 0), (3, 4)]
[[1, 2, 3], [], [1, 2], [9], [1, 3, 7], [2]]
[[], [1, 2], [1, 2, 3], [1, 3, 7], [2], [9]]
Vyhodnocení tohoto výrazu skončí s chybou.
[[], [9], [2], [1, 2], [1, 2, 3], [1, 3, 7]]
4.
Které z následujících řádků nejsou výrazy?
(Právě dvě správné odpovědi.)
None
3.14
sorted(data)
a += b
data.sort()
správně*return True


5.
Která z následujících tvrzení jsou pravdivá?
(Právě dvě správné odpovědi.)
Datová struktura slovník (dict) je v Pythonu modifikovatelná.
Řadicí algoritmus Select Sort má lineární složitost vzhledem k délce řazeného seznamu.
Celá čísla (typ int) jsou v Pythonu 3 neomezená, tedy můžeme mít libovolně velké celé číslo.
Prvky datové struktury množina (set) jsou vždy seřazeny vzestupně (tj. od nejmenšího po největší).
Prvky datové struktury množina (set) jsou vždy seřazeny sestupně (tj. od největšího po nejmenší).
Abstraktní datová struktura zásobník pracuje na principu FIFO (first in, first out), tedy při výběru prvku dostaneme vždy ten první vložený.


6.
def supersort(s: list[int]) -> list[int]:
    assert len(s) > 0
    result = s.copy()
    current = result[0]
    for i in range(1, len(result)):
        if result[i] < current:
            result[i] = current
        else:
            current = result[i]
    return result
Máme funkci supersort, jejíž vstupní podmínkou je uvedena u příkazu assert. Které z následujících možností jsou korektními výstupními podmínkami této funkce (tj. platí na konci funkce pro každý vstup splňující vstupní podmínku uvedenou výše)?
(Právě dvě správné odpovědi.)
Seznam result je vzestupně seřazený.
Seznam result obsahuje alespoň dvakrát prvek s[0].
Hodnota prvku result[0] je minimem seznamu result.
Hodnota prvku result[0] je minimem seznamu s.
Seznam result je permutací seznamu s (tj. obsahuje stejné prvky a ve stejném počtu).
Platí len(result) > len(s).


7.
Vyberte výrazy, které se vyhodnotí na požadovanou hodnotu:
1. Předposlední číslice pětkového zápisu kladného celého čísla uloženého v proměnné num.
2. Nový seznam, který obsahuje stejné prvky jako seznam v proměnné lst, ale je seřazený.
(Právě dvě správné odpovědi.)
(num // 5) % 10
sorted(lst)
(num % 25) // 5
(num // 10) % 10
(num % 10) // 5
lst.copy().sort()


8.
def use_your_brain_please(x: int) -> int:
    y = 0
    while x != 0:
        x -= 2
        y += 1
    return y
Co bude hodnotou výrazu use_your_brain_please(1000000000)?
(Právě jedna správná odpověď.)
500000000
500000002
499999999
Vyhodnocení výrazu nikdy neskončí.
499999998
500000001


9.
def fun(a: int, b: int) -> int:
    x, y = a, b
    while x > 0:
        x //= 2
        y //= 2
    return y
Která tvrzení o vztahu mezi vstupy a výstupy této funkce jsou pravdivá?
(Právě dvě správné odpovědi.)
Pokud b > a >= 0, pak fun(a, b) > 0.
Pokud b < a <= 0, pak fun(a, b) < 0.
Pokud a >= b >= 0, pak fun(a, b) == 0.
Pokud b < a <= 0, pak fun(a, b) nikdy neskončí.
Pokud b > a >= 0, pak fun(a, b) == 0.
Pokud a >= b >= 0, pak fun(a, b) < 0.


10.
def f(data: XXX) -> list[int | None]:
    x, y, z = data
    return [x + y, z]
Jakou typovou anotaci je možné napsat místo XXX, aby byla funkce korektně anotovaná?
(Právě dvě správné odpovědi.)
tuple[None, int, None]
tuple[int | None, int | None, int | None]
tuple[int, int, int]
tuple[int | None]
tuple[int, None]
tuple[int, int, None]


11.
def one(fn: str) -> list[str]:
    r = []
    with open(fn, "r") as f:
        for line in f:
            r.extend(two(line))
    return r

def two(line: str) -> list[str]:
    r = []
    three(line, 0, r)
    return r

def three(line: str, i: int, r: list[str]) -> None:
    while i < len(line) and line[i] != '#':
        r.append(line[i])
        i += 1
    print("Line processed.")
Která tvrzení o čistotě těchto funkcí platí?
(Právě dvě správné odpovědi.)
Funkce one není čistá.
Funkce two je čistá, ale funkce three není čistá.
Funkce three je čistá, ale funkce two není čistá.
Ani jedna z funkcí two, three není čistá.
Obě funkce two a three jsou čisté.
Funkce one je čistá.


12.
def f(a: bool, b: bool, c: bool) -> bool:
    if a == True:
        b = True
    elif b == True:
        c = True
    elif c == True:
        a = True
    return a != False and b == True and c != False
Kterému z následujících výrazů je ekvivalentní výraz f(a, b, c)?
(Právě jedna správná odpověď.)
a and b and c
a and c
a and (b or c)
a and not b and c
(a and b) or (a and c) or (b and c)
a and b


13.
a = {1, 2}
b = a | {2}
c = a
a.add(3)
c = {4}
Které výrazy se na konci tohoto programu vyhodnotí na True?
(Právě dvě správné odpovědi.)
a == {1, 2, 3}
*b == {1, 2}
b == {1, 2, 3}
b == {1}
špatněb == {1, 3}
a == {4}


14.
Které z následujících příkazů se vykonají v konstantním čase (tj. nezávislém na velikosti seznamů)? Předpokládejte, že v proměnných data, data1, data2 jsou seznamy takové, aby všechny uvedené příkazy proběhly bez chyb.
(Právě dvě správné odpovědi.)
data2 = data1   
return [x for x in data if x > 0]
middle = data[-len(data) // 2] 
data1.reverse()
data1 = sorted(data2)
data = data1 + data2


15.
def f1(x: int) -> None:
    i = 7
    while i <= x:
        print(i)
        i += 3

def f2(x: int) -> None:
    for i in XXX:
        print(i)
Co musíme doplnit za XXX tak, aby měly obě procedury f1, f2 stejný efekt pro libovolné vstupní x?
(Právě jedna správná odpověď.)
range(7, x + 1, 3)
[i for i = 7 to x step 3]
range(3, x + 1, 7)
Za XXX není možné doplnit nic, co by způsobilo, aby obě procedury f1, f2 měly stejný efekt.
range(3, x, 7)
range(7, x, 3)