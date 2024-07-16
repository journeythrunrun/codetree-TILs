# 1~100
# move : k
# 더 이동 불가하면 종료

# 현재보다 작은 곳으로 이동 가능 -> 여러 개면 그 중 큰 거 
## -> 여러 개 : 행번호가 가장 작은 곳 -> 열번호 작은 곳

# 2) bfs -> sort
#   작은 것만 append.  행index,열index , 값
# target.sort(key=lambda x : (-x[2],x[0],x[1] ) ) 
import sys
from collections import deque
input=sys.stdin.readline

n, k=map(int,input().split())
amap=[ list(map(int,input().split())) for _ in range(n)    ]
r,c=map(int,input().split())

if n==1:
    print(r,c)
    exit()# + (4) 엣지케이스_exit()!!!!!!!!! 

i,j=r-1,c-1
di=[0,0,1,-1]
dj=[1,-1,0,0]

for _ in range(k):
    target=[]
    visited=[[0]*n for _ in range(n)]
    aque=deque([[i,j]]) 
    visited[i][j]=1

    while(aque):
        v=aque.popleft()
        # i,j=v[0],v[1] # + 한 이유로 수정생각하고 빼먹은 경우 -> 여러 곳에 수정시작 전에, #@표시
        

        for x in range (4): 
            ni,nj=v[0]+di[x],v[1]+dj[x]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0 and amap[ni][nj]<amap[i][j]: # 큐에서 pop된 거 말고, 더 본질적인 위치여야함.
                aque.append([ni,nj])
                visited[ni][nj]=1
                target.append([ni,nj,amap[ni][nj]]) # + 이건 또 왜 안에 비워뒀었지. 코드 수정 때, 복붙 후에도 쭉 내려 훑기. 
    # print(i,j)
    if len(target)==0: # 작은 값 append된게 없다면. # ==이동할곳 없으면 탈출 ## 이전이랑 같아서 값 업데이트 안해도됨
        break
    else :
        target.sort(key=lambda x : (-x[2],x[0],x[1] ) ) 
        i,j=target[0][0],target[0][1] # - 코드 통째로 변형할때 엄밀히 한줄한줄 보며 변경
    # ni,nj=target[0][0],target[0][1]
    # if i==ni and j ==nj :        
    #     break
    # else :
    #     i,j=ni,nj
    
# +1 출력
print(i+1,j+1)


# - 엄밀히봐보기
# - 시간복잡도 암기
#   + 500, 만, 백만 (보통 대략 1초 기준)
# - 1h 15m (결국 틀린 테스트케이스봄 : exit())