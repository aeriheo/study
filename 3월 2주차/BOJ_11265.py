import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[j][k] > arr[j][i]+arr[i][k]:
                arr[j][k] = arr[j][i]+arr[i][k]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if arr[a-1][b-1]<=c:
        print("Enjoy other party")
    else:
        print("Stay here")