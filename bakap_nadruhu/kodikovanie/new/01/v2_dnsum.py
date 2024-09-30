from ib111 import week_01  # noqa


# Napište čistou funkci ‹sum_elements_dn›, která vrátí součet
# prvních ‹count› prvků vzestupně seřazené posloupnosti kladných
# celých čísel, která jsou dělitelná číslem ‹div› a zároveň nejsou
# dělitelná číslem ‹nondiv›. Předpokládejte, že všechny parametry
# jsou kladná celá čísla a že číslo ‹div› není dělitelné číslem
# ‹nondiv›. (Můžete zkusit přemýšlet, co by se stalo v takovém
# případě.)

def sum_elements_dn(div, nondiv, count):
    pass


def main():
    assert sum_elements_dn(3, 2, 7) == 147
    assert sum_elements_dn(6, 4, 5) == 150
    assert sum_elements_dn(10, 6, 11) == 910


if __name__ == '__main__':
    main()
