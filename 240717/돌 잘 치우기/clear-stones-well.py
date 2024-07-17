# 다른 컴 코드실행은 했던 거 여기엔 안나타나네->제출 클릭
# 저녁 코딩 때 데스크톱에서하면 소리 스스로 신경쓰이니까 나와서 해야징

# 0 이동가능
# 시작점의 수 k
# m개 뽑 ->최대수


import sys
inpu=sys.stdin.readline
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

# - itertools 복습
#   + product(*list) : 각 행에서 한 개씩 뽑음
# 1개여서 활용 때 좀 헷갈렸을뿐 저렇게 나오는 거 맞음 print(list(combinations(ones,m)))#[([1, 2],), ([2, 0],)]

di=[0,0,1,-1]
dj=[1,-1,0,0]
from collections import deque
def bfs(v):
    # print(v)
    if visited[v[0]][v[1]]==True: ## 디버깅 : 이미 방문한놈 (첫노드는 방문체크 없이 들어왔어서 pop될때 갔던 곳 이중으로 세지기도 함. 애초에 bfs 노드 들어올때 미방문체크가 나음 ) 
        return 0
    cnt=0 
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
from copy import deepcopy # +
for aset in combinations(ones,m): # + 튜플 인덱스 가능 # 치우기   # 다른 경우의 수
    maps=deepcopy(amap)# + =하면 아마 주소참조였나
    visited=[[False]*n for _ in range(n)]
    target=0
    # print(aset[0])
    for i in range(len(aset)):  # 각 경우의 수에 대해서 m개씩 뽑았으니까 당연히 또 for.
        maps[aset[i][0]][aset[i][1]]=0
    # print(maps)
    
    for i in range(k):
        target+=bfs([starts[i][0]-1,starts[i][1]-1]) # + 아놔 비슷 코드 복붙 때 안 값 글자단위 체크. 변경
    result=max(result,target)
print(result)

# - 52m+조심히문제읽및소심작성15m 
#   > 암기 못한거 봄
#   + 2)를 더해야할 듯 싶다. 나무의 위에서 시작돼서 내려오는데, 구현쓰다가 다시 위의 생각으로 돌아가려고 약간 두리번_중복 및 생각 전환 시간.

# - (4)까지 하기 : (엣지케이스_exit()!!!!!!!!!)