N ,M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
sum_grid = []
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            sum_grid.append([grid[i][j]])
        elif i == 0:
            sum_grid[i].append(sum_grid[i][j-1] + grid[i][j])
        elif j == 0:
            sum_grid.append([sum_grid[i-1][j] + grid[i][j]])
        else:
            sum_grid[i].append(max(sum_grid[i-1][j], sum_grid[i][j-1]) + grid[i][j])
print(sum_grid[N-1][M-1])   