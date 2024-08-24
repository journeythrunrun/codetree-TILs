# 1)
# 1<= <=N 숫자 중 => M개의 숫자를 골라 만들 수 있는 모든 조합

# 2) combinations _m1
# - 예시 => '중복' 없음
import sys
from itertools import combinations
inpu=sys.stdin.readline
n,m= map(int, inpu().split())


for a in combinations( range(1,n+1) ,m ): # m개씩
    # print()
    for i,one in enumerate(a): # m개
        if i== len(a)-1:           
        # if one == a[-1]: # 튜플 인덱싱
            print(one)

        else :
            print(one, end=' ')

# 4) m,n=1,2이상-> 개수 아니라 아무것도 출력 안해야함 | 1,1 | m=n