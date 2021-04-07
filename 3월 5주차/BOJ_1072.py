end = 1000000000
x, y = map(int, input().split())
z = (y*100)//x
start = 0
result = 0
while start<=end:
    if z>=99:
        result = -1
        break
    else:
        mid = (start+end)//2
        comp = ((mid+y)*100)//(mid+x)
        if comp>z:
            result = mid
            end = mid -1
        else:
            start = mid+1

print(result)