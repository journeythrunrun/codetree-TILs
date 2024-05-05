# 1) 숫자는 반시계방향 회전
# -> t초 후 컨베이어벨트 숫자
# 2) t초만큼 인덱스를 -= : 원행열은 없으니 앞 넘어가면 연산해서 맨 뒷쪽으로 가게.

import sys
# readline() : 입력의 마지막 줄 아닌 줄은 \n붙음.  
n,t= map(int, sys.stdin.readline().split())
## 숫자 : 시계방향으로 줌
amap=list(map(int, sys.stdin.readline().split()))
amap+=list(map(int, sys.stdin.readline().split())) 

#  2) if n개보다 적  3 초 : [0-3~: ] # n개
#  2) else

t%=(2*n)

for i in range(2*n):
    if -t+i > 2*n-1 :
        print(amap[-t+i-n],end=' ')
    else:
        print(amap[-t+i],end=' ')
    if i== n-1:
        print()

# m1) n개씩 출력 : 수식 좀 귀찮아서 패스
## print(*amap[-t:-t+n],*amap[],sep='' ) 
## if len( )

# - 25m
#  > 17m~ : 디버깅 : '여러 바퀴 시간' 케이스 인지

# - 't초' / '회전' -> '여러 바퀴' 돌고 '제자리'오는 것도 감안

# - (리스트 인덱스) amap [1:여기값은 초과해도 에러 안남]

# - '런타임에러'-> """"인덱스""""" 인가
#   > n을 두 번 뺄 일은 없을텐데. 리스트의 각 요소 한바퀴 훑어 출력하니까.
#   > 엣지케이스인가
#     n==1 
#     t : 1,3 
#   + 여러 바퀴 돌 시간을 입력한 경우