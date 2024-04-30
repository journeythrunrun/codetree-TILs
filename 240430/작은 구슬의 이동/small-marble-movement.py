# 1) L
# 방향소요 1
import sys

n,t=sys.stdin.readline().split()
r,c,d=sys.stdin.readline().split()
index={'U': 0,'D':3,'R':1,'L':2}
dr=[-1,0,0,1] # 반대방향: index=3-index가능하기위해, 반대방향으로 짝꿍이 [1][2]에 있어야함 # U, R,"L", 
dc=[0,1,-1,0]

n=int(n) 
t=int(t)
r=int(r)
c=int(c)
# m1 수식으로 남은 거 빼기/나머지/나누기해서 한꺼번에 점프 두번 : 굳이
# m2 한칸씩 count
inde=index[d]
for i in range(t):
    nr,nc= r+ dr[inde],c+dc[inde] # 새 일반방향 한칸
    if nr < 1 or nc<1 or nr >n or nc>n :
        inde=3-inde # 회전도 1회 소멸  ## r,c= r+ dr[index[d]-3],c+dc[index[d]-3] # 
    else :
        r,c=nr,nc ## 이동

print(r,c)