import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

cnt = 0
now = k
idx = 0
for i in range(n):
    # k보다 작은 동전 index 찾기
    if coin[i] < k:
        idx = i
    else:
        break

# 0원되면 끗
while now != 0 or idx>=0:
    cnt += now//coin[idx]
    now = now%coin[idx]
    idx -= 1

print(cnt)