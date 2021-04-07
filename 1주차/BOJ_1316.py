n = int(input())
result = 0
for i in range(n):
    s = input()
    arr=[]
    p = ''
    isTrue = False
    for j in range(len(s)):
        if s[j] not in arr:
            arr.append(s[j])
            p = s[j]
        elif p != s[j] and s[j] in arr:
            isTrue = True

    if isTrue == False:
        result+= 1

print(result)
