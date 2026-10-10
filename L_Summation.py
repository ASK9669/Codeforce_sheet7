N = int(input())

lst = list(map(int, input().split()))

def summation(lst, N):
    if N == 0:
        return 0

    return lst[N - 1] + summation(lst, N - 1)

print(summation(lst, N))