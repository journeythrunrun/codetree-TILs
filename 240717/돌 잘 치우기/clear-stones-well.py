# 다른 컴 코드실행은 했던 거 여기엔 안나타나네->제출 클릭
# 0 이동가능
# 시작점의 수 k
# m개 뽑 ->최대수


import sys
inpu=sys.stdin.readline
# 1,2 2,0
n,k,m=map(int, inpu().split())
amap=[list(map(int, inpu().split())) for _ in range(n)]
starts=[list(map(int, inpu().split())) for _ in range(k)]
# -1 주의

ones=[]
for i in range(len(amap)):
    for j in range(len(amap[0])):
        if amap[i][j]==1: 
            ones.append([i,j])
from itertools import combinations

# 저장 rc -1

# combinations.p
# *
# print(list(combinations(ones,m)))#[([1, 2],), ([2, 0],)]

di=[0,0,1,-1]
dj=[1,-1,0,0]
from collections import deque
def bfs(v):
    # print(v)
    if visited[v[0]][v[1]]==True:
        return 0
    cnt=0 ## 디버깅 이미 방문한놈 
    visited[v[0]][v[1]]=True
    aque=deque([v])

    while(aque):
        v=aque.popleft()
        cnt+=1
        # print(v,cnt)
        for i in range(4):# 인접
            ni,nj=v[0]+di[i],v[1]+dj[i]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==False and maps[ni][nj]==0:## 변수 바꿨으면amap maps 코드 전체 훑..다른 amap위치..
                aque.append([ni,nj])
                visited[ni][nj]=True


    return cnt
result=0
# 읽는 디버깅중 : amap의 원상복귀
from copy import deepcopy
for aset in combinations(ones,m): # 튜플순선 # 치우기
    # 다른경우의수
    maps=deepcopy(amap)# =하면 아마 주소참조였나
    visited=[[False]*n for _ in range(n)]
    target=0
    # print(aset[0])# m개 뽑
    for i in range(len(aset)):
        maps[aset[i][0]][aset[i][1]]=0
    # print(maps)
    #bfs
    
    for i in range(k):
        target+=bfs([starts[i][0]-1,starts[i][1]-1]) # 아놔 복붙해서 쓸때 안에 값 자세히 체크. 변경
    result=max(result,target)
print(result)
# 어제꺼 복습


# - 기타 
# 저녁 코딩 때 데스크톱에서하면 소리 스스로 신경쓰이니까 나와서 해야징