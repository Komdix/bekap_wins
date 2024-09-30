from ib111 import week_06  # noqa


# V této úloze budete zjišťovat, je-li možné pomocí alchymie vyrobit
# požadovanou substanci. Vstupem je:
#
#  • množina substancí, které již máte k dispozici (máte-li už
#    nějakou substanci, máte ji k dispozici v neomezeném množství),
#  • slovník, který určuje, jak lze existující substance
#    transmutovat: klíčem je substance kterou můžeme vytvořit a
#    hodnotou je seznam „vstupních“ substancí, které k výrobě
#    potřebujeme,
#  • cílová substance, kterou se pokoušíme vyrobit.
#
# Napište predikát, kterého hodnota bude ‹True›, lze-li z daných
# substancí podle daných pravidel vytvořit substanci požadovanou,
# ‹False› jinak.


def control(needed: set[str], owned: list[str]) -> bool:
    need = 0

    for element in needed:
        if element in owned:
            need += 1
    return need == len(needed)


def is_creatable(owned_substances: set[str],
                 rules: dict[str, set[str]], wanted: str) -> bool:

    if wanted in owned_substances:
        return True
    if rules == {}:
        return False

    needed = rules.get(wanted)
    creatable = list(rules.keys())
    owned = list(owned_substances)

    assert needed is not None
    needed_control = control(needed, owned)
    
    if needed_control:
        return True

    for element in creatable:
        ingredients = rules.get(element)
        assert ingredients is not None
        break
        ingredients_control = control(ingredients, owned)
        if ingredients_control:
            owned.append(element)

    return wanted in owned


def main() -> None:
    assert is_creatable({"a"}, {}, "a")
    assert is_creatable({"a", "b"}, {"c": {"a", "b"}}, "c")
    assert is_creatable({"a", "b"}, {"c": {"a"}, "d": {"c"}}, "d")
    assert is_creatable({"a", "b"}, {"c": {"a", "b"}, "d": {"a", "c"},
                                     "e": {"d", "b"}, "f": {"e", "a"}}, "f")

    owned = {"b", "c", "d"}
    rules = {"a": {"b", "c", "d"},
             "e": {"a", "b", "c", "d"},
             "f": {"a", "b", "c", "d", "e"}}

    assert is_creatable(owned, rules, "f")
    assert owned == {"b", "c", "d"}
    assert rules == {"a": {"b", "c", "d"},
                     "e": {"a", "b", "c", "d"},
                     "f": {"a", "b", "c", "d", "e"}}

    assert not is_creatable({"a"}, {"c": {"a", "b"}}, "c")
    assert not is_creatable(set(), {"c": {"a", "b"}}, "c")
    assert not is_creatable({"a", "b"}, {}, "c")

    owned = {"a", "b"}
    rules = {"c": {"a", "b"}, "d": {"a", "c"},
             "e": {"d", "b"},
             "f": {"e", "a", "h"}}
    assert not is_creatable(owned, rules, "f")
    assert owned == {"a", "b"}
    assert rules == {"c": {"a", "b"}, "d": {"a", "c"},
                     "e": {"d", "b"},
                     "f": {"e", "a", "h"}}


if __name__ == '__main__':
    main()
