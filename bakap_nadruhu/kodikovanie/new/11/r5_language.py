from ib111 import week_11  # noqa


# Jednou z možností, jak poznat v jakém (přirozeném) jazyce je
# nějaký dokument napsaný, je jednoduchá statistická analýza.
# Napište funkci, která dostane jako parametr slovník ‹lang_freq› a
# název souboru ‹text_file›:
#
#  1. ‹lang_freq› bude pro každý jazyk obsahovat slovník tvaru ‹{
#     'a': 357907, 'b': 113756, … }› kde hodnota u každého písmene
#     je počet jeho výskytů v nějakém reprezentativním dokumentu,
#  2. soubor ‹text_file› je textový soubor, kterého jazyk chceme
#     určit.
#
# Jazyk určujte tak, že spočítáte frekvence jednotlivých písmen
# v souboru ‹text_file› a srovnáte je s těmi uloženými ve slovníku
# ‹lang_freq›.
#
# Jak nalezneme nejlepší shodu? Informace o frekvenci písmen
# v nějakém dokumentu lze chápat jako vektory v 26-rozměrném
# prostoru (resp. vícerozměrném, uvažujeme-li písmena s diakritikou,
# ale přesná dimenze není podstatná). Za nejpodobnější budeme
# považovat vektory, které svírají nejmenší úhel. Tento získáte ze
# vztahu ⟦ a⋅b = |a|⋅|b|⋅\cos θ ⟧ (kde na levé straně je běžný
# skalární součin, „absolutní hodnoty“ na straně pravé jsou pak
# délky, které zjistíte ze vztahu ⟦ |a|² = a⋅a ⟧).


def recognize_language(lang_freq: dict[str, dict[str, int]],
                       text_file: str) -> str:
    pass


def main() -> None:
    lang_freq = {
        "english": {"a": 8167, "b": 1492, "c": 2782, "d": 4253, "e":
                    12702, "f": 2228, "g": 2015, "h": 6094, "i":
                    6966, "j": 153, "k": 772, "l": 4025, "m": 2406,
                    "n": 6749, "o": 7507, "p": 1929, "q": 95, "r":
                    5987, "s": 6327, "t": 9056, "u": 2758, "v": 978,
                    "w": 2360, "x": 150, "y": 1947, "z": 74},
        "german": {"a": 6516, "b": 1886, "c": 2732, "d": 5076, "e":
                   16396, "f": 1656, "g": 3009, "h": 4577, "i":
                   6550, "j": 268, "k": 1417, "l": 3437, "m": 2534,
                   "n": 9776, "o": 2594, "p": 670, "q": 18, "r":
                   7003, "s": 7270, "t": 6154, "u": 4166, "v": 846,
                   "w": 1921, "x": 34, "y": 39, "z": 1134},
        "spanish": {"a": 11525, "b": 2215, "c": 4019, "d": 5010,
                    "e": 12181, "f": 692, "g": 1768, "h": 703, "i":
                    6247, "j": 493, "k": 11, "l": 4967, "m": 3157,
                    "n": 6712, "o": 8683, "p": 2510, "q": 877, "r":
                    6871, "s": 7977, "t": 4632, "u": 2927, "v":
                    1138, "w": 17, "x": 215, "y": 1008, "z": 467},
        "czech": {"a": 8421, "b": 822, "c": 740, "d": 3475, "e":
                  7562, "f": 84, "g": 92, "h": 1356, "i": 6073, "j":
                  1433, "k": 2894, "l": 3802, "m": 2446, "n": 6468,
                  "o": 6695, "p": 1906, "q": 1, "r": 4799, "s": 5212,
                  "t": 5727, "u": 2160, "v": 5344, "w": 16, "x": 27,
                  "y": 1043, "z": 1599}
    }

    lang_samples = [("english",
                     "Python is a great programming language. " +
                     "We love Python. And we love our school " +
                     "and learning." +
                     "And we apperently need more text, so that " +
                     "we will hopefully successfuly recognize " +
                     "english, as intended in the first place."),

                    ("german",
                     "Python ist eine großartige Programmiersprache." +
                     "Wir lieben Python. Und wir lieben unsere " +
                     "Schule und das Lernen."),

                    ("spanish",
                     "Python es un gran lenguaje de programación. " +
                     "Nos encanta Python. Y amamos " +
                     "nuestra escuela y nuestro aprendizaje."),

                    ("czech",
                     "Python je skvělý programovací jazyk. " +
                     "Zbožňujeme Python, naši školu a učení.")]

    for expect, content in lang_samples:
        with open('zt.language.txt', "w") as file:
            file.write(content)
        lang = recognize_language(lang_freq, 'zt.language.txt')
        assert lang == expect, (lang, expect)


if __name__ == "__main__":
    main()
