from ib111 import week_09  # noqa

# V této úloze budeme pracovat se stromovou strukturou představující
# jednoduchý rodokmen, který má jednu výchozí osobu, její potomky, potomky
# jejích potomků atd. (V českém genealogickém názvosloví se tento strom
# správně nazývá „rozrod“.)
#
# Osoby v rodokmenu budou reprezentovány třídou ‹Person›, každá osoba má
# své jméno (atribut ‹name›), rok narození (atribut ‹birth_year›) a seznam
# dětí (atribut ‹children›). Za „rodokmen osoby“ považujeme vždy tu část
# rodokmenu, která obsahuje danou osobu samotnou a všechny její potomky,
# přímé i nepřímé.
#
# Předpokládejte, že rodokmen je vždy korektní stromovou strukturou,
# tj. nikdo v rodokmenu nemá více než jednoho rodiče, nejsou v něm žádné
# cyklické vztahy (např. že by někdo byl svým vlastním potomkem) apod.
#
# Následující řetězcové konstanty neměňte, jsou určeny pro vykreslování
# rodokmenu (viz metodu ‹to_picture› níže). Totéž se týká typového aliasu
# ‹Picture›.

Picture = dict[tuple[int, int], 'str | Person']
FORK = "├─ "
LINE = "│  "
BEND = "└─ "


class Person:

    # Inicializační funkci nemodifikujte.

    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year
        self.children: list[Person] = []

    # Metoda-predikát ‹is_valid› rozhodne, zda rodokmen osoby splňuje tyto
    # podmínky:
    #
    # • jméno žádné osoby není prázdné;
    # • každý rodič se narodil dříve než jeho děti;
    # • žádní dva sourozenci nemají stejné jméno.

    def is_valid(self) -> bool:
        if not self.name:
            return False
        for child in self.children:
            if child.birth_year <= self.birth_year:
                return False

        names = []

        for child in self.children:
            if child.name in names:
                return False
            names.append(child.name)

        for child in self.children:
            if not child.is_valid():
                return False

        return True

    # Rodokmen budeme chtít (textově) vykreslit, a to dle tohoto vzoru:
    #
    #      Qempa' (2256)
    #      ├─ Thok Mak (2281)
    #      │  ├─ Ag'ax (2317)
    #      │  ├─ K'alaga (2302)
    #      │  └─ Samtoq (2317)
    #      └─ Worf (2290)
    #         └─ Mogh (2310)
    #            ├─ Worf (2340)
    #            │  ├─ K'Dhan (2388)
    #            │  └─ Alexander Rozhenko (2366)
    #            │     └─ D'Vak (2390)
    #            └─ Kurn (2345)
    #               ├─ Grehka (2359)
    #               ├─ Elumen (2357)
    #               └─ Ga'ga (2366)
    #
    # Samotná vykreslovací procedura ‹draw_picture› je níže připravena, vy
    # pouze implementujete čistou metodu ‹to_picture›, která určí jak má
    # obrázek vypadat. Obrázek je dán slovníkem, jehož klíči jsou souřadnice
    # a hodnotami buď konektory nebo osoby. Konektory jsou konstanty ‹FORK›
    # (větvení), ‹LINE› (rovná čára) a ‹BEND› (zahnutá čára). Souřadnice
    # levého horního rohu obrázku jsou (0, 0); x-ová (první) souřadnice se
    # zvyšuje směrem doprava – a to tak, že každá jednotka znamená posun
    # o šířku jednoho konektoru; y-ová (druhá) souřadnice se zvyšuje směrem
    # dolů. Například osoba jménem «Alexander Rozhenko» je umístěna na
    # souřadnicích (4, 9).
    #
    # Pro obrázek musí platit:
    #
    # • počáteční osoba se vykreslí v levém horním rohu;
    # • svislá čára (tvořená konektory ‹LINE›, ‹FORK›, ‹BEND›) sahá vždy jen
    #   tak daleko, jak je třeba;
    # • pořadí vypisování dětí je pořadí dané seznamem ‹children›.

    def to_picture(self) -> Picture:
        picture: Picture = {(0, 0): self}
        self.make_picture(0, 0, picture)
        self.draw_lines(-1 ,0,picture)
        return picture

    def make_picture(self, x: int, y: int, picture: Picture)\
            -> tuple[Picture, int]:
        if self.children is None:
            return None
        picture[(x, y)] = self
        x += 1
        for child in self.children:
            y += 1
            picture, y = child.make_picture(x, y, picture)
        return picture, y
    
    def draw_lines(self, x, y, picture):
        if self.children is None:
            return None
        
        child_num = 0   
        for child in self.children:
            child_num += 1
        if self.children is not None:

        if child_num > 1:
            # print(x, y)
            picture[x, y] = FORK

            # for child in child.children:
            #     child.draw_lines(x,y,picture)


        elif child_num == 1:
            print(x, y)
            picture[x, y] = BEND
            child.draw_lines(x,y,picture)
            # child_num += 1
        
        x += 1
        for child in self.children:
                y += 1
                child.draw_lines(x, y, picture)
        return picture, y
            

        
        
    # Čistá metoda ‹order_of_succession› dostane na vstupu množinu žijících
    # osob ‹alive› a vrátí slovník, který každé osobě přiřadí pořadí
    # následnictví (podobně jako u královských rodů). Přitom uvažujeme tzv.
    # absolutní primogenituru – nerozlišujeme pohlaví osob (ani nemáme jak)
    # a přednost má vždy nejstarší potomek. Jsou-li dva potomci stejně staří
    # (narozeni ve stejném roce), přednost má ten, který je uveden dřív
    # v seznamu ‹children›. (Podrobnější vysvětlení a příklad je níže.)

    def order_of_succession(self, alive: set['Person']) \
            -> dict['Person', int]:
        if not self.alive_descendant(alive):
            return {}
        order: dict['Person', int] = {}
        order_num = [1]
        first = self
        order = self.assigning_the_order(alive, order, order_num, first)

        return order

    def assigning_the_order(self, alive: set['Person'],
                            order: dict['Person', int],
                            order_num: list[int], first: 'Person')\
            -> dict['Person', int]:
        if self.children is None:
            return None

        siblings_order = []
        children = []
        lst = []

        for child in self.children:
            children.append(child)
            siblings_order.append(child.birth_year)

        sorted_years = sorted(siblings_order)

        for year in sorted_years:
            lst.append(children[siblings_order.index(year)])
            children.pop(siblings_order.index(year))
            siblings_order.pop(siblings_order.index(year))

        if self != first and self in alive:
            order[self] = order_num[0]
            order_num[0] += 1
        for child in lst:
            child.assigning_the_order(alive, order, order_num, first)
        return order

    # Metoda ‹remove_extinct_branches› dostane opět na vstupu množinu
    # žijících osob a odstraní z rodokmenu všechny vyhynulé větve,
    # tj. osoby, které již nežijí ani nemají žádné (ani nepřímé) žijící
    # potomky. Zpracováváme přitom pouze podstrom aktuální osoby – tuto
    # osobu samotnou z rodokmenu neodstraňujeme (ani nemáme jak).

    # def remove_extinct_branches(self, alive: set['Person']) -> None:
    #     self.children = []
    #     for child in self.children:
    #         child.remove_extinct_branches(alive)

    #     print("begin")
    #     if self not in alive and self.alive_descendant(alive) == False:
    #         # print(child.alive_descendant(alive),"kek")
    #         for child in self.children:
    #             self.children.pop(self)
    

