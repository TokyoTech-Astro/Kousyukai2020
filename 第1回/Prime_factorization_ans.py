n = int(input("n = "))
prime_factor = []

i = 2
while i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        prime_factor.append(i)

print("  = ", end = "")
print(*prime_factor, sep=" x ")