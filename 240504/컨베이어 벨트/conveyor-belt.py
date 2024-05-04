# 1) 숫자는 반시계방향 회전
# -> t초 후 컨베이어벨트 숫자

# 2) t초만큼 인덱스를 -= : 원행열은 없으니 앞 넘어가면 연산해서 맨 뒷쪽으로 가게.

import sys
n,t= map(int, sys.stdin.readline().split())#~ r
# 숫자 : 시계방향으로 줌
amap=list(map(int, sys.stdin.readline().split()))+list(map(int, sys.stdin.readline().split()))
# amap=  [ list(map(int, sys.stdin.readline().split())) for _ in range(2)]
#  if n개보다 적  3 초 : [0-3~: ] # n개
#  else

# 에러 안나네print(amap [1:100])
# 수식 귀찮다
for i in range(2*n):
    if -t+i > 2*n-1 :
        print(amap[-t+i-n],end=' ')
    else:
        print(amap[-t+i],end=' ')
    if i== n-1:
        print()


# print(*amap[-t:-t+n],*amap[],sep='' ) # n개씩 출력 : 수식 좀 귀찮긴하다

## 출력

#@ 2차원

# 17m