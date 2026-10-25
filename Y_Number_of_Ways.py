S , E = map(int, input().split())
def ways(S):
    if S ==  E:
        return 1
    if S > E:
        return 0
    return ways(S + 1) + ways(S + 2) + ways(S + 3)
print(ways(S))