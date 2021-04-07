def solution(brown, yellow):
    answer = []
    s = brown + yellow
    # i는 가로 최소 3부터 시작
    for i in range(3, s):
        if s%i==0:
            j = s//i
            # i가 j보다 같거나 커야함
            if (i-2)*(j-2) == yellow and i>=j:
                answer.append(i)
                answer.append(j)
                return answer

print(solution(8,1))