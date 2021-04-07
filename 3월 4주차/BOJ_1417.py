import heapq
n = int(input())
arr = []
for i in range(n):
    data = int(input())
    if i == 0:
        dasom = data
    else:
        heapq.heappush(arr, (-data, data))
result = 0
while arr and dasom<=arr[0][1]:
    tmp = heapq.heappop(arr)[1]
    tmp -= 1
    dasom += 1
    if tmp >0:
        heapq.heappush(arr, (-tmp, tmp))
    result +=1
print(result)