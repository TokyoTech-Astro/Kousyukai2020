from fraction import frac

x = frac(*map(int,input().split("/"))) # "3/5"のように入力された分数を読み取る
denominators = []                      # 分母をこのリストに入れる

while x.bunsi != 1:
    t = x.bunbo//x.bunsi + 1
    denominators.append(t)
    x = x - frac(1, t)
denominators.append(x.bunbo)

print("= 1/", end = "")
print(*denominators, sep = " + 1/")