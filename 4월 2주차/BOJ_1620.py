import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for i in range(1, n+1):
    data = sys.stdin.readline().rstrip()
    dic[str(i)] = data
    dic[data] = i

for _ in range(m):
    print(dic[sys.stdin.readline().rstrip()])