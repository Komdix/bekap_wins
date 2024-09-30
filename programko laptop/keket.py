
# # # x = [1]
# # # y = x
# # # x[0] += 1
# # # print(x, y)


# # # def f(s):
# # #     s.append(1)
# # #     s = [2]
# # #     s.append(3)
# # #     print(s, end=" ")

# # # t = [0]
# # # f(t)
# # # print(t)

# # def f(s):
# #     s = s + [1]
# #     print(s)

# # t = [0]
# # f(t)
# # print(t)



# # keket = [2,1,5,7,62,45,42] + [21]
# # keket = [2,1,5,7,62,45,42,21]

# # def keket(a,b):

# #     x,y = a,b
# #     while x>0:
# #         x//2
# #         y//2
    
# #     return y
# # b>a>=0 y>0
# # a<b<0 y<0
# # a<=0 nikdy neskonci == BS 
# # a>b>=0 y==0


# # def fool(s):
# #     y = 0
# #     while s > 0:
# #         s -= 2
# #         y += 1
# #     return y
# # print(fool(10000000))

# def mystery(num: int, result: list[int]) -> list[int]:
#     if num <= 0:
#         return result
#     result.append(num)
#     one = mystery(num - 1, result)
#     two = mystery(num - 2, result)
#     return result
# print(mystery(4,[])
# )





# def fun(a: int, b: int) -> int:
#     x, y = a, b
#     while x > 0:
#         x //= 2
#         y //= 2
#     return y
# Která tvrzení o vztahu mezi vstupy a výstupy této funkce jsou pravdivá?
# (Právě dvě správné odpovědi.)
# Pokud  -  b > a >= 0, pak fun(a, b) > 0.
# Pokud  -  b < a <= 0, pak fun(a, b) < 0.
# Pokud  -  a >= b >= 0, pak fun(a, b) == 0.
# Pokud  -  b < a <= 0, pak fun(a, b) nikdy neskončí.
# Pokud  -  b > a >= 0, pak fun(a, b) == 0.
# Pokud  -  a >= b >= 0, pak fun(a, b) < 0.


def fun(a: int, b: int) -> int:
    x, y = a, b
    while x > 0:
        x //= 2
        y //= 2
    return y

a = -2
b = 2
print(fun(a,b))