import sys
dic = {1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1],
       4:[4, 6], 5:[5],
       6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6],
       9:[9, 1], 10:[10]}
n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    if a==0:
        a=10
    b %= len(dic[a])
    print(dic[a][b-1])
