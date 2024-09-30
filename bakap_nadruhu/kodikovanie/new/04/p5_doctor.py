from ib111 import week_04  # noqa


# V této úloze bude Vaším úkolem implementovat funkce pracující se
# seznamem pacientů ‹patients› u lékaře. Každý pacient má záznam
# (dvojici), který obsahuje jeho unikátní identifikátor a seznam
# návštěv s výsledky. Návštěva je reprezentovaná čtveřicí – rokem,
# kdy pacient navštívil lékaře, a naměřenými hodnotami: pulz,
# systolický a diastolický tlak. Seznam návštěv pacienta je
# uspořádaný vzestupně od nejstarší. Můžete předpokládat, že každý
# pacient má alespoň jeden záznam.

# Vaším prvním úkolem bude implementovat a otypovat funkci
# ‹missing_visits›, která zjistí, kteří pacienti nebyli na prohlídce
# od roku ‹year›. Jako výsledek vraťte seznam identifikátorů
# pacientů.

def missing_visits(year, patients):
    pass


# Dále napište a otypujte funkci ‹patient_reports›, která vrátí
# seznam zpráv o pacientech. Zpráva o pacientovi je čtveřice, která
# obsahuje záznam o jeho nejvyšším doposud naměřeném pulzu a pro
# každou měřenou hodnotu informaci, zda se měření dané hodnoty
# v jednotlivých letech konzistentně zvyšují (‹True› nebo ‹False›).

# Například zpráva o pacientovi ‹(1, [(2015, 91, 120, 80), (2018,
# 89, 125, 82), (2020, 93, 120, 88)])› je ‹(93, False, False,
# True)›.

def patient_reports(patients):
    pass


def main() -> None:
    p1 = (0, [(2016, 102, 140, 95)])
    p2 = (1, [(2015, 91, 120, 80), (2018, 89, 125, 82),
              (2020, 93, 120, 88)])
    p3 = (2, [(2010, 73, 110, 70), (2015, 75, 112, 70),
              (2017, 76, 114, 71), (2019, 79, 116, 72)])
    p4 = (3, [(2016, 82, 115, 82), (2017, 83, 117, 80)])
    p5 = (4, [(2005, 81, 130, 90), (2007, 81, 130, 90),
              (2011, 80, 130, 90), (2013, 81, 130, 90),
              (2017, 82, 130, 90)])

    p6 = (5, [(2000, 74, 120, 80), (2011, 107, 142, 95),
              (2012, 94, 140, 97)])
    p7 = (6, [(2019, 101, 145, 95), (2020, 101, 145, 95)])

    patients = [p1, p2, p3, p4, p5]
    assert missing_visits(2017, patients) == [0, 3, 4]
    assert missing_visits(2016, patients) == [0]
    assert missing_visits(2000, patients) == []

    assert patient_reports(patients) == \
        [(102, True, True, True), (93, False, False, True),
         (79, True, True, False), (83, True, True, False),
         (82, False, False, False)]

    assert patient_reports([p6, p7]) == \
        [(107, False, False, True), (101, False, False, False)]


if __name__ == "__main__":
    main()
