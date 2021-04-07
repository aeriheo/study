import heapq
import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(lst)
    if l>p:
        arr.append(1)
    else:
        for _ in range(p-l):
            heapq.heappop(lst)
        arr.append(heapq.heappop(lst))

result = 0
arr.sort()

for data in arr:
    if data<=m:
        m -= data
        result +=1
    else:
        break
print(result)