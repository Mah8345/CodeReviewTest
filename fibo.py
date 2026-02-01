def fib(n):
    a = []
    for i in range(n):
        a.append(1)

    for i in range(n - 2):
        a[i+2] = a[i] + a[i+1]
    return a[n-1]


n = 5
print(fib(n))
