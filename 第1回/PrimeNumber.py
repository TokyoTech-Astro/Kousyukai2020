prime_num = []

t=2
while len(prime_num)<50:
    for i in prime_num:
        if t%i==0:
            break
    else:
        prime_num.append(t)
    t+=1

print(prime_num)