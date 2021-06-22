import itertools

member = [i for i in range(1,9)]
perm = itertools.permutations(member, 8)
perm = list(perm)
# N 이닝수
N = int(input())
Inn = []
for _ in range(N):
    Inn.append(list(map(int, input().split())))

# 최대 점수
result = 0
for p in perm:
    # 이번 경우의 점수
    score = 0
    nextNum = 0
    p = list(p)
    p.insert(3, 0)
    for inning in range(N):
        outCnt = 0
        base1 = 0
        base2 = 0
        base3 = 0
        while outCnt<3:
            if Inn[inning][p[nextNum]] == 0:
                outCnt += 1
            elif Inn[inning][p[nextNum]] == 4:
                score += (base1+base2+base3+1)
                # 홈런이면 다음엔 아무도 없어야하니까 0으로 처리
                base1 = 0
                base2 = 0
                base3 = 0
            elif Inn[inning][p[nextNum]] == 1:
                # 3루에 누가 있으면 1점
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            elif Inn[inning][p[nextNum]] == 2:
                # 2, 3루에 누가 있으면 1점씩 추가
                score += (base2+base3)
                base3 = base1
                base2 = 1
                base1 = 0
            elif Inn[inning][p[nextNum]] == 3:
                # 1, 2, 3루에 누가 있으면 점수 추가
                score += (base1+base2+base3)
                base3 = 1
                base1 = 0
                base2 = 0
            nextNum += 1
            if nextNum == 9: nextNum = 0
    result=max(result, score)

print(result)