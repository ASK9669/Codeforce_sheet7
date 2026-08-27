def print_recursion(n):
    if n == 0:
        return

    print("I love Recursion")
    print_recursion(n - 1)


N = int(input())
print_recursion(N)