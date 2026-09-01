def binary(n):
    if n == 0:
        return
    binary(n // 2)
    print(n % 2, end="")


T = int(input())

for _ in range(T):
    n = int(input())
    binary(n)
    print()
