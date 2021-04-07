arr = []
sort_arr = []
sum = 0
for _ in range(8):
    num = int(input())
    arr.append(num)
    sort_arr.append(num)

idx = []
sort_arr.sort(reverse=True)
for i in range(5):
    sum += sort_arr[i]
    idx.append(arr.index(sort_arr[i])+1)

print(sum)
idx.sort()
for i in idx:
    print(i, end=' ')