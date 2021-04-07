
def main(n):
    listA = [0] * (n + 1)
    return Fibonacci(n,listA)

def Fibonacci(n,listA):
    if n <= 2:
        return 1
    if listA[n] > 0:
        return listA[n]
    
    fn = Fibonacci(n-1, listA) + Fibonacci(n-2, listA)
    listA[n] = fn
    return fn

if __name__ == "__main__":
    print(main(500))