# 1) 인접 칸중 1이 적혀있는 칸의 수가 3개 이상인 곳의 개수 
# 2) 쉬워서 이 문젠 설계 안하고 바로 품

import sys

n=int(sys.stdin.readline())
# split -> 리스트화 ['0', '1', '0', '1']
## print(sys.stdin.readline().split()) #['0', '1', '0', '1'] # m2) input()도 그럼
amap=[sys.stdin.readline().split() for _ in range(n)] 

dr=[1,0,-1,0]
dc=[0,1,0,-1]
result=0
for i in range(n):
    for j in range(n):
        count=0
        for k in range(4):
            nr, nc= i+dr[k], j+dc[k]
            if nr>=0 and nr<n and nc>=0 and nc<n and amap[nr][nc]=='1':
                count+=1
        if count>=3: ## 2번 이상 틀리면 탈출로 간략화는 굳이
            result+=1

print(result)