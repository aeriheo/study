import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, cnt):
    visited[x][y] = 1
    cnt+=1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<m and arr[xx][yy] == '1' and visited[xx][yy] == 0:
                dq.append([xx, yy, cnt])
                visited[xx][yy] = 1


n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
visited = [[0]*m for _ in range(n)]
dq = deque()
dq.append([0,0,1])
# bfs(0, 0, 1)
result = 100001
while dq:
    x, y, cnt = dq.popleft()
    result = cnt
    if x==n-1 and y == m-1:
        break
    bfs(x, y, cnt)
    # print(dq)

print(result)