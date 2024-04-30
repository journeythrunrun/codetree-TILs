x,y=0,0
# L : 반시계

dx=[1,0,-1,0]
dy=[0,-1,0,1]
dire=3

# - rotation [방향회전]
# dire =(dire+1)%4 # 시계
# dire =(dire-1)%4 # 반시계

import sys
data=sys.stdin.readline()
for a in data :
    if a=='L':# 딕셔너리 코드 압축 굳이
        dire =(dire-1)%4
    elif a=='R':
        dire =(dire+1)%4
        
    elif a=='F':
        x,y=x+dx[dire],y+dy[dire]
print(x,y)