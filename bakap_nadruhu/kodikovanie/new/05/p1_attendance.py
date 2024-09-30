from ib111 import week_05  # noqa


# V tomto příkladu budeme pracovat se systémem docházky jedné
# fiktivní firmy. Při příchodu do práce si musí každý zaměstnanec
# pípnout kartičkou u vchodu a zaznamenat tak svůj příchod. Při
# odchodu zase stejně musí zaznamenat, že z práce odešel.

# Čidlo u dveří pak do firemního systému zaznamená data o docházce
# zaměstnance. Každý záznam je trojice obsahující kód zaměstnance,
# časovou známku a typ záznamu - příchod nebo odchod.

EmployeeId = str  # kód zaměstnance
TimeStamp = int  # počet sekund od nějakého pevného bodu
RecordType = bool  # typ záznamu

ENTRY = True
LEAVE = False

MachineRecord = tuple[EmployeeId, TimeStamp, RecordType]


# Bohužel, někteří zaměstnanci zapomínají zaznamenávat svou
# docházku. Vaším úkolem je napsat čistou funkci
# ‹employees_with_missing_records›, která projde seznam záznamů, a
# vrátí množinu obsahující kódy těch zaměstnanců, pro které existuje
# v seznamu nějaká nesrovnalost – buď z práce odešli, aniž by do ní
# přišli, nebo přišli do práce vícekrát bez záznamu o odchodu.
# Seznam záznamů začíná v situaci, kdy žádný zaměstnanec v práci není.
# Můžete počítat s tím, že seznam je seřazený podle času od
# nejstaršího záznamu po nejnovější.

def employees_with_missing_records(
        records: list[MachineRecord]) -> set[EmployeeId]:
    pass


def main() -> None:
    id1 = "abc00001"
    id2 = "xyz00002"
    id3 = "hjkl0003"

    e1 = (id1, 100, ENTRY)
    e2 = (id2, 110, ENTRY)
    e3 = (id3, 140, ENTRY)
    e4 = (id1, 200, ENTRY)
    e5 = (id1, 300, ENTRY)

    l1 = (id1, 150, LEAVE)
    l2 = (id2, 160, LEAVE)
    l3 = (id3, 210, LEAVE)
    l4 = (id1, 250, LEAVE)
    l5 = (id2, 270, LEAVE)

    # no missing records
    m1 = employees_with_missing_records([])
    assert len(m1) == 0

    m2 = employees_with_missing_records([e1, l1])
    assert len(m2) == 0

    m3 = employees_with_missing_records([e1, e2, l1, l2, e4])
    assert len(m3) == 0

    m4 = employees_with_missing_records([e1, e3, l1, e4, l3, l4])
    assert len(m4) == 0

    # missing records
    m5 = employees_with_missing_records([e1, l1, e4, e5])
    assert len(m5) == 1
    assert id1 in m5

    m6 = employees_with_missing_records([e1, e2, l1, l2, l5])
    assert len(m6) == 1
    assert id2 in m6

    m7 = employees_with_missing_records([e1, e4, l5])
    assert len(m7) == 2
    assert id1 in m7
    assert id2 in m7


if __name__ == "__main__":
    main()
