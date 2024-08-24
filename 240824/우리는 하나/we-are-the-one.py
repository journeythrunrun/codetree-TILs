# 1,2)
#  k개의 도시 고름 -> 갈수 있는 서로 다른 도시의 수_max
# -> 사방_ 높이 차가 u이상 d이하

# 2) bfs
# 시복_k개의 도시 선정 (collection) = n*n C k |  -> n*n=최대 64 
# --> nC
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
for selected in combinations(range(n*n),k):
    cnt=0
    visited=[ [False]*n for _ in range(n) ]

    for a in selected :
        # print(a)
        i,j=a//n, a%n
        # print(i,j)    
        cnt+=1
        visited[i][j]=True


        for k in range(4):
            ni, nj=i+dx[k], j+dy[k]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==False and u<=abs(amap[i][j]-amap[ni][nj])<=d:
                cnt+=1
                visited[i][j]=True
        # print(visited)
    amax=max(amax,cnt)
print(amax)

# u이상 d이하 거꾸로
# 4) u,d 0 | n 1 | k 1


# - 멍때림