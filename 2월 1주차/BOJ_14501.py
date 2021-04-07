day = int(input())
arr = []
for _ in range(day):
    arr.append(list(map(int, input().split())))

dp = [0]*day
for i in range(day-1, -1, -1):
    t = arr[i][0]
    p = arr[i][1]

    if t > day-i:
        if i != day-1:
            dp[i] = dp[i+1]
        continue

    if i == day-1:
        dp[i] = p
    elif i + t == day:
        dp[i] = max(p, dp[i+1])
    else:
        dp[i] = max(p+dp[i+t], dp[i+1])


print(dp[0])

