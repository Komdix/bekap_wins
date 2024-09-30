from ib111 import week_11  # noqa


# Napište čistou funkci, která na základě daného vzoru vytvoří
# množinu všech odpovídajících řetězců. Vzor je tvořený
# alfanumerickými znaky a navíc může obsahovat hranaté závorky –
# znaky ‹[› a ‹]›. Mezi těmito závorkami může stát libovolný počet
# přípustných znaků (krom samotných hranatých závorek) a na daném
# místě se ve výsledném řetězci může nacházet libovolný z těchto
# znaků. Například vzor ‹a[bc]d› reprezentuje řetězce ‹abd› a ‹acd›.

def generate_combinations(part: str) -> set[str]:
    if len(part) > 1 and part[0] == '[' and part[-1] == ']':
        chars = set()
        for i in range(1, len(part) - 1):
            chars.add(part[i])
        return chars
    return {part}

def split_template(template: str) -> list[str]:
    parts = []
    temp = ''
    inside_brackets = False
    for char in template:
        if char == '[':
            if temp:
                parts.append(temp)
            temp = '['
            inside_brackets = True
        elif char == ']':
            temp += ']'
            parts.append(temp)
            temp = ''
            inside_brackets = False
        else:
            temp += char
            if not inside_brackets and temp != '[':
                parts.append(temp)
                temp = ''
    if temp:
        parts.append(temp)
    return parts

def combine(parts: list[str], index: int, prefix: str, result: set[str]):
    if index == len(parts):
        result.add(prefix)
        return
    for part in generate_combinations(parts[index]):
        combine(parts, index + 1, prefix + part, result)

def resolve_template(template: str) -> set[str]:
    parts = split_template(template)
    result = set()
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
