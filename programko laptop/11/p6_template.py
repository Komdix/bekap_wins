from ib111 import week_11  # noqa


# Napište čistou funkci, která na základě daného vzoru vytvoří
# množinu všech odpovídajících řetězců. Vzor je tvořený
# alfanumerickými znaky a navíc může obsahovat hranaté závorky –
# znaky ‹[› a ‹]›. Mezi těmito závorkami může stát libovolný počet
# přípustných znaků (krom samotných hranatých závorek) a na daném
# místě se ve výsledném řetězci může nacházet libovolný z těchto
# znaků. Například vzor ‹a[bc]d› reprezentuje řetězce ‹abd› a ‹acd›.

def generate_combos(part: str) -> set[str] | str:
    if not (len(part) > 1 and part[0] == "[" and part[-1] == "]"):
        return part

    chars = set()

    for i in range(1, len(part) - 1):
        chars.add(part[i])
    return chars


def manual_split(template: str) -> list[str]:
    parts = []
    huh = ""
    brackets = False

    for char in template:
        if char == "[":
            if huh:
                parts.append(huh)
            huh = "["
            brackets = True
        elif char == "]":
            huh += "]"
            parts.append(huh)
            huh = ""
            brackets = False
        else:
            huh += char
            if not brackets and huh != "[":
                parts.append(huh)
                huh = ""

    if huh:
        parts.append(huh)

    return parts


def combine(parts: list[str], index: int, pre: str, result: set[str]) -> None:
    if index == len(parts):
        result.add(pre)
        return
    for part in generate_combos(parts[index]):
        combine(parts, index + 1, pre + part, result)


def resolve_template(template: str) -> set[str]:
    parts = manual_split(template)
    result: set[str] = set()
    combine(parts, 0, '', result)
    return result


def main() -> None:
    assert resolve_template("[]") == set()
    assert resolve_template("a") == {"a"}
    assert resolve_template("[abc]") == {"a", "b", "c"}
    assert resolve_template("a[bc]d") == {"abd", "acd"}
    assert resolve_template("[Hh]ello, [Ww]orld") \
        == {"Hello, World", "Hello, world", "hello, World", "hello, world"}
    assert resolve_template("[ab]x[cd]y[ef]") \
        == {"axcye", "axcyf", "axdye", "axdyf",
            "bxcye", "bxcyf", "bxdye", "bxdyf"}
    assert resolve_template("[abc]abc[ef]") \
        == {"aabce", "aabcf", "babce", "babcf", "cabce", "cabcf"}
    assert resolve_template("[ab][a][b][c][d]") \
        == {"aabcd", "babcd"}


if __name__ == '__main__':
    main()
