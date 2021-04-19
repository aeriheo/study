def find_num(arr2):
    cnt1 = 0
    # arr[0][0]이 W일 때
    for i in range(8):
        if i%2==0:
            for j in range(0, 8, 2):
                if arr2[i][j]!='W':
                    cnt1 += 1

            for j in range(1, 8, 2):
                if arr2[i][j] != 'B':
                    cnt1 += 1
        else:
            for j in range(0, 8, 2):
                if arr2[i][j] != 'B':
                    cnt1 += 1

            for j in range(1, 8, 2):
                if arr2[i][j] != 'W':
                    cnt1 += 1

    cnt2 = 0
    # arr[0][0]이 B일 때
    for i in range(8):
        if i % 2 == 0:
            for j in range(0, 8, 2):
                if arr2[i][j] != 'B':
                    cnt2 += 1

            for j in range(1, 8, 2):
                if arr2[i][j] != 'W':
                    cnt2 += 1
        else:
            for j in range(0, 8, 2):
                if arr2[i][j] != 'W':
                    cnt2 += 1

            for j in range(1, 8, 2):
                if arr2[i][j] != 'B':
                    cnt2 += 1

    if cnt1>cnt2:
        return cnt2
    else:
        return cnt1

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(input()))

result = 65

for i in range(n-7):
    for j in range(m-7):
        temp = []
        for k in range(8):
            temp.append(arr[i+k][j:j+8])
        t = find_num(temp)
        if result>t: result = t

print(result)