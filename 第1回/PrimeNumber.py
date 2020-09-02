prime_list = []
t=2
while len(prime_list)<50:
    for i in prime_list:
        if t%i==0:
            break
    else:
        prime_list.append(t)
    t+=1
print(prime_list)