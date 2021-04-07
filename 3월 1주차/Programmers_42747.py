def solution(citations):
    answer = 0
    # 정렬
    citations.sort()
    for i in range(max(citations)):
        for idx in range(len(citations)):
            if citations[idx]>=i:
                cnt = len(citations[idx:])
                if answer<i and i<=cnt:
                    answer = i
    return answer


print(solution([3,0,6,1,5]))