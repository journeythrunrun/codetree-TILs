# 탈출 가능 경로 있는지
# 뱀없1
n,m = map(int,input().split())
amap=[ list(map(int,input().split())) for _ in range(n) ] # 아놔 요런실수 _ 에러 시 사용데이터 다  출력코드?

from collections import deque
visited=[[0]*m for _ in range(n)]
di=[0,0,1,-1]
dj=[1,-1,0,0]
# print(amap)
def bfs(v): 
    answer=0
    aqueue=deque([v]) # [ ] 
    visited[v[0]] [v[1]] = True
    # print(aqueue)
    while (aqueue):
        v=aqueue.popleft()
        # print(v)
        if v[0]==n-1 and v[1]==m-1:
            answer=1
            break
        for i in range(4):
            ni,nj=v[0]+di[i],v[1]+dj[i]
            # print(ni,nj)
            # 먼저
            if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and amap[ni][nj]==1 :
                    aqueue.append([ni,nj]) # 거리저장 필요 없음
                    visited[ni][nj]=1
    return answer
print( bfs([0,0])  )  
# - 23m