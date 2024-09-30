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

def years_visited(ord_of_patient: int,
                  patients: list[tuple[int, list[tuple[int, int, int, int]]]])\
                      -> tuple[int, list[int]]:
    years = []

    patient = patients[ord_of_patient]
    num_of_patient, visit = patient
    for years_of_visits in visit:
        year_of_visit, _, _, _ = years_of_visits
        years.append(year_of_visit)
    return num_of_patient, years


def all_patients(lst_patients: list[int],
                 patients: list[tuple[int, list[tuple[int, int, int, int]]]])\
                     -> list[int]:
    lst = []
    add = True
    for i in range(len(patients)):
        num_of_patient, _ = years_visited(i, patients)
        for element in lst_patients:
            if element == num_of_patient:
                add = False
        if add:
            lst.append(num_of_patient)
        add = True

    return lst


def missing_visits(year: int, patients:
                   list[tuple[int, list[tuple[int, int, int, int]]]])\
                       -> list[int]:

    lst_patients = []
    count = year

    for i in range(len(patients)):
        num_of_patient, lst = years_visited(i, patients)

        for element in lst:
            count = year + 1

            for k in range(20):
                if count == element:
                    lst_patients.append(num_of_patient)
                count += 1

    final = all_patients(lst_patients, patients)
    return final


# Dále napište a otypujte funkci ‹patient_reports›, která vrátí
# seznam zpráv o pacientech. Zpráva o pacientovi je čtveřice, která
# obsahuje záznam o jeho nejvyšším doposud naměřeném pulzu a pro
# každou měřenou hodnotu informaci, zda se měření dané hodnoty
# v jednotlivých letech konzistentně zvyšují (‹True› nebo ‹False›).

# Například zpráva o pacientovi ‹(1, [(2015, 91, 120, 80), (2018,
# 89, 125, 82), (2020, 93, 120, 88)])› je ‹(93, False, False,
# True)›.


# def years_visited(ord_of_patient, patients):
#     patient = patients[ord_of_patient]


def patient_reports(patients:
                    list[tuple[int, list[tuple[int, int, int, int]]]])\
                        -> list[tuple[int, bool, bool, bool]]:
    lst = []
    max_pulse, prev_pulse, prev_out, prev_into = 0, 2000, 2000, 2000
    pulse_check, out_check, into_check = True, True, True

    for element in patients:
        _, visits = element

        for visit in visits:

            _, pulse, out, into = visit

            if pulse > max_pulse:
                max_pulse = pulse
            if pulse <= prev_pulse and prev_pulse != 2000:
                pulse_check = False
            prev_pulse = pulse

            if out <= prev_out and prev_out != 2000:
                out_check = False
            prev_out = out

            if into <= prev_into and prev_into != 2000:
                into_check = False
            prev_into = into

        final = (max_pulse, pulse_check, out_check, into_check)
        lst.append(final)

        max_pulse, prev_pulse, prev_out, prev_into = 0, 2000, 2000, 2000
        pulse_check, out_check, into_check = True, True, True

    return lst



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
