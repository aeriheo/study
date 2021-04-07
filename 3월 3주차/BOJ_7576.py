from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, day):
    arr[x][y] = 1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        # 0일 경우만 deque에 넣기
        if 0<=xx<n and 0<=yy <m and arr[xx][yy]==0:
            dq.append([xx,yy,day+1])
            arr[xx][yy] = 1
            
# m 세로 n 가로
m, n = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dq = deque()
for x in range(n):
    for y in range(m):
        if arr[x][y] == 1:
            # 1일 경우 deque에 넣기 여기서 0은 해당 위치에서 몇일이 지낫는지
            dq.append([x, y, 0])

result = -1
# print(dq)
while dq:
    x, y, result = dq.popleft()
    bfs(x, y, result)

#마지막으로 0이 있는지 check
for x in range(n):
    if 0 in arr[x]:
        result = -1
        break

print(result)