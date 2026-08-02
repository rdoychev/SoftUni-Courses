def fib(n: int) -> int:
    a = 5 ** 0.5
    return int((((1 + a) / 2) ** n - ((1 - a) / 2) ** n) / a)


n1 = 11
print(fib(n1))