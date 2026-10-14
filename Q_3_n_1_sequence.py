def sequence(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + sequence(n // 2)
    else:
        return 1 + sequence(3 * n + 1)

n = int(input())
print(sequence(n))