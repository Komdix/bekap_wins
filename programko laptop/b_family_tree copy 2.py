
Picture = dict[tuple[int, int], 'str | Person']
FORK = "├─ "
LINE = "│  "
BEND = "└─ "


class Person:

    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year
        self.children: list[Person] = []

    def is_valid(self) -> bool:
        names = set()

        if not self.name:
            return False
        for child in self.children:
            if child.birth_year <= self.birth_year:
                return False
            if child.name in names:
                return False
            names.add(child.name)
            if not child.is_valid():
                return False

        return True


    def to_picture(self) -> Picture:
        picture: Picture = {(0, 0): self}
        self.make_picture(0, 0, picture)
        self.draw_lines(-1, 0, picture, self.children)
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

    def line(self, x: int, y: int, picture: Picture) -> None:
        while (x, y) not in picture:
            picture[(x, y)] = LINE
            y -= 1

    def draw_lines(self, x: int, y: int, picture: Picture,
                   parent: list['Person']) -> tuple[Picture, int]:
        if self.children is None:
            return None

        if self.children is not None and x > -1:

            if self != parent[-1]:
                picture[(x, y)] = FORK
                self.line(x, y - 1, picture)

            else:
                picture[(x, y)] = BEND
                self.line(x, y - 1, picture)

        x += 1
        for child in self.children:
            y += 1
            picture, y = child.draw_lines(x, y, picture, self.children)
        return picture, y

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

        siblings_birth_year = []
        children = []
        lst = []

        for child in self.children:
            children.append(child)
            siblings_birth_year.append(child.birth_year)

        sorted_children = sorted(self.children, key=lambda child: child.birth_year)

        for child in sorted_children:
            child.assigning_the_order(alive, order, order_num, first)

        if self != first and self in alive:
            order[self] = order_num[0]
            order_num[0] += 1
        for child in lst:
            child.assigning_the_order(alive, order, order_num, first)
        return order

    def remove_extinct_branches(self, alive: set['Person']) -> None:
        for i in range(len(self.children) - 1, -1, -1):
            child = self.children[i]
            child.remove_extinct_branches(alive)

            if child not in alive and not child.alive_descendant(alive):
                self.children.pop(i)

    def alive_descendant(self, alive: set['Person']) -> bool:
        for child in self.children:
            if child in alive or child.alive_descendant(alive):
                return True
        return False

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
    assert pic[4, 9] == alex

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
