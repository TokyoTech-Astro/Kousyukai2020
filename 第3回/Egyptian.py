from fraction import frac

x = frac(*map(int,input().split("/"))) # "3/5"のように入力された分数を読み取る
denominators = []       # 分母をこのリストに入れる

# TODO

print("= 1/", end = "")
print(*denominators, sep = " + 1/")