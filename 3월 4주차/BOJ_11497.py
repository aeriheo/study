import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))

    lst = []
    arr.sort()
    # arr 중 가장 큰 값을 넣기
    lst.append(arr.pop())
    # idx true > 오른쪽에 false > 왼쪽에 넣기
    idx = True
    while arr:
        if idx == True:
            lst.append(arr.pop())
            idx = False
        else:
            lst.insert(0, arr.pop())
            idx = True

    result = 0
    idx = 0
    while idx<len(lst)-1:
        tmp = lst[idx]-lst[idx+1]
        if abs(tmp)>result:
            result = abs(tmp)

        idx += 1
    print(result)
