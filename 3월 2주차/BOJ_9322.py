n = int(input())

for _ in range(n):
    m = int(input())
    arr1 = input().split()
    arr2 = input().split()
    arr3 = input().split()

    change = [0]*len(arr3)
    # print(change)

    for i in range(len(arr1)):
        idx = arr2.index(arr1[i])
        change[i] = idx

    for i in range(len(arr3)):
        print(arr3[change[i]], end = ' ')
    print()

