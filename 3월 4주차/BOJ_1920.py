import sys
n = int(sys.stdin.readline().rstrip())
dic = {}
arr = list(map(int, sys.stdin.readline().split()))
for i in arr:
    if i not in dic:
        dic[i] = 0
m = int(sys.stdin.readline().rstrip())
del arr
arr = list(map(int, sys.stdin.readline().split()))
for i in arr:
    if i in dic:
        print(1)
    else:
        print(0)