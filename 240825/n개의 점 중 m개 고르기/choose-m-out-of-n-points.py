# 1)
# 고유한 위치의 점 n개에서 점 m개 선택-> '거리가 가장 먼 두 점 사이의 거리 '의 최소값 -> 최소값 제곱
# 점 위치 중복 없


# - 2.1) n,m=20 -> O(n^4)을 넘어서 O(2^n)에서도 가능
#   + O(  생성(날아감) + nCr_  *[거리] *r*r ) # *경우의 수 아님_ nCr(다음 인덱스부터_경우의 수에 대해 도는 게 아니라, 그 경우의 수안에 점들의 수에 대해서 돌아야함) )
#   > < O( n*r*r*r )

import sys
inpu = sys.stdin.readline
n, m = map(int, inpu().split())

from itertools import combinations  # ! 와 어케 이걸 다 collections로 쓰고 에러날때까지 몰랐지. 기계적 타이핑 & 화면 너무 축소 때문인가
amap = [list(map(int, inpu().split())) for _ in range(n)]
# - 'comb의 요소값은 index'여야하니까 : 'range'로 넣기 | 추가 장점이라고 생각했는데 아닌 거 : r*nCr이라, 각 r이 여러 요소 가지고 있어도 그 길이까지 시간 복잡도에 반영되진 않음

min_answer = 'initial'
for aset_index in combinations(range(n), m):  # - 중첩 반복문 : 가져다쓰기 헷갈리니까, for에서 쓰는 요소 1개 적어두기 #aset_index=(2,4,5)
    # - 최소값을 찾아야하는 경우의 수들이 '거치는 곳' -> 해당 값 관련하여 초기화
    temp_answer = 0

    # - 당연히 '경우의 수들 끼리의 거리 값이 아니라', 한 경우의 수(aset_index)에서, 그 안에 있는 것들 끼리 중 두 점을 고른 모든 경우의 수

    for i in range(len(aset_index)):  # - 오히려 여기선 인덱스의 인덱스의 값이 되버리게 또 인덱스(('aset_index의 인덱스'로 접근.'range'로 접근)) 쓰지 말고, aset_index에 있는 요소값을 가져왔어야 편함
        #  - ! 이중인덱스인데 1중인덱스로 사용해버려서 다른 결과 나왔었음.-> 이중 인덱스= 기왕 i_i 와 같이 쓰자
        #    > i->aset_index[i]
        #    + ! for 도는데도 똑같은 값들로 연산됐었음 : 주소 참조라하기엔 리스트 값 변경하고 있지 않음
        #      + 길이가 보다 큰 거에서의 인덱스를 써야하는데, 길이가 작은 거에서의 이중인덱스였던 걸 거기에 쓰니까, 길이가 큰 대상에서 그 작은길이의 앞 값들만 쓰인거임.
        for j in range(i + 1, len(aset_index)):
            temp_answer = max(temp_answer, (amap[aset_index[i]][0] - amap[aset_index[j]][0]) ** 2 + (
                        amap[aset_index[i]][1] - amap[aset_index[j]][1]) ** 2)  # - 제곱, 루트 : 다 ** ()

    min_answer = temp_answer if min_answer == 'initial' else min(min_answer, temp_answer)

# - 루트하고 다시 제곱 되길래 뺌
#   > 제곱과 루트는 최소 최대 변화도 없음
print(min_answer)

# 4)
# - 39m : 5m정도는 필기
# - (1개만 하는) 초간단 버전 아닌 좀 더 일반적인 테스트 케이스를 만들어서 중간값 테스트해야하는가
#   + i. '논리가 맞다고 생각하는데 과연 해야하는가' 로 안했음 & 논리 단계 코드 간결한 문제.
#   + ii. 이렇게 해나가다가 실제론 틀린 경우 많으면 -> 5) test셋 만들어서 테스트
# # L12