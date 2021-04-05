# エラトステネスのふるいを用いた解

l = [0]*1000
prime_list = []
i = 1

while len(prime_list) < 50:
    i += 1
    if l[i]:
        continue
    prime_list.append(i)
    
    for j in range(i**2,1000,i): # i^2より大きいiの倍数を消せばよい
        l[j] = 1

print(prime_list)