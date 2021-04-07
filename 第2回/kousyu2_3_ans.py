import kousyu2_2
import time

t0 = time.perf_counter()
listA = [0] * (500 + 1)

kousyu2_2.Fibonacci(500, listA)

print(time.perf_counter() - t0)