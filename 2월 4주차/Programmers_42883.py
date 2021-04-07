def solution(number, k):
    answer = ''
    ori = list(number)
    cnt = 0
    idx = 0
    while cnt<k and idx<len(ori)-1:
        if ori[idx]<ori[idx+1]:
            del ori[idx]
            cnt += 1
            idx = 0
        else:
            idx += 1
    answer = ''.join(ori)
    return answer

print(solution("1231234", 3))