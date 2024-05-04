# 1,2) m개 구슬 : 1초에 상하좌우 숫자 중 가장 큰값 위치로 이동[max값 & 상하좌우 우선순위]
# -> 중복된 위치 있으면 : 사라짐
# -> t초후 남은 구슬 수

import sys
n, m, t = map(int, sys.stdin.readline().split())
# int() : 앞뒤 딱붙은 공백 지워주는거 말고는, 일반적으로 생각한 int() 제한이랑 같음 
amap=[ list(map(int, sys.stdin.readline().split()))  for _ in range(n)]
coins=[list(map(int, sys.stdin.readline().split()))  for _ in range(m) ]

# index(): 해당 값가지는 인덱스 한개만 알려줌
dr=[-1,1,0,0]
dc=[0,0,-1,1]

dele=set()
for i in range(t): ## 초
    if m-len(dele)==0:
        break
    for j in range(len(coins)):## 구슬
        if j in dele :
            break
        ## 최적화 안함
        val=[]
        posi=[]
        for k in range(4):
            nr=coins[j][0]+dr[k] # 인덱스용 변수의 값을 1부터의 범위로 '저장할때'. 대신 nr nc변수를 '사용하는 곳'에서 '-1'하면 됨
            nc=coins[j][1]+dc[k]
            if 0<=nr-1<=n-1 and 0<=nc-1<=n-1 :
                val.append(amap[nr-1][nc-1]) # 값을 저장
                posi.append(k)
        if val :  #### 사방에 이동할 게 있었으면
            maxv=max(val)
            inde=val.index(maxv)
            coins[j][0]=coins[j][0]+dr[posi[inde]]
            coins[j][1]=coins[j][1]+dr[posi[inde]] # coins[j][1]+dr[inde]#  posi[inde]

    ## 구슬 전부 이동 후 
    ## 중복 위치
    
    for j in range(len(coins)):
        for k in range(j+1, len(coins)):
            if coins[j] == coins[k] : # pop 하면 for j , k 밀려서
                dele.add(j) # j,k
                dele.add(k)   
                # coins=coins[i]
                # coins.pop(k-    )


print(m-len(dele))
# 23m