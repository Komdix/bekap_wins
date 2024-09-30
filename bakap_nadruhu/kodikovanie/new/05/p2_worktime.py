from ib111 import week_05  # noqa


# V tomto příkladu budeme opět pracovat se systémem docházky (data
# mají stejný formát i význam).

EmployeeId = str  # kód zaměstnance
TimeStamp = int  # počet sekund od nějakého pevného bodu
RecordType = bool  # typ záznamu

ENTRY = True
LEAVE = False

MachineRecord = tuple[EmployeeId, TimeStamp, RecordType]


# Na základě odpracovaných hodin za jeden měsíc firma počítá mzdu
# pro zaměstnance. Napište čistou funkci ‹seconds_spent_working›,
# která zjistí, kolik sekund každý zaměstnanec odpracoval. Můžete
# počítat s tím, že vstupní seznam je seřazený podle časových známek
# od nejstaršího záznamu po nejnovější, že se v něm nevyskytují
# žádné nesrovnalosti, že záznamy začínají v situaci, kdy žádný zaměstnanec
# v práci není a že každý zaměstnanec, který do práce přišel, z ní také
# později odešel.

# Nápověda: odečtením dvou časových známek zjistíte, kolik sekund
# uplynulo mezi nimi.

def seconds_spent_working(
        records: list[MachineRecord]) -> dict[EmployeeId, int]:
    pass


def main() -> None:
    id1 = "abc00001"
    id2 = "xyz00002"
    id3 = "hjkl0003"

    e1 = (id1, 100, ENTRY)
    e2 = (id2, 110, ENTRY)
    e3 = (id3, 140, ENTRY)
    e4 = (id1, 200, ENTRY)

    l1 = (id1, 150, LEAVE)
    l2 = (id2, 160, LEAVE)
    l3 = (id3, 210, LEAVE)
    l4 = (id1, 250, LEAVE)

    t1 = seconds_spent_working([e1, l1])
    assert len(t1) == 1
    assert t1[id1] == 50

    t2 = seconds_spent_working([e2, e3, l2, l3])
    assert len(t2) == 2
    assert t2[id2] == 50
    assert t2[id3] == 70

    t3 = seconds_spent_working([e1, l1, e4, l4])
    assert len(t3) == 1
    assert t3[id1] == 100

    t4 = seconds_spent_working([e1, e2, e3, l1, l2, e4, l3, l4])
    assert len(t4) == 3
    assert t4[id1] == 100
    assert t4[id2] == 50
    assert t4[id3] == 70


if __name__ == "__main__":
    main()
