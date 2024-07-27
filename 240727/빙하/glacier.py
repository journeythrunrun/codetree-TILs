# 빙하1 
# 1초당 빙하 물에 닿아있는 부분 녹음 but 빙하로 둘러싸여있는 물은 빙하못녹임

# 빙하가 전부 녹는데 걸리는 시간, 마지막으로 녹은 빙하의 크기(1의 개수)
# 2) while(len(left)!=0) for n  
#    1이 미방문 0 만났을 때 : 인접0다가가기로 벽만날수있으면->자신인1의 0화 # 잘못썼넹
# 둘러쌓임 : 
 
#(4) 엣지케이스 = 예제
import sys
inpu=sys.stdin.readline
#
n,m=map(int, inpu().split())
amap=[ list(map(int, inpu().split())) for _ in range(n)]
# n,m=6, 7
# amap=[[ 0 ,0 ,0, 0, 0, 0, 0],
# [0, 1, 1, 1, 1, 0, 0],
# [0, 1, 1, 0, 1, 1, 0],
# [0, 1, 0, 1, 1, 1, 0],
# [0, 1, 1, 1, 1, 1, 0],
# [0, 0, 0, 0, 0, 0, 0]]
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
                
                if ni==1 or nj==1 or ni==n-2 or nj==m-2:
                    return True
    return False


def bfs(v):
    visited[v[0]][v[1]]=True
    aque=deque([v])
    # print(v)
    while(aque):
        w=aque.popleft()
        # 출
        
        for i in range(4):
            ni,nj=w[0]+di[i],w[1]+dj[i] # i대신 0,1실화냐
            if 0<=ni<n and 0<=nj<m and visited[ni][nj]==False and amap[ni][nj]==0:
                if bfs2([ni,nj])==True:#인접0다가가기로 벽만날수있으면->1의 0화     
                    # 한번에 바껴야함 amap[v[0]][v[1]]=0
                    return True# 걍 자신이 변하는지 하나씩 볼거라. 어라 복잡하게 풀었네 걍 네곳 보면 되는데.(아마 초반에 1<->0변함관계잘못봐서)
                # 1 한개씩 넣을거라 while로 여러 1 볼필요 없음
                #aque.append([ni,nj])
                #visited[ni][nj]=True
    return False

# abcd                    
alln=len(ones)
numb=0
another=[]
cnt=0
while(ones):#numb!=alln):# 다음초
    visited=[[False]*m for _ in range(n)]
    cnt+=1

    #left=alln-numb
    left=len(ones)
    # 아 'pop'하면 인덱스 밀리네 | ones 길이로 while문 종료 판단
    # 멍
    #len(ones)-1
    # print('second')
    # ones.pop빼는 알고리즘으로 바꾸기 전에 모든 ones 사용 위치 찾아봤어야지. 
    post=0
    change=[]
    for i in range(len(ones)): # 하나씩보다 bfs로 한번에가 낫나.   # pop되면 어케되려나 이미첨에 계산했으니?     
        # 전체 검사
        i+=post
        if bfs(ones[i])==True: # True면 pop, 바뀔놈
            #numb+=1
            #print(numb)
            change.append(ones[i])

            ones.pop(i)
            post-=1
        #else :
        #    anothoer.append(ones[i])

    for v in change :
        amap[v[0]][v[1]]=0

print(cnt,left )#~


# - 시간많이듬+
#   + 딴 생각 쫌 함
#   > 16분 디버깅 오타
#   + 딴 생각 들거나 멍 때려지면 : 노래 크게 듣기?

#