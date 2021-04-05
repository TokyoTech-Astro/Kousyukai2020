# エラトステネスのふるいを用いていない解
prime_list = []
n = 2

while len(prime_list) < 50:
    for i in prime_list:
        if n % i == 0:
            break
    else:
        prime_list.append(n)
    n+=1

print(prime_list)