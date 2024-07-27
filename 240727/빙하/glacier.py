# 빙하1 
# 1초당 빙하 물에 닿아있는 부분 녹음 but 빙하로 둘러싸여있는 물은 빙하못녹임

# 빙하가 전부 녹는데 걸리는 시간, 마지막으로 녹은 빙하의 크기(1의 개수)
# 2) while(len(left)!=0) for n  
#    1이 미방문 0 만났을 때 : 인접0다가가기로 벽만날수있으면->자신인1의 0화 # 잘못썼넹
# 둘러쌓임 : 
 
import sys
inpu=sys.stdin.readline

n,m=map(int, inpu().split())
amap=[ list(map(int, inpu().split())) for _ in range(n)]

ones=[]
for i in range(n):
    for j in range(m):
        if amap[i][j]==1:
            ones.append([i,j])
visited=[[False]*m for _ in range(n)]
di=[0,0,-1,1]
dj=[1,-1,0,0]
from collections import deque

def bfs2(v):#인접0다가가기로 벽만날수있으면->1화  

    visited2=[[False]*m for _ in range(n)]
    visited2[v[0]][v[1]]=True
    aque2=deque([v]) #~ 이름v

    while(aque2):
        v2=aque2.popleft()
        # 출력
        
        for i in range(4):
            ni,nj=v2[0]+di[i],v2[1]+dj[i]#v2[0]+di[0],v2[1]+dj[1]
            if 0<=ni<n and 0<=nj<m and visited2[ni][nj]==False and amap[ni][nj]==0:
                aque2.append([ni,nj])  # aque2 # 2헷갈리니 아예이름이 다른게 낫
                visited2[ni][nj]=True #visited2
                
                if ni==0 or nj==0 or ni==n-1 or nj==m-1:
                    return True
    return False


def bfs(v):
    visited[v[0]][v[1]]=True
    aque=deque([v])

    while(aque):
        w=aque.popleft()
        # 출
        
        for i in range(4):
            ni,nj=w[0]+di[i],w[1]+dj[i] # i대신 0,1실화냐
            if 0<=ni<n and 0<=nj<m and visited[ni][nj]==False and amap[ni][nj]==0:
                if bfs2([ni,nj])==True:#인접0다가가기로 벽만날수있으면->1의 0화     
                    amap[v[0]][v[1]]=0
                    return True# 걍 자신이 변하는지 하나씩 볼거라. 어라 복잡하게 풀었네 걍 네곳 보면 되는데.(아마 초반에 1<->0변함관계잘못봐서)
                # 1 한개씩 넣을거라 while로 여러 1 볼필요 없음
                #aque.append([ni,nj])
                #visited[ni][nj]=True
    return False

# abcd                    
cnt=0
while(len(ones)!=0):# 다음초
    visited=[[False]*m for _ in range(n)]
    cnt+=1

    left=len(ones)
    #bfs
    for i in range(len(ones)): # 하나씩보다 bfs로 한번에가 낫나.
        if bfs(ones[i])==True: # True면 pop
            # amap[ones[i][0]][ones[i][1]]=0
            ones.pop(i)
    
print(cnt,left )#~



# 3m+
#   + 딴 생각 쫌 함