import heapq

n, m, k = map(int, input().split())
arr = []
for _ in range(m):
    tmp = list(input().split())
    for i in range(0, n*2, 2):
        # 참가자 번호는 int로, 능력은 float으로 받기
        heapq.heappush(arr, [int(tmp[i]), float(tmp[i+1])])

arr.sort(key=lambda x:(x[1]))
# print(arr)
idx = []
num = 0
sum = 0
# k명 뽑기 전까지 loop
while num != k:
    d = arr.pop()
    if d[0] not in idx:
        idx.append(d[0])
        sum += d[1]
        num += 1

print("%0.1f" %sum)