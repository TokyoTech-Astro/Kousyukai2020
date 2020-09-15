def fibonacci(x):
    num_list = [0] * (x + 1)
    return calculate(x, num_list)

def calculate(x, num_list):
    if x >= 1 and num_list[x] == 0:
        if x == 1:
            num_list[x] = 1
        else:
            num_list[x] = calculate(x - 1, num_list) + calculate(x - 2, num_list)
    return num_list[x]

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))