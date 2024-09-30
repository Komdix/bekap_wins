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

def is_creatable(owned_substances: set[str],
                 rules: dict[str, set[str]], wanted: str) -> bool:
    pass


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
