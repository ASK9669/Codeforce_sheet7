N = int(input())
arr = list(map(int, input().split()))
average = sum(arr) / N
print(f"{average:.6f}")