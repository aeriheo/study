T = int(input())
for _ in range(T):
    dic = {}
    d_keys = []
    n = int(input())
    for i in range(n):
        data = list(input().split())
        if data[1] in dic.keys():
            dic[data[1]] += 1
        else:
            dic[data[1]] = 1
            d_keys.append(data[1])

    result = 1

    for v in dic.values():
        result *= (v+1)

    print(result-1)