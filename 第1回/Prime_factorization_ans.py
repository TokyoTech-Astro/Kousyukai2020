from math import sqrt
n = int(input("n = "))
prime_factor = []

sqrt_n = sqrt(n) + 1
t=2
while t<= n:
    if n % t:
        t += 1
        if sqrt_n < t:
            prime_factor.append(n)
            break
    else:
        n //= t
        prime_factor.append(t)


print("  = ", end = "")
print(*prime_factor, sep=" x ")