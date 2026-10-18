
n, k = map(int, input().split())
a = list(map(int, input().split()))

def solve(index, total):
    if index == n:
        return total == k

    add = solve(index + 1, total + a[index])
    subtract = solve(index + 1, total - a[index])

    return add or subtract

if solve(1, a[0]):
    print("YES")
else:
    print("NO")