# def has_alive_descendant(self, alive: set['Person']) -> bool:
#     """ Check if this person or any descendants are in the alive set. """
#     if self in alive:
#         return True
#     return any(child.has_alive_descendant(alive) for child in self.children)


                
                
            

    def alive_descendant(self, alive: set['Person']) -> bool:
        for child in self.children:
            if child in alive or child.alive_descendant(alive):
                return True
        return False

# «Poznámka» – pořadí následnictví (absolutní primogenitura):
#
# Pořadí následnictví podle tzv. absolutní primogenitury funguje podle těchto
# principů: (a) Přednost má vždy starší potomek před mladším. (b) Děti
# nahrazují rodiče, tj. potomci osoby mají přednost před jejími sourozenci.
#
# Ukážeme si to na příkladu rodokmenu výše. Nejprve předpokládejme, že
# všechny zmíněné osoby stále žijí. Následníci výchozí osoby («Qempa'») mají
# toto pořadí:
#
# 1. «Thok Mak» je nejstarším potomkem. Je tedy prvním následníkem.
# 2. «K'alaga» je nestarším potomkem prvního následníka. Protože potomci mají
#    přednost před sourozenci, je druhým následníkem.
# 3. «Ag'ax» je dalším v pořadí («K'alaga» žádné potomky nemá a ačkoli
#    «Ag'ax» a «Samtoq» jsou stejně staří, «Ag'ax» je v seznamu dětí dříve).
# 4. «Samtoq»
# 5. «Worf (2290)» je dalším potomkem výchozí osoby. (Už jsme vyčerpali
#    všechny potomky prvního následníka.)
# 6. «Mogh» je jediným potomkem.
# 7. «Worf (2340)» je nejstarším potomkem osoby «Mogh».
# 8. «Alexander Rozhenko» je nestarším potomkem osoby «Worf (2340)».
#    (Opět vidíme, že má přednost potomek před sourozencem.)
# 9. «D'Vak» (opět přednost potomka před sourozencem)
# 10. «K'Dhan»
# 11. «Kurn» (po vyčerpání všech potomků jeho sourozence)
# 12. «Elumen»
# 13. «Grehka»
# 14. «Ga'ga»
#
# V případě, že některé osoby již nežijí, vyloučíme je z pořadí následnictví,
# ale jejich potomky ponecháme. Pokud tedy předpokládáme, že již nejsou
# naživu osoby «Qempa'», «Thok Mak», «Worf (2290)», «Mogh» a «Kurn», pořadí
# následníků osoby «Qempa'» je toto:
#
# 1. «K'alaga»
# 2. «Ag'ax»
# 3. «Samtoq»
# 4. «Worf (2340)»
# 5. «Alexander Rozhenko»
# 6. «D'Vak»
# 7. «K'Dhan»
# 8. «Elumen»
# 9. «Grehka»
# 10. «Ga'ga»
#
# Pokud by nás zajímalo pouze následnictví osoby «Mogh», pak je pořadí toto:
#
# 1. «Worf (2340)»
# 2. «Alexander Rozhenko»
# 3. «D'Vak»
# 4. «K'Dhan»
# 5. «Elumen»
# 6. «Grehka»
# 7. «Ga'ga»
#
# Odkazy:
#
# • ‹https://en.wikipedia.org/wiki/Primogeniture#Absolute_primogeniture›
# • ‹https://en.wikipedia.org/wiki/Succession_to_the_British_throne›
#   (příklad pořadí následnictví – pozor ovšem na to, že do roku 2011
#   fungovala v Británii mužská primogenitura, kde měli synové přednost před
#   dcerami nezávisle na věku)


