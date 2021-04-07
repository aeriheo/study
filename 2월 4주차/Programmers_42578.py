# import copy
# from collections import deque
#
# def coll(dic, arr):
#     n = len(arr)
#     for _ in range(n):
#         p = arr.popleft()
#         for k in dic.keys():
#             if k not in p:
#                 tmp = copy.deepcopy(p)
#                 tmp.append(k)
#                 tmp.sort()
#                 if tmp not in arr:
#                     arr.append(tmp)
#
# def summ(arr, dic):
#     num = 0
#     for i in arr:
#         tt = 1
#         for j in i:
#             tt *= len(dic[j])
#         num += tt
#     return num
#
# def solution(clothes):
#     answer = 0
#     dic = {}
#     for i in clothes:
#         if i[1] not in dic:
#             dic[i[1]] = []
#             dic[i[1]].append(i[0])
#         else:
#             dic[i[1]].append(i[0])
#     arr = [[i] for i in dic.keys()]
#     arr = deque(arr)
#
#     for _ in range(1,len(dic.keys())):
#         answer += summ(arr, dic)
#         coll(dic,arr)
#
#     answer += summ(arr, dic)
#     return answer

def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] =1
        else:
            dic[i[1]]+=1

    for v in dic.values():
        answer *= (v+1)

    return answer-1

ans = solution([
["a", "a"],
["b", "b"],
["c", "c"]
])
print(ans)