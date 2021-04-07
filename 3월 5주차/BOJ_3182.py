def go(idx, tmp):
    if dic[idx] not in tmp:
        tmp.append(dic[idx])
        go(dic[idx], tmp)
    return tmp

n = int(input())
dic = {}
for i in range(1, n+1):
    dic[i] = int(input())

res = {}
for i in range(1, n+1):
    tmp = [i]
    tmp.append(dic[i])
    res[i] = go(dic[i], tmp)

result = []
for i in res.keys():
    result.append([i, len(res[i])])

result.sort(key=lambda x:(-x[1],x[0]))
print(result[0][0])