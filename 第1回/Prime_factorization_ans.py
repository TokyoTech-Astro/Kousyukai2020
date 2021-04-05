n = int(input("n = "))
prime_factor = []

t = 2

while t <= n:
    if n % t:
        t += 1
        if t**2 > n:  # 大きい素数が残ったときは√nで打ち切る
            prime_factor.append(n)
            break
    else:
        n //= t
        prime_factor.append(t)

print("  = ", end = "")
print(*prime_factor, sep=" x ")