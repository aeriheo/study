import sys
dp = [0] * 45
dp[0] = 0
dp[1] = 1

n = int(sys.stdin.readline().rstrip())
dic = {}
d_key = []
for _ in range(n):
    idx = int(sys.stdin.readline().rstrip())
    dic[idx] = []
    d_key.append(idx)

idx = 0
for i in range(2, len(dp)):
    dp[i] = dp[i-1]+dp[i-2]

for i in range(n):
    sum = d_key[i]
    for j in range(len(dp)-1, -1, -1):
        if dp[j]<=sum and dp[j] != 0:
            sum -= dp[j]
            dic[d_key[i]].append(dp[j])

        if sum==d_key[i]:
            continue

for k in dic.keys():
    dic[k].sort()
    for v in dic[k]:
        print(v, end = ' ')
    print()
