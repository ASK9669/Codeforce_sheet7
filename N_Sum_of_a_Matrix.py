R,C = map(int, input().split())
matrix1 = []
matrix2 = []
for i in range(R):
    row = list(map(int, input().split()))
    matrix1.append(row)
for i in range(R):
    row = list(map(int, input().split()))
    matrix2.append(row)
for i in range(R):
    for j in range(C):
        print(matrix1[i][j] + matrix2[i][j], end=' ')
    print()