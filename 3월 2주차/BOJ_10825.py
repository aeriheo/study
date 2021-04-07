import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().split()))

arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for name in arr:
    print(name[0])