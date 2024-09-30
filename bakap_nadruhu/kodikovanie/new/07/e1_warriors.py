from ib111 import week_07  # noqa


# Třída ‹Warrior› reprezentuje válečníka, který má jméno a sílu.
# Tyto jeho vlastnosti bude třída reprezentovat atributy ‹name› a
# ‹strength›. Tato třída obsahuje pouze inicializační funkci ‹__init__›.

class Warrior:
    def __init__(self, name: str, strength: int) -> None:
        self.name = name
        self.strength = strength


# Velké množství válečníků tvoří hordu, kterou reprezentujeme třídou
# ‹Horde›. Horda má interní strukturu – je rozdělena do
# pojmenovaných klanů, které reprezentujeme slovníkem (jméno klanu,
# seznam válečníků).

class Horde:

    # Vytvoří hordu se zadanými klany.

    def __init__(self, clans: dict[str, list[Warrior]]) -> None:
        pass

    # Metoda vrátí aktuální stav hordy, t.j. slovník všech klanů.

    def clans(self) -> dict[str, list[Warrior]]:
        pass

    # Metoda přidá válečníka do klanu. Neexistuje-li klan daného
    # jména, metoda jej vytvoří.

    def add_warrior(self, clan: str, warrior: Warrior) -> None:
        pass

    # Metoda (a zároveň predikát) zkontroluje, má-li každý klan
    # dostatečnou sílu, která je rovna součtu sil všech jeho válečníků.
    # Měl by vám stačit nanejvýš jeden průchod seznamy válečníků.

    def validate_clan_strength(self, required: int) -> bool:
        pass


def main() -> None:
    noname = Warrior('Noname', 12)
    assert noname.name == 'Noname'
    assert noname.strength == 12

    achilleus = Warrior('Achilleus', 1000)
    patrokles = Warrior('Patrokles', 700)

    horde = Horde({"peasants": [noname]})
    assert horde.clans() == {"peasants": [noname]}
    assert horde.validate_clan_strength(10)
    assert not horde.validate_clan_strength(13)

    horde.add_warrior("heroes", achilleus)
    horde.add_warrior("heroes", patrokles)
    assert horde.clans() == {"peasants": [noname],
                             "heroes": [achilleus, patrokles]}
    assert not horde.validate_clan_strength(50)

    empty_horde = Horde({})
    assert empty_horde.validate_clan_strength(100)
    assert empty_horde.validate_clan_strength(1)

    empty_horde = Horde({"empty_clan": []})
    assert not empty_horde.validate_clan_strength(100)
    assert not empty_horde.validate_clan_strength(1)


if __name__ == "__main__":
    main()