def main() -> None:
    adam = Person("Adam", 1)
    assert adam.name == "Adam"
    assert adam.birth_year == 1
    assert adam.children == []

    assert adam.is_valid()
    assert adam.order_of_succession({adam}) == {}
    assert adam.order_of_succession(set()) == {}

    qempa = Person("Qempa'", 2256)
    thok_mak = Person("Thok Mak", 2281)
    worf1 = Person("Worf", 2290)
    ag_ax = Person("Ag'ax", 2317)
    k_alaga = Person("K'alaga", 2302)
    samtoq = Person("Samtoq", 2317)
    mogh = Person("Mogh", 2310)
    worf2 = Person("Worf", 2340)
    kurn = Person("Kurn", 2345)
    k_dhan = Person("K'Dhan", 2388)
    alex = Person("Alexander Rozhenko", 2366)
    d_vak = Person("D'Vak", 2390)
    grehka = Person("Grehka", 2359)
    elumen = Person("Elumen", 2357)
    ga_ga = Person("Ga'ga", 2366)

    qempa.children = [thok_mak, worf1]
    thok_mak.children = [ag_ax, k_alaga, samtoq]
    worf1.children = [mogh]
    mogh.children = [worf2, kurn]
    worf2.children = [k_dhan, alex]
    alex.children = [d_vak]
    kurn.children = [grehka, elumen, ga_ga]

    assert qempa.is_valid()
    assert alex.is_valid()

    thok_mak.name = ""
    assert not qempa.is_valid()
    assert alex.is_valid()
    thok_mak.name = "Thok Mak"

    thok_mak.birth_year = 2302
    assert not qempa.is_valid()
    assert alex.is_valid()
    thok_mak.birth_year = 2281

    alive = {qempa, thok_mak, worf1, ag_ax, k_alaga, samtoq, mogh,
             worf2, kurn, k_dhan, alex, d_vak, grehka, elumen, ga_ga}
    succession = {
        thok_mak: 1,
        k_alaga: 2,
        ag_ax: 3,
        samtoq: 4,
        worf1: 5,
        mogh: 6,
        worf2: 7,
        alex: 8,
        d_vak: 9,
        k_dhan: 10,
        kurn: 11,
        elumen: 12,
        grehka: 13,
        ga_ga: 14
    }

    assert qempa.order_of_succession(alive) == succession

    alive.remove(qempa)
    assert qempa.order_of_succession(alive) == succession

    alive.difference_update({thok_mak, worf1, mogh, kurn})
    assert qempa.order_of_succession(alive) == {
        k_alaga: 1,
        ag_ax: 2,
        samtoq: 3,
        worf2: 4,
        alex: 5,
        d_vak: 6,
        k_dhan: 7,
        elumen: 8,
        grehka: 9,
        ga_ga: 10,
    }

    assert mogh.order_of_succession(alive) == {
        worf2: 1,
        alex: 2,
        d_vak: 3,
        k_dhan: 4,
        elumen: 5,
        grehka: 6,
        ga_ga: 7,
    }

    pic = qempa.to_picture()
    # assert pic[4, 9] == alex

    print("Check the picture of the tree yourself:\n")
    draw_picture(pic)

    alive = {ga_ga, elumen, d_vak, worf2, k_dhan, alex}

    print("\nAfter calling remove_extinct_branches:\n")
    qempa.remove_extinct_branches(alive)
    draw_picture(qempa.to_picture())


def draw_picture(pic: Picture) -> None:
    height = 0
    width: dict[int, int] = {}
    for (x, y), _ in pic.items():
        assert x >= 0 and y >= 0, "Negative coordinates not allowed."
        height = max(height, y + 1)
        width[y] = max(width.get(y, 0), x + 1)

    for y in range(height):
        for x in range(width.get(y, 0)):
            item = pic.get((x, y))
            if isinstance(item, Person):
                print(item.name, " (", item.birth_year, ")",
                      sep="", end="")
            else:  # connector or None
                print("   " if item is None else item, end="")
        print()


if __name__ == '__main__':
    main()
