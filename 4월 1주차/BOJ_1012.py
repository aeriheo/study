from collections import deque
import sys

sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    arr[x][y] = 0
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<m and arr[xx][yy]==1:
            bfs(xx,yy)

t = int(input())
for _ in range(t):
    result = 0
    m, n, k = map(int, input().split())
    arr = [ [0 for _ in range(m)] for _ in range(n)]

    dq = deque()
    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1
        dq.append((x, y))

    while dq:
        d = dq.popleft()
        x = d[0]
        y = d[1]
        if arr[x][y] == 1:
            bfs(x, y)
            result += 1

    print(result)