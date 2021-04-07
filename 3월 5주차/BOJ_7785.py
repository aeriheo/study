import sys
n = int(sys.stdin.readline().rstrip())
dic = {}
for _ in range(n):
    ipt = list(sys.stdin.readline().split())
    if ipt[1]=="enter":
        dic[ipt[0]] = 1
    elif ipt[1]=="leave":
        dic[ipt[0]] = 0

arr = []
for i in dic.keys():
    if dic[i]==1:
        arr.append(i)

arr.sort(reverse=True)
for data in arr:
    print(data)