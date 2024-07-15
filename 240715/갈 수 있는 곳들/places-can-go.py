# 0 이동가능 -> 도달 가능 칸 수
# for 시작지점 -> 주변 미방문 쳌

# 문제 예시로부터 -> 인접 거리1 초과 이동 가능

from collections import deque
n, k = map(int,input().split()) # std
amap=[list(map(int,input().split()) ) for _ in range(n) ] 
starts=[ list(map(int,input().split()) ) for _ in range(k)]

visited=[ [0]*n for _ in range(n) ]
cnt=0

di=[0,0,1,-1]
dj=[1,-1,0,0]
# m2
# aqueue=deque(starts) # - []가 요소 밖에 이미 있음  # - 실수하니까 queue보다 que로 

aqueue=deque()
for a in starts :  
    a[0]-=1 # rc의 인덱스화 -=1  # - 이건 나중보다 초반에 처리해서 저장해주고 시작해야 덜 헷갈림
    a[1]-=1
    aqueue.append(a) 
    visited[a[0]][a[1]]=1

if 1:
    while(aqueue):
        a=aqueue.popleft()
        # visited[a[0]][a[1]]=1 # > (다른m수정중에)여기에서 하면 괜찮은 인덱스로 들어간것도 이상해짐
        cnt+=1 # 중복 체크하고 넣었기에 ㄱㅊ & 원래 뺄때 출력하듯.
        # if not visited[a[0]][a[1]]:
        #     cnt+=1
        #     visited[a[0]][a[1]]=1
        for i in range(4):
            ni, nj = a[0]+di[i],a[1]+dj[i]
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and amap[ni][nj]==0:
                visited[ni][nj]=1
                aqueue.append([ni,nj])

print(cnt)

# - 21m -> 오류 29m 
#   > 문제 조건 세부추가로, 방법 수정 이것저것 하다가 미세하게 놓치곤 함