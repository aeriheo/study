import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = [0] * n
for i in range(len(arr)):
    temp[i] = sum(arr[:i+1])
print(sum(temp))