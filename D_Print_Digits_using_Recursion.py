def print_digits(n):
    if n < 0:
        print("-", end="")
        n = -n
    if n // 10:
        print_digits(n // 10)
    print(n % 10, end=" ")
T = int(input())
for i in range(T):
    num = int(input())
    print_digits(num)
    print()  
