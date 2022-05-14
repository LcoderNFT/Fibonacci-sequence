def fib(a, b, lim):
    j = []
    j.append(a)
    j.append(b)
    for i in range(lim - 2):
        j.append(j[-1] + j[-2])
    return j

d = fib(0, 1, 10)
print(d)
