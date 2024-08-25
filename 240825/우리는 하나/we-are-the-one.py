# 1,2)
#  k개의 도시 고름 -> 갈수 있는 서로 다른 도시의 수_max
# -> 사방_ 높이 차가 u이상 d이하

# 2) bfs
# 시복_k개의 도시 선정 (collection) = n*n C k |  -> n*n=최대 64 
# --> nC

# 2) X_m2. amap훑으며 ud 만족하는 개수(bfs로?) 하기엔(min(numbs, k)) 쭉 갈 수 있는거라 다름? 선정된 k에 따라 다름 -> 

import sys
inpu=sys.stdin.readline
n,k,u,d = map(int,inpu().split() )
amap= [ list(map(int,inpu().split() )) for _ in range(n)]

# - combi
from itertools import combinations 

dx,dy=[0,0,1,-1], [1,-1,0,0]
amax=0

# -   print  (  list   (combinations( range(n*n) ,k)) ) 
# - [(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,)]
#   > 잘못기억하고 있나 했는데 걍 k가 1이었네 ㅋㅎ 


from collections import deque
for selected in combinations(range(n*n),k):
    # - 각 세트의 경우를 거쳐서 max값 찾을 때 -> visited, count : 각 새로운 세트 마다 초기화
    cnt=0
    visited=[ [False]*n for _ in range(n) ]

    q=deque(selected) # - (0,) -> deque([0])  튜플은 원래 1개만 있는게 저런 형식으로 있는 거일 뿐임. #형식 특이한 부분 없음  
    # - selected=(1,2,3) -> deque([1,2,3]) -> pop 
    # - deque : 한 껍질 벗기고 deque버전 리스트껍질화

    #for a in selected : # 2,4,5
    while(q):
        a= q.popleft()
        i,j=a//n, a%n
        # - queue에 처음부터 들어있는 값이 여러개인 상황 -> popleft한 것이 방문한 곳이면 continue #<-그 두 번째 이후 꺼가, 첫 번째 꺼로 부터 유발된 장소에 또 가지 않기 위함
        if visited[i][j]==True:
            continue

        cnt+=1
        visited[i][j]=True

        for k in range(4):
            ni, nj=i+dx[k], j+dy[k]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==False and u<=abs(amap[i][j]-amap[ni][nj])<=d:
                # - cnt+=1
                # - bfs로 바꿨을 땐, while(큐)라, 큐입력때든 큐출력때든 한 곳에서만 cnt해야함[cnt 두번됨] # 문제가 '연속으로' 이동 가능했던 거였어서, for->bfs_pop으로 바꿈 => ! 바꿀 때, 해당 부분 전체 코드 라인 살펴보면서, 변경으로 인한 알고리즘 세부 논리 재확인 검증했어야함 #이 부분 주석처리로 바꿨어야함.
                visited[i][j]=True
                q.append(ni*n+nj) # - ! i j 아니고 ni nj

    amax=max(amax,cnt)
print(amax)

# 4) u,d 0 | n 1 | k 1



# - 멍때림
# - 1h 3m  (itertools 사용 관련 암기를 까먹어서 본 시간 빼짐)
#   + 28m 틀림 : [문제이해] 상하좌우 인접한 도시간의 이동만 가능 -> 이어서 '계속' 못 간다는 말은 없으니 '가능'
#   + ! u이상 d이하 거꾸로
 

# - O(NCr) 관련 시간복잡도 및 허가 케이스 _ n최대 8
#   > ((maybeN=n으로 쓰셨던듯. 나는 N을 총 개수로 사용))

#   + M2_DP 로 시간복잡도*k부분 간소화 가능한 케이스의 문제였음.[뽑은 거에서 이어서 바로 연산들어가면 되기 때문임]
#     > O(C(N,k)*N) 

#     >> k는 max라고 해도 'N'에 비하면 네제곱근 수준일 뿐임. 그래도 시간복잡도면 작은 값이어도 변수니까 지우진 않고 기왕이면 기재했을 것임.

#     + -> 나 이제 n^2처럼 소문자 n으로 적어야겠다  (단순제곱근인지 헷갈 대비)

#   + M1_itertools  :  O(  r*  C(N,k)*N)