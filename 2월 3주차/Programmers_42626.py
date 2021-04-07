import heapq
def solution(scoville, K):
    answer = 0
    # heap정렬 만들기
    heapq.heapify(scoville)
    while 1:
        if len(scoville)<2 and scoville[-1]<K:
            answer = -1
            break
        if scoville[0] >=K:
            break
        # 가장 작은 수
        one = heapq.heappop(scoville)
        # 두번째
        two = heapq.heappop(scoville)
        three = one + (two*2)
        # 섞은 음식 지수
        heapq.heappush(scoville,three)
        answer += 1

    return answer


scoville = [1, 2,3,9,10,12]
K = 7
print(solution(scoville, K))