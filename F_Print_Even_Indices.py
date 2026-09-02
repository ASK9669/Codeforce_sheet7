n = int(input())
a = list(map(int, input().split()))

def print_even(i):
    if i >= n:
        return

    print_even(i + 2)

    print(a[i], end=" ")

print_even(0)
