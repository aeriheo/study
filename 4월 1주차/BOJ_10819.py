import itertools
def fun_sum(data):
    num = 0
    for i in range(len(data)-1):
        num += abs(data[i]-data[i+1])
    return num

n = int(input())
arr = list(map(int, input().split()))
p = list(itertools.permutations(arr, len(arr)))
result = 0
for i in p:
    temp = fun_sum(i)
    if temp>result:
        result = temp

print(result)