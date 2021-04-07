import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
hq = []
arr = list(map(int, sys.stdin.readline().split()))
for data in arr:
    heapq.heappush(hq, data)
# print(hq)

for cnt in range(m):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    heapq.heappush(hq, a+b)
    heapq.heappush(hq, a+b)

card_sum = sum(hq)
print(card_sum)
