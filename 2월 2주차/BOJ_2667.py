def dfs(i, j):
    arr[i][j] = '0'
    cnt = 0
    for idx in range(4):
        x = dx[idx]+i
        y = dy[idx]+j
        if 0<=x and x<n  and 0<=y and y<n:
            if arr[x][y] == '1':
                cnt += dfs(x, y)
    return cnt + 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(input()))
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            result.append(dfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)