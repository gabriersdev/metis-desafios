def fib(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
