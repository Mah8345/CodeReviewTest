def fib(n):
    fibo_nums = [1 for x in range(n)]

    for i in range(n - 2):
        fibo_nums[i+2] = fibo_nums[i] + fibo_nums[i+1]
    return fibo_nums[n-1]


n = 5
print(fib(n))
