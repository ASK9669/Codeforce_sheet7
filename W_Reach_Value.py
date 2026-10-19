import sys

def can_reach(n):
    # Base Case 1: Target reached
    if n == 1:
        return True
    # Base Case 2: Overshot target
    if n < 1:
        return False
    
    # Check division paths
    if n % 20 == 0 and can_reach(n // 20):
        return True
    if n % 10 == 0 and can_reach(n // 10):
        return True
        
    return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        if can_reach(n):
            results.append("YES")
        else:
            results.append("NO")
            
    print("\n".join(results))

if __name__ == "__main__":
    solve()