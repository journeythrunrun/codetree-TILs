# 1) N번(~100) 움직 # 방향, 거리(~10)_1초에 한칸
# -> 다시 (0,0)로 올 때가 몇 초 후인지 / 못 오면 -1 

# 2) 저장 -> 초씩 움직여


import sys
n=int(sys.stdin.readline())
answer=-1
str_data = [ sys.stdin.readline().split() for _ in range(n) ]
r, c=0,0
dict1={'W':[0,-1], 'S':[1,0], 'N':[-1,0], 'E':[0,1]}
count=0
for i in range(n):  # str_data[i]

    for j in range(int(str_data[i][1] )): # 3
        r=r+dict1[str_data[i][0]][0]
        c=c+dict1[str_data[i][0]][1] # 1새위치
        #2탐색
        count+=1
        if r==0 and c==0:
            answer = count # i+1)
print(answer)