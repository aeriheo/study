import sys

dic = {}
n, p = map(int, sys.stdin.readline().split())

result = 0
for _ in range(n):
    l, pn = map(int, sys.stdin.readline().split())
    if l not in dic.keys():
        dic[l] = []
        dic[l].append(pn)
        result += 1

    elif dic[l][-1] > pn:
        while dic[l] and dic[l][-1]>pn:
            dic[l].pop()
            result+=1
        if dic[l] and dic[l][-1] == pn:
            continue
        dic[l].append(pn)
        result+=1

    elif dic[l][-1] == pn:
        pass

    else:
        dic[l].append(pn)
        result += 1

print(result)