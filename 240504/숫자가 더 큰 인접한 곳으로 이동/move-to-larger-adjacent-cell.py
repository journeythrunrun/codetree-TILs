# 1) 상하좌우 중 더 큰값 만나면 이동 / 없으면 종료
# -> 거친 값

import sys

n,r,c = map(int, sys.stdin.readline().split())
r-=1 
c-=1
amap=[list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

dr=[-1,1,0,0]
dc=[0,0,-1,1]
print(amap[r][c],end=' ')
while(1):
    exist=False
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i] # 1새 탐색
        if n-1>=nr >=0 and n-1>= nc >=0 and amap[r][c]<amap[nr][nc]: #2검사
            # 이동
            r,c=nr,nc
            print(amap[r][c],end=' ')
            exist=True
            break
    if exist==False:
        break
# 9m