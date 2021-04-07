import sys
from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key = lambda x:x[0])
dq = deque()
result = 0
for data in arr:
    if len(dq)<1:
        dq.append(data)
        continue

    x = data[0]
    y = data[1]
    if dq[0][0]<=x<=dq[0][1]:
        if dq[0][1]<y:
            dq[0][1] = y
    else:
        temp = dq.popleft()
        result += (temp[1]-temp[0])
        dq.append(data)

if dq:
    temp = dq.popleft()
    result += (temp[1]-temp[0])

print(result)