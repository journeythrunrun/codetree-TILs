# 1) 0,0 북방향시작
# N개의 명령 : R: 시계방향90도, L, F 한칸이동
# -> 0,0오기까지의 소요 시간 / 못오면 -1

import sys
data=sys.stdin.readline()
r,c=0,0
dr=[0,1,0,-1]
dc=[1,0,-1,0]
index=3
for i in range(len(data)):
    if data[i]=='L':
        index=(index-1)%4
    elif data[i]=='R':
        index=(index+1)%4
    else :
        r+=dr[index]
        c+=dc[index]
        if r==0 and c==0:
            print(i+1)
            exit()
    # print(r,c)
print(-1)
# 회전에도 1초걸림
# 11m