def dfs(idx, cnt):


t = int(input())
for _ in range(t):
    dic ={}
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        if a not in dic.keys():
            dic[a] = [b]
        else:
            dic[a].append(b)
        if b not in dic.keys():
            dic[b] = [a]
        else:
            dic[b].append(a)
    visited = [0] * n
