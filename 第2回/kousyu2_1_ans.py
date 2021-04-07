from time import perf_counter

def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

N = 30
t0 = perf_counter()

while True:
    print(f"Fibonacci({N}) = {Fibonacci(N)}  {perf_counter() - t0}s")
    N += 1
