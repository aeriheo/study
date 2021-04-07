from collections import deque

def solution(priorities, location):
    # answer = 0
    # index 번호
    priorities = deque(priorities)
    arr = deque()
    for i in range(len(priorities)):
        arr.append(i)

    # 출력되는 순서를 보여줄 배열
    orderList = []
    # 가장 앞에 있는 문서를 대기목록에서 꺼냄 > J보다 중요도 높은 게 있는 경우 J를 맨뒤에 넣고 아니면 인쇄
    # 대기 목록이 끝날때까지 반복
    while priorities:
        j = arr.popleft()
        j_p = priorities.popleft()
        # is_in이 False면 대기목록에 중요도 높은게 없음
        is_in = False
        for i in priorities:
            if j_p<i:
                # 중요도가 높으면 뒤로 보내고 True로 바꿔주기
                priorities.append(j_p)
                arr.append(j)
                is_in = True
                break
        # False면 orderList에 넣기
        if is_in == False:
            orderList.append(j)

    # print(orderList)
    answer = orderList.index(location)+1
    return answer

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))