# 1)
# ‘.’ (빈 공간), ‘S’ (시작점), ‘E' (도착점),_중복 수 없음_‘1'이상 '9’이하의 숫자
# N * N 
# -> 3개((이상)) 의 동전 수집하여 도착 # <- topdown #노상관_어차피 가는길에 가지는 경우도 있으려나
#   + 번호가 증가하는 순서대로
#   + 자리에서 미수집 가능
#   + 중복 위치 가능
# => 최소 이동 횟수, 불가능 하면 -1

# 2) 
# -> 3개((이상)) 의 동전 수집하여 도착 # <- topdown #노상관_어차피 가는길에 가지는 경우도 있으려나


# M1_X_s~시작 숫자는 아직 미정 & 값들 이동할 때의 최소 거리_두 단계?그래도다름 첫위치부터 첫값까지의도 포함되면 세트다름. 걍 전체셋트하자. n도 작구. 2,4,7-> 그 첫 

# new로 수정
# M2 값들 세개 고름. index로. 0,6,7  # =iabc=
# -> 이동연산 : 함수값+=_영향시복*1...,3((n=50)) _ abs(target[ia][0]-target[ib][0])+abs(target[ia][1]-target[ib][1])
# -> X_#_아 거리 누적해서 더하는 거 아님_이동 연산[미리 저장해두기.]
####  => distance[0] #distance=[]# i=0_(1번째수-2번째수_ix) #  
# -> min값 [answer=max(answer,)]
# -> DP vs 라이브러리O(r_3_*nCr _;n^2이하_*_1,3_ # 

# 3) 시복#_^3
#  NCr근사
import sys
inpu=sys.stdin.readline
n=int(  inpu())

# amap=[ inpu().split()[0]  for _ in range(n) ] #['..3.', '2..E', '.1..', '5S.4']
## print(amap) # [['..3.'], ['2..E'], ['.1..'], ['5S.4']]
## 구_print(amap) # inpu의 뒤에 엔터 # ['..3.\n', '2..E\n', '.1..\n', '5S.4']

amap=[]
target=[]
se=[[0,0],[0,0]]
for i in range(n) :
    # 숫자면 위치 저장
    amap.append(inpu().split()[0]) # '..3.'
    for  j in range(n):
        if amap[i][j]=='S':
            se[0][0], se[0][1]=i,j
        elif amap[i][j]=='E':
            se[1][0], se[1][1]=i,j
        elif amap[i][j]!='.' :
            #숫자
            target.append([int(amap[i][j]), i,j ]) # 값, i, j
# 숫자 기준 sort
# print주석하려다가 실수로 sort 주석
target.sort(key=lambda x:x[0] ) # 저번 다른 사용
# print(target) # [[1, 2, 1], [2, 1, 0], [3, 0, 2], [4, 3, 3], [5, 3, 0]]
# 중간중간 바로 확인 괜찮다 오류 빨리 찾고, 알고리즘 구체화때도 저 요소있는 값바로보면서 편하고 오류 덜할듯

# s,E
 
##str이 파이썬은 C언어와 달리 아스키가 아니었던 것 같은데 대소관계가
answer='yet' #변수최대값몇일까 # min이면, 반대로 최대값

from itertools import combinations # 현재23m
# new
# M2 값들 세개 고름. index로. 0,6,7  # =iabc=
# -> 이동연산 :함수값다섯개+=_영향시복*1...,5((n=50))
# + _  _ abs(target[ia][0]-target[ib][0])+abs(target[ia][1]-target[ib][1])
# -> X_#_아 거리 누적해서 더하는 거 아님_이동 연산[미리 저장해두기.]
####  => distance[0] #distance=[]# i=0_(1번째수-2번째수_ix) #  
# -> min값 [answer=min(answer,)]

#~#~
def distance ( one, two ):
    # print(one,two)
    # print(abs(one[0]-two[0])+abs(one[1]-two[1]))
    return abs(one[0]-two[0])+abs(one[1]-two[1])

# combi순서 : 정렬해서 입력줘도 섞여나오네_ X_안섞었던 것 같은데, 확실 항상?
# print('combinations(target, 3):',list(combinations(target, 3)))

def self_combinations(target, haha ): # r=3처럼 개작은 경우 & # 근데 따로 함수로 만들어서 똑같이 전달하려면(저장꼴) *r못아낌. forforfor내에 하기엔 코드지저분 *r 아끼기도 가능 
    temp=[]
    for i in range(len(target)):
        for j in range(i+1,len(target)): # i+1. 반복이면 _
            for k in range(j+1,len(target)):
                temp.append((target[i], target[j], target[k]))
    return temp

                # 한가지 리턴하고 끝나네 return (target[i], target[j], target[k])
# 4_i
# print( list(combinations([1,2], 3)) ) # []
# for a in []: # 에러 안나고 그냥 for 바로 탈출
#     print('00')
for aset in combinations(target, 3): # ( [1, 2, 1], [2, 1, 0], [3, 0, 2]
    # print('1',aset)##########
    temp_answer=0
    # [인덱스]쓸때 모양 그거 확실한지 생각.
    temp_answer+=distance(se[0],aset[0][1:]) +distance(aset[2][1:],se[1])  # [1,2],
    # print(temp_answer)
    temp_answer+=distance(aset[0][1:],aset[1][1:])+distance(aset[1][1:],aset[2][1:])  # 한 aset에만 [1:]복붙 놓침실화냐 급해도 요소 하나하나 넘어가듯 봐라라쫌 # 문제 꽤 맞췄어도, 코드논리 틀렸을(,실수) 가능성 꽤됨.
    # print(temp_answer)
    #4
    if answer=='yet':
        answer=temp_answer
    else :
        answer=min(answer,temp_answer)
    # print('temp_answer',temp_answer)
    # print('answer------',answer)
if answer =='yet':
    print(-1)
else :
    print(answer)

# 4) 
# n=2 -> 3개 못고름 -> -1 나와야함-> 특정케이스보다, 이정도는 논리로 전체케이스 체크
# 떨어져있는 값_논리뇌체크 = 값sort & 인덱스썼다#이부분굳이테스트케이스로?
# 아직 미처리한 케이스(answer=-1)뒤에다 적었어야.

# - nCr은 다항식이나 log,root등으로 표시시 ? 대략? _  & GPT근거수식()

# - 1h 23m : 공부용으로 필기를 주석에 한 시간 끽해봤자 5m되려나
#   + 1h 14m : 8퍼에서 틀림
#   + 1h 넘어서 틀린 테스트 케이스봄
#   + 전체 논리의 '검증' : 아는 제일 어려운 케이스에서 전체 흐름 출력 체크?
#     -> temp_answer+=distance(aset[0][1:],aset[1][1:])+distance(aset[1][1:],aset[2][1:])  # 한 aset에만 [1:]복붙 놓침실화냐 급해도 요소 하나하나 넘어가듯 봐라라쫌 # 문제 꽤 맞췄어도, 코드논리 틀렸을(,실수) 가능성 꽤됨.