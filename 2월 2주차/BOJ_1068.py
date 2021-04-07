def Delete_node(node):
    if dic[node]:
        nd = dic[node]
        for i in nd:
            Delete_node(i)
       # 자식들을 지운 후에 본인 삭제
        del dic[node]
    else:
        # 자식 node가 없으면 그냥 삭제
        del dic[node]


n = int(input())
dic = {}
lst = list(map(int, input().split()))

for i in range(n):
    # tree 번호는 i
    dic[i] = []

for i in range(n):
    # root는 -1이므로 패스
    if lst[i] == -1:
        pass
    else:
        # 해당 부모에 자식 번호 넣어두기
        dic[lst[i]].append(i)

# print(dic)
# 지울 노드번호
remove_node = int(input())
# 지우기
Delete_node(remove_node)

for k in dic.keys():
    # 만약 일직선일경우..
    if remove_node in dic[k]:
        dic[k].remove(remove_node)

# leaf node 개수
result = 0
if dic:
    for k, v in dic.items():
        if len(v)==0:
            result+=1
# print(dic)
print(result)