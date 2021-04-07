def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        # em은 접두어
        em = phone_book[i]
        for j in range(len(phone_book)):
            # 같은 index는 제외 접두어가 동일하면 False
            if i!=j and em==phone_book[j][:len(em)]:
                answer = False
                break
        # 한번더 체크
        if answer ==False:
            break

    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))