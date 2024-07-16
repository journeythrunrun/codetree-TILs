# 1~100
# move : k
# 더 이동 불가하면 종료

# 현재보다 작은 곳으로 이동 가능 -> 여러 개면 그 중 큰 거 
## -> 여러 개 : 행번호가 가장 작은 곳 -> 열번호 작은 곳

# 2) bfs -> sort
#   작은 것만 append.  행index,열index , 값
# target.sort(lambda key=(-a[2],a[0],a[1] ) )# 클래스때만 되는건아니겠지
# import sys
from collections import deque
# input=sys.stdin.readline

n, k=map(int,input().split())
amap=[ list(map(int,input().split())) for _ in range(n)    ]
r,c=map(int,input().split())

if n==1:
    print(r,c)

i,j=r-1,c-1
di=[0,0,1,-1]
dj=[1,-1,0,0]

for _ in range(k):
    target=[]
    # k번에서
    visited=[[0]*n for _ in range(n)]
    aque=deque([[i,j]]) #~
    visited[i][j]=1

    while(aque):
        v=aque.popleft()
        # i,j=v[0],v[1] # 아 수정하고 수정한다는 게 안했었네
        

    #     for x in range (4): # !
    #         ni,nj=v[0]+di[x],v[1]+dj[x]
    #         if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0 and amap[ni][nj]<amap[i][j]: # 조건이 틀림
    #             aque.append([ni,nj])
    #             visited[ni][nj]=1
    #             target.append([ni,nj,amap[ni][nj]])# wow
    # target.sort(key=lambda x : (-x[2],x[0],x[1] ) )
    # # print(target)
    # ni,nj=target[0][0],target[0][1]
    # if i==ni and j ==nj :        # 이동할곳 없으면 탈출
    #     break
    # else :
    #     i,j=ni,nj
    # print(i+1,j+1)
    
# +1 출력
print(i+1,j+1)


# 엄밀히봐보기
# 일반input()의 줄엔터는
# 시간복잡도 암기

# 런타이멩러 엣지케이스