n = int(input())

def pyramid(row):
    if row > n:
        return

    print(" " * (n - row) + "*" * (2 * row - 1))

    pyramid(row + 1)

pyramid(1)
