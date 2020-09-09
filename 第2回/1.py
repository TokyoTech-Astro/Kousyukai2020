import time

def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

i = 30

while True:
    start_time = time.perf_counter()
    Fibonacci(i)
    end_time = time.perf_counter()
    print(end_time - start_time)
    i += 1