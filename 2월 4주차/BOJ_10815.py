import sys
def find_card(start, end, data):
    if start>=end or end<=start:
        print(0, end = ' ')
        return

    mid = (start+end)//2

    if sang[mid] == data:
        print(1, end = ' ')
        return

    else:
        if sang[mid]<data:
            start = mid+1
            find_card(start, end, data)
        else:
            end = mid
            find_card(start, end, data)

n = int(sys.stdin.readline())
# 상근이 카드
sang = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
# 숫자카드
card = list(map(int, sys.stdin.readline().split()))

# 상근이 카드 sort
sang.sort()
for i in card:
    find_card(0, n, i)