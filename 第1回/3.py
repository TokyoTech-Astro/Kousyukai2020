import math

num = int(input())
original = num
num_list = list(range(2, math.ceil(num ** (1 / 2))))
num_list2 = []
pro = 1

while len(num_list) >= 1:
    if num % num_list[0] == 0:
        num_list2.append(num_list[0])
        num = num / num_list[0]
        pro = pro * num_list[0]
    else:
        i = num_list[0]
        # j = 1
        num_max = num_list[-1]
        for j in range(i, num_max + 1, i):
            if j in num_list:
                num_list.remove(j)
        # while i * j <= num_max:
        #    if i * j in num_list:
        #        num_list.remove(i * j)
        #    j += 1

if pro != original:
    num_list2.append(round(original / pro))
    

# print(num_list2)

num_dic = {}

for i in num_list2:
    if i not in num_dic:
        num_dic[i] = 1
    else:
        num_dic[i] += 1

# print(num_dic)

for i in num_dic:
    print("(" + str(i) + " ** " + str(num_dic[i]) + ")", end = "")
    if i == num_list2[-1]:
        break
    print(" * ", end = "")
    
