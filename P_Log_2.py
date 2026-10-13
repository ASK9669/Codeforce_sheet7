import math
n = int(input())
if n == 1:
    print(0)
else:
    print(math.floor(math.log2(n)))