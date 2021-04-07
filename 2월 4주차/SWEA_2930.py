import heapq

T = int(input())
for test_case in range(1, T+1):
    hq = []
    result = []
    n = int(input())
    for _ in range(n):
        num = list(map(int, input().split()))
        if num[0] == 1:
            # -num[1]은 우선순위 (값이 클수록 먼저)
            heapq.heappush(hq, (-num[1],num[1]))
        elif hq:
            m = heapq.heappop(hq)
            result.append(m[1])
        else:
            result.append(-1)
    print("#"+str(test_case), end = ' ')
    for v in result:
        print(v, end = ' ')
    print()