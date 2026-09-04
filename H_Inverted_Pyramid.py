n = int(input())

def pyramid(stars, spaces):
    if stars <= 0:
        return

    print(" " * spaces + "*" * stars)
    pyramid(stars - 2, spaces + 1)

pyramid(2 * n - 1, 0)
