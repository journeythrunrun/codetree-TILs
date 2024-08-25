# 1) 
# 고유한 위치의 점 n개에서 점 m개 선택-> '거리가 가장 먼 두 점 사이의 거리 '의 최소값 -> 최소값 제곱
# 점 위치 중복 없




# 2) n,m=20 -> O(n^4)에서도 충분 ^5조사
# O(  생성(날아감) + nCr_  *[거리] *r*r ) # *경우의 수 아님_ nCr(다음 인덱스부터) )
#  < O( n*r*n*r )

import sys
inpu=sys.stdin.readline
n,m=map(int,inpu().split())

from itertools import combinations # 와 어케 이걸 collec이라고 다 
amap=[ list(map(int,inpu().split()) ) for _ in range(n)  ]
# sets = list(collections( range( n ) ,m)) # - 'comb의 요소값은 index'여야하니까 'range'로 넣기' | 추가 장점 : 여러 차원일 때 해당 내부 요소의 수 까지 안나와도 돼서 좋을 때도 있음.
# print(amap)
min_answer='initial'
for aset_index in combinations( range( n ) ,m) : # aset_index=(2,4,5)
    # 최소값을 찾아야하는 경우의 수들이 거치는 곳
    temp_answer=0
    # aset에 있는 것들 끼리 _ 모든 두 점

    for i in range(len(aset_index)) : # - 값 대신 'aset_index의 인덱스'로 접근.'range'로 접근 
        #  i->aset_index[i]
        for j in range(i+1,len(aset_index) ) : 
            # 주소 참조라하기엔
            # print(i,j,amap)
            # print(amap[i], amap[j] ) 
            # print(amap[i][0]-amap[j][0] , (amap[i][1]-amap[j][1]))
            # 아 해당 셋에서는 순차적 길이인덱스로 amap에 바로 적용할 순 없음 i->aset_index[i]

            temp_answer=max(temp_answer,  (amap[  aset_index[i]  ][0]-amap[ aset_index[j] ][0])**2+  (amap[aset_index[i] ][1]-amap[aset_index[j] ][1])**2  ) # 제곱 루트 구현별시복
    
    min_answer= temp_answer if min_answer=='initial' else min(min_answer, temp_answer)
    # print('aset', aset_index ,'temp_ans',temp_answer,'min_ans', min_answer)
# 제곱루트 뺌
print(  min_answer )
# 4) 


# 
# # L1 L2