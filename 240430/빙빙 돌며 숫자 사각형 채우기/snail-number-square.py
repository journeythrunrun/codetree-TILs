# 1) 달팽이 회전값 맵 만들기
# 2) 2.0) 새 nr nc
# 2.1) 맵크기 초과 or 방문 했던곳 => 방향회전
# 2.2) 새로운 r,c , 값저장 

import sys
n,m=map(int,sys.stdin.readline().split())

amap=[ [0]*m for _ in range(n)]

# 시계방향 # 다른 케이스 3-index가능하도록 = 같은 수평선 [1][2]에 있어야함 OR 이 dr에 새수식
dr=[0,1,0,-1] 
dc=[1,0,-1,0]
r,c=0,0
index=0
amap[0][0]=1
for i in range(1,m*n):
    nr,nc=r+dr[index],c+dc[index] # 기존방향으로 가봄
    if nr <0 or nc<0 or nr > n-1 or nc > m-1 or amap[nr][nc]!=0:
        index=(index+1)%4 # 방향업데이트
    r,c=r+dr[index],c+dc[index] # 이동
    amap[r][c]=i+1
for a in amap :   
    print(' '.join(map(str,a)) )