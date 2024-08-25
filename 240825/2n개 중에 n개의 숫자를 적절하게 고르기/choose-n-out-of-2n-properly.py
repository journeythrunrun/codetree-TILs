# 1) 2n개의 숫자 -> n개씩 2개의 그룹으로 분리 -> '각 그룹 원소합'의 차_ 최소값

# 2)
# - ~O(N^4), N=2n=20  # n이 100보다 훨씬 작은 20 (만약 10으로 치면 2도있긴한데 대충 저만큼이다. -> 'n^2'도 100이라 O(N^4)=O(n^8)까지 ㄱㅊ )
#-> n개 뽑 : 두 가지 그룹 중에 한 곳으로 나누는 거라, 선정한 것이 아니면 무조건 다른 그룹.

# - 시간복잡도 허가범위의 코딩 빠른 풀이
#   + ('n'_[range생성]_[combi]와 직렬이 *가 아님. 스스로도 남도 그 변수번을 반복적으로 해야 *임. 한 번만 하는 거라 곱하기 아님. 곱하기는, 다 대 다여야함. )
#   + O( 'n'_[range생성]_지워질 +   'n'*nCr['n'* r[2]] + nCr(생성되고 그 생성된 길이를 for에서 돔) *'n'[for] *'n'[in]    ) # N,n 뇌에서 대략화
#   + Ex. O( 'n*n' + r*NCr + NCr[for문]* k))
# for selected in combinations(range(n*n),k):
#   for _ in range(k):
#     print(3*4)

#   + 오히려 생각보다 더 복잡해지기도 하는 것 같은 기분

import sys
inpu = sys.stdin.readline
n = int(inpu())
amap = list(map(int, inpu().split())) 

from itertools import combinations
min_answer = 'initial'

# for aset in combinations(amap, n): # - comb 등 경우의 수 -==> "인덱스"
# - 인덱스화 : amap -> range( len_amap의 전체 요소 수) : 시간복잡도에서 더해지는 range 생성항은 어차피 N 수준 밖에 안됨. 
#   + -> aset -> aset_index
for aset_index in combinations(range(2 * n), n):  # - range도 iterable 
    sums = [0, 0]

    # - ! 2n안 되고 2*n
    # print(aset_index) # - range에서 2개 뽑은 거 : (0, 1) _ list아님
    # - 이중 논리 더 복잡함# for i in aset_index :
    for j in range(2 * n):
        if j in aset_index:  # - set화로 in 간단화는 굳이 안함
            sums[0] += amap[j]
        else:
            sums[1] += amap[j]

    temp_answer = abs(sums[0] - sums[1])
    if min_answer == 'initial':
        min_answer = temp_answer
    else:
        min_answer = min(temp_answer, min_answer)
print(min_answer)
# 4)
# n=1 : 2n개의 데이터라 2개나 있음
# - 중복값 : '인덱스'로 사용해서 '고유'함.


# - 20m