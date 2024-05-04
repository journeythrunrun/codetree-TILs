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
    if m-len(dele)==0: ## 효율++
        break
    for j in range(len(coins)):## 구슬
        if j in dele :
            continue ###  break로 해버림 한 10분썻나
        ## 최적화 안함
        val=[]
        posi=[]
        for k in range(4):
            nr=coins[j][0]+dr[k] # 인덱스용 변수의 값을 1부터의 범위로 '저장할때' : 대신 nr nc변수를 '사용하는 곳'에서 '-1'하면 됨
            nc=coins[j][1]+dc[k]
            if 0<=nr-1<=n-1 and 0<=nc-1<=n-1 :
                val.append(amap[nr-1][nc-1]) # 값을 저장
                posi.append([nr,nc])
            
        if val :  #### 사방에 이동할 게 있었으면. if문도 max 찾는 것도 굳이 최적화 안함
            maxv=max(val)
            inde=val.index(maxv) ## 여러 개 있어도 1개의 인덱스값 줘서 상하좌우 우선순위.
            coins[j][0]=posi[inde][0]
            coins[j][1]=posi[inde][1] # - 가끔 저장한 형식 사용 실수하네. 예시 적어놔야하나 [ , ]

    ## 구슬 전부 이동 후 
    ## """중복""주의" 위치 : 이미 제거된 애들이랑은 겹쳐도 상쇄 안되는데, 그게 고려 안됐네[2]
    for jj in range(len(coins)): 
        if jj in dele : # 이미 사라진 애들은 continue! # 데이터 아예 삭제( m2)pop이나 remove)해버리는 거 아니면 해당 중복위치 탈출 조건문(m1)&다른데이터에 저장) 필요.
            continue
        for kk in range(jj+1, len(coins)):
            if kk in dele:
                continue
            if coins[jj] == coins[kk] : # pop 하면 for j , k 밀려서
                dele.add(jj) # j,k
                dele.add(kk)   

print(m-len(dele))
# - 59m ((잠시 후 테스트 떠서 맞은 줄 알고 필기 정리한 있던 시간 빼졌는지 모르겠음))
#   > 23m + 30m(디버깅: 일분 수정했어도 제출에선 틀림) + 6m (( 50m쯤 해설보긴했는데 알고리즘이 많이 달라서 그냥 다시 내 코드분석해서 해결함 ))
#   + [2] 중복 위치 : 이미 제거된 애들이랑은 겹쳐도 상쇄 안되는데, 그게 고려 안됐네
#     이미 사라진 애들은 continue! < ~~ > 데이터 아예 삭제(pop이나 remove)해버리는 거 아니면 해당 중복위치 탈출 조건문 필요.
# - break <-> continue 주의해라