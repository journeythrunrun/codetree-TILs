# 0 이동가능 -> 도달 가능 칸 수
# for 시작지점 -> 주변 미방문 쳌

# 문제 예시로부터 -> 인접 거리1만 이동 아님. 
from collections import deque
n, k = map(int,input().split()) # std
amap=[list(map(int,input().split()) ) for _ in range(n) ] 

starts=[ list(map(int,input().split()) ) for _ in range(k)]

visited=[ [0]*n for _ in range(n) ]
cnt=0

di=[0,0,1,-1]
dj=[1,-1,0,0]
# print(starts)
## aqueue=deque(starts) # []   ## ueue
# print(aqueue)
# print(aqueue.popleft())
# if 1:
aqueue=deque()
for a in starts :  # 시작점의 카운팅은
    a[0]-=1 # 행열 -> -1 # 이건 초반데이터에 대해서 다해주고 시작해야 덜헷갈
    a[1]-=1
    aqueue.append(a) # [ a ]  여야 pop할때 a가 빠짐
    visited[a[0]][a[1]]=1

if 1:
    while(aqueue):
        a=aqueue.popleft()
        # 원랜 들어갈때하는데 얘넨 초기값 한번에 넣어줘서
        # visited[a[0]][a[1]]=1 #여기에 하면 괜찮은 인덱스로 들어간것도 이상해짐
        cnt+=1 # 중복 체크하고 넣었기에
        # if not visited[a[0]][a[1]]:
        #     cnt+=1
        #     visited[a[0]][a[1]]=1
        for i in range(4):
            ni, nj = a[0]+di[i],a[1]+dj[i]
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and amap[ni][nj]==0:
                visited[ni][nj]=1
                aqueue.append([ni,nj])

print(cnt)

# 21m