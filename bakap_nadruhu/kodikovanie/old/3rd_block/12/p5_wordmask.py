from ib111 import week_12  # noqa


# Napište čistou funkci ‹wordmask›, která vypočte všechny možnosti
# zamaskování slova ‹word›. Slovo zamaskujete aplikováním masky
# ‹mask›, tj. na každý znak slova se aplikuje korespondující znak
# masky. Je-li maska kratší než slovo, aplikuje se cyklicky.
#
# Například pro slovo «abababa» a masku «XX?» je situace následovná
# (odpovídající písmena jsou pod sebou):
#
#     abababa
#     XX?XX?X
#
# Maska je složena ze 2 znaků, ‹X› a ‹?›:
#
#  1. obsahuje-li maska na dané pozici znak ‹X›, odpovídající znak
#     slova se nemění,
#  2. naopak, je-li na dané pozici znak ‹?›, odpovídající znak ve
#     slově se zamaskuje některým znakem ze seznamu ‹alternatives›.
#
# Funkce ‹wordmask› pak vrátí seznam všech slov (v libovolném
# pořadí), které mohou tímto postupem vzniknout.
#
# Například pro slovo ‹abababa›, masku ‹XX?› a seznam alternativ
# ‹['x', 'y']› bude výsledkem maskování některá permutace seznamu
# ‹['abxbaxa', 'abybaxa', 'abxbaya', 'abybaya']›.


def masking(index: int, current: str, word: str, mask: str,
            alternatives: list[str], results: set[str]) -> None:
    if index == len(word):
        results.add(current)
        return

    mask_char = mask[index % len(mask)]

    if mask_char == 'X':
        masking(index + 1, current + word[index],
                word, mask, alternatives, results)
    elif mask_char == '?':
        for alt in alternatives:
            masking(index + 1, current + alt,
                    word, mask, alternatives, results)


def wordmask(word: str, mask: str, alternatives: list[str]) -> list[str]:
    results: set[str] = set()
    masking(0, "", word, mask, alternatives, results)
    return list(results)


def main() -> None:
    assert test_wordmask('aaa', 'X?X', ['b', 'c'], ['aba', 'aca'])
    assert test_wordmask('aaaa', 'X?X?', ['b', 'c'],
                         ['abab', 'abac', 'acab', 'acac'])
    assert test_wordmask('abc', '?X', ['A'], ['AbA'])
    assert test_wordmask('aaaa', 'X?', ['b', 'c'],
                         ['abab', 'abac', 'acab', 'acac'])
    assert test_wordmask('aaa', '?', ['x'], ['xxx'])
    assert test_wordmask('aaa', '?', ['x', 'i'],
                         ['xxx', 'ixx', 'xix', 'iix',
                          'xxi', 'ixi', 'xii', 'iii'])
    assert test_wordmask('aaaaa', '?X', ['x', 'i'],
                         ['xaxax', 'iaxax', 'xaiax', 'iaiax',
                          'xaxai', 'iaxai', 'xaiai', 'iaiai'])
    assert test_wordmask('aaaa', '??X?', ['x', 'y', 'z'],
                         ['xxax', 'yxax', 'zxax', 'xyax',
                          'yyax', 'zyax', 'xzax', 'yzax',
                          'zzax', 'xxay', 'yxay', 'zxay',
                          'xyay', 'yyay', 'zyay', 'xzay',
                          'yzay', 'zzay', 'xxaz', 'yxaz',
                          'zxaz', 'xyaz', 'yyaz', 'zyaz',
                          'xzaz', 'yzaz', 'zzaz'])


def test_wordmask(w: str, m: str, alt: list[str], exp: list[str]) -> bool:
    result = wordmask(w, m, alt)
    return len(result) == len(exp) and set(result) == set(exp)


if __name__ == '__main__':
    main()
