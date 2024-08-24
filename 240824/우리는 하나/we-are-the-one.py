# 1,2)
#  k개의 도시 고름 -> 갈수 있는 서로 다른 도시의 수_max
# -> 사방_ 높이 차가 u이상 d이하

# 2) bfs
# 시복_k개의 도시 선정 (collection) = n*n C k |  -> n*n=최대 64 
# --> nC

# 2) amap훑으며 ud 만족하는 개수(bfs로?) 하기엔(min(numbs, k)) 쭉 갈 수 있는거라 다름? 선정된 k에 따라 다름 -> 
import sys
inpu=sys.stdin.readline
n,k,u,d = map(int,inpu().split() )
amap= [ list(map(int,inpu().split() )) for _ in range(n)]
# import collections
from itertools import combinations #
#~

dx,dy=[0,0,1,-1], [1,-1,0,0]
amax=0
# print(list(range(n*n)) )
# print(list(combinations( range(n*n) ,k)) ) # 예전꺼라 잘못기억하고 있나 했는데 걍 k가 1이었네 ㅋㅎ [(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,)]

# - visited & count vc비자
# - > visited 초기화


# 큐 전체빠져나올듯
from collections import deque
for selected in combinations(range(n*n),k):
    # print('sele', selected) # for로 벗겨서 튜플
    cnt=0
    visited=[ [False]*n for _ in range(n) ]

    q=deque(selected) # deque([0]) 1개짜리도 이 화 #     # selected=(1,2,3)도
    #for a in selected : # 2,4,5
    # combi 시간복잡도
    while(q):
        # print('q',q)
        a= q.popleft() #~left _queue
        # print(a)
        i,j=a//n, a%n
        # 출발대상이 여러개이다보니, 이전에 방문했던  곳 방문하지 않도록
        if visited[i][j]==True:
            continue


        # print(i,j)    
        cnt+=1
        visited[i][j]=True
        # print('11111',i,j)
        # print('q',q)
        for k in range(4):
            ni, nj=i+dx[k], j+dy[k]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==False and u<=abs(amap[i][j]-amap[ni][nj])<=d:
                ## cnt+=1 # cnt 두번되네. bfs pop화하면서 주석처리로 바꿨어야
                visited[i][j]=True
                q.append(ni*n+nj)# i j 아니고 ni nj

                # print('22222',ni, nj)
        # print(visited)
    # print('cnt',cnt)
    amax=max(amax,cnt)
print(amax)

# u이상 d이하 거꾸로
# 4) u,d 0 | n 1 | k 1



# - 멍때림
# - 28m 틀렸습니다
#  + 상하좌우 인접한 도시간의 이동만 가능 -> 계속 갈수도..