import sys
def func(arr):
    result = 0
    end = 0
    for data in arr:
        if data[0] >= end:
            result += 1
            end = data[1]
    print(result)

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1], x[0]))
func(arr)