import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
S = list(map(int, sys.stdin.readline().split()))
s_len = len(S)
result = []
for i in range(1, s_len+1):
    for d in combinations(S, i):
        result.append(sum(d))
answer = 1
idx = 0
result = set(result)
result = list(result)
result.sort()

while idx<len(result) and answer == result[idx] :
    answer += 1
    idx += 1

print(answer)