
n, W = map(int, input().split())

weights = []
values = []

for i in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

def solve(i, capacity):
    if i == n:
        return 0

    skip = solve(i + 1, capacity)

    if weights[i] <= capacity:
        take = values[i] + solve(i + 1, capacity - weights[i])
        return max(take, skip)

    return skip

print(solve(0, W))
