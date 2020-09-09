num_list = list(range(2, 1000))
prime_list = []

try:
    for i in range(50):
        # print(num_list[0])
        prime_list.append(num_list[0])
        j = 1
        i = num_list[0]
        num_max = max(num_list)
        while i * j <= num_max:
            if i * j in num_list:
                num_list.remove(i * j)
            j += 1
        # print(num_list)
except Exception as e:
    print("a")

print(prime_list)
