import sys
from collections import deque

def bfs(node):
    if visited[node] == 0:
        print(node, end = ' ')
        visited[node] = 1

    if node in dic.keys():
        dic[node].sort()
        for v in dic[node]:
            if visited[v] == 0:
                print(v, end = ' ')
                visited[v] = 1
                will_visit.append(v)

def dfs(node):
    if visited[node] == 0:
        print(node, end = ' ')
        visited[node]=1

    if node in dic.keys():
        dic[node].sort()

        for v in dic[node]:
            if visited[v] == 0:
                print(v, end = ' ')
                visited[v] = 1
                dfs(v)

n, m, v = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a not in dic:
        dic[a] = []
        dic[a].append(b)
    else:
        dic[a].append(b)

    if b not in dic:
        dic[b] = []
        dic[b].append(a)
    else:
        dic[b].append(a)

will_visit = deque()
visited = [0] * (n+1)
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)
while will_visit:
    go_node = will_visit.popleft()
    if go_node in dic.keys():
        bfs(go_node)