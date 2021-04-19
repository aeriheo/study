import copy
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
now = '0'
def bfs_arr1(x, y):
    arr[x][y] = '0'
    for j in range(4):
        xx = x+dx[j]
        yy = y+dy[j]
        if 0<=xx<n and 0<=yy<n and arr[xx][yy]==now:
            bfs_arr1(xx,yy)

def bfs_arr2(x, y):
    arr2[x][y] = '0'
    for j in range(4):
        xx = x+dx[j]
        yy = y+dy[j]
        if 0<=xx<n and 0<=yy<n and arr2[xx][yy]==now:
            bfs_arr2(xx,yy)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))

arr2 = copy.deepcopy(arr)
dq2 = deque()
for i in range(n):
    for j in range(n):
        if arr2[i][j]=='G':
            arr2[i][j]='R'
        dq2.append([i, j])

cnt1 = 0
cnt2 = 0
dq = deque()
for i in range(n):
    for j in range(n):
        dq.append([i, j])

while dq:
    t = dq.popleft()
    x = t[0]
    y = t[1]
    if arr[x][y] =='0':
        continue
    now = copy.deepcopy(arr[x][y])
    bfs_arr1(x,y)
    cnt1 += 1

while dq2:
    t = dq2.popleft()
    x = t[0]
    y = t[1]
    if arr2[x][y] =='0':
        continue
    now = copy.deepcopy(arr2[x][y])
    bfs_arr2(x,y)
    cnt2 += 1

print(cnt1, cnt2)