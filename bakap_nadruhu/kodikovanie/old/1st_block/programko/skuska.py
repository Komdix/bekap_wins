def sequence(n, k, initial):
    a = initial
    result = 0
    if n == 0:
        return initial
    elif k == 1:
        return - initial
    else:
        for i in range(1,k+1):
            
            
            result = (-1)** i * i *a
            
            a = result
        return result
s= sequence(2, 3, 2)
print(s)