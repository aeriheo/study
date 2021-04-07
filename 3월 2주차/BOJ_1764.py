import sys
n,m = map(int, sys.stdin.readline().split())
# 듣지도 보지도 못한애
noPerson = []
# 듣보잡
result = []
for _ in range(n+m):
    noPerson.append(sys.stdin.readline().rstrip())

noPerson.sort()
idx = 0
while idx+2<=len(noPerson):
    if noPerson[idx]==noPerson[idx+1]:
        result.append(noPerson[idx])
        idx+=2
    else:
        idx+=1

result.sort()
print(len(result))
for data in result:
    print(data)