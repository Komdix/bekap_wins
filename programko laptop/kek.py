# def mystery(num, result):
#     if num <= 0:
#         return result
#     one = mystery(num - 1, result)
#     two = mystery(num - 2, result)
#     result.append(num)
#     return one
# print(mystery(4, []))
import random
lst = [
"if CONDITION: ",
"elif CONDITION: ",
"else: ",
"for VARIABLE in SEQUENCE: ",
"while CONDITION: ",
"try: ",
"except EXCEPTION as e: ",
"class MYCLASS: ",
"def MYFUNCTION(): ",
"return SOMETHING ",
"raise SOMETHING ",
"with SOMETHING: ",
"2 + 2 ",
"3 * 7" ,
"1 + 2 + 3 * (8 ** 9) - sqrt(4.0)" ,
"min(2, 22)" ,
"max(3, 94)" ,
"round(81.5) ",
"'foo'" ,
"'bar' ",
"'foo' + 'bar" ,
"None" ,
"True" ,
"False" ,
"2" ,
"3" ,
"4.0",
"students.get(uco)" - vyraz,
"assert len(data) > 0", prikaz
"data[0].append(3)", vyraz
"return students[uco]", prikaz
"students[uco] = '' ", prikaz???  -  si amore
"data[0] = [3]" , prikaz

"return a + b == 7", prikaz
"sorted(row)", vyraz
"num *= -1", prikaz
"7 if x > 10 else 11", vyraz
"s == [1, 2, 3]", vyraz
"data.pop(0)", vyraz

"None", vyraz
"3.14", vyraz
"sorted(data)", vyraz
"a += b", prikaz
"data.sort()", vyraz
"return True" prikaz
]
# print(len(lst))
for i in range(10):
    print(lst[random.randint(27, (len(lst)-1))])

# def fun(a: int, b: int) -> int:
#     x, y = a, b
#     while x > 0:
#         x //= 2
#         y //= 2
#     return y
# a = 0
# b = 4
# print(fun(a, b))

# print(data.sort())