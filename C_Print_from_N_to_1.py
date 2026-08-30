n = int(input())
def countDown(n):
    if n == 0:
        return
    if n == 1:
        print(n)
    else:
        print(n, end=" ")
    countDown(n-1)
countDown(n)
