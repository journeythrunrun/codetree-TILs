# 1)
# ‘.’ (빈 공간), ‘S’ (시작점), ‘E' (도착점),_중복 수 없음_‘1'이상 '9’이하의 숫자
# N * N
# -> 3개((이상)) 의 동전 수집하여 도착 # <- topdown #노상관_어차피 가는길에 가지는 경우도 있으려나
#   + 번호가 증가하는 순서대로
#   + 자리에서 미수집 가능
#   + 중복 위치 가능
# => 최소 이동 횟수, 불가능 하면 -1

# 2)
# -> 3개((이상)) 의 동전 수집하여 도착 # <- topdown #X_노상관<-어차피 가는길에 가지는 경우도 있으려나


# M1_X_숫자들 이동할 때의 최소 거리_두 단계?그래도다름 첫위치부터 첫값까지의도 포함되면 세트다름. -> 걍 전체 경우의 수 셋트 구하자. n도 작으니까 괜찮 ##2,4,7-> 그 첫




#M2 값들 세개 고름. index로. 0,6,7  # - 자세한 변수 형식은 자세한 구현 때가 맞을듯#iabc
# - 이동거리 연산 : 거리함수값 다섯개 더하기+=
#   + 영향시복_변수로는*r이긴한데 r이 3이라 의미없는수준(기타 상수는 의미없음 1...,5) ((n=20))
#   + [ abs(target[ia][0]-target[ib][0])+abs(target[ia][1]-target[ib][1]) ] # - 어차피 변수이름 다른 거 썼음
# - M_Xfor동안 모든 요소들 끼리의 거리 순차적으로 누적해뒀다가 더해도 논리상 다름_이동 연산[미리 저장해두기.]
#  =>distance[0] #distance=[]# i=0_(1번째수-2번째수_ix) #
# -min값 [answer=min(answer,)]

# - 백트래킹 vs 라이브러리 (r_3_*nCr[n^2이하]_*_r_ ) -> 문제의 n값에서 라이브러리써도 시간복잡도 ㄱㅊ



# 3) - 시복 : 20 < 100 -> O(N^4) # n적용 전에 외운 정리 적을 때는 N.
# - 이전 정리와는, 평균과 항상 되는 케이스의 차이일 수도 있음
#
# N 범위 100 O(N^4)
# N 범위 500 O(N^3)
# N 범위 2,000 O(N^2)

# N 범위 100,000 O(NlogN) # 백만은 안되네
# N 범위 10,000,000 O(N) # 대신 이건 천만이네
import sys
inpu = sys.stdin.readline
n = int(inpu())

# - 한 행의 입력문자가 붙어서 들어올 때  ->  inpu().split()[0]  # - split()은 inpu 뒤에 붙은 엔터 없앰 -> 대신 문자열밖에 리스트 또씌워져서(string 붙어서 들어왔기 때문에 split으로 리스트의 다른 요소로 분리는 안됨) [0]
# amap=[ inpu().split()[0]  for _ in range(n) ] #['..3.', '2..E', '.1..', '5S.4']
## print(amap) # [['..3.'], ['2..E'], ['.1..'], ['5S.4']]
## 구_print(amap) # inpu의 뒤에 엔터 # ['..3.\n', '2..E\n', '.1..\n', '5S.4']

amap = []
target = []
se = [[0, 0], [0, 0]]
for i in range(n):
    amap.append(inpu().split()[0])  #'..3.'
    for j in range(n):
        if amap[i][j] == 'S':
            se[0][0], se[0][1] = i, j
        elif amap[i][j] == 'E':
            se[1][0], se[1][1] = i, j
        elif amap[i][j] != '.':
            #숫자면 위치 저장
            target.append([int(amap[i][j]), i, j])  #값, i, j
# - ! print 주석하려다가 실수로 sort도 주석함

target.sort(key=lambda x: x[0])   #첫 요소에 넣은 값 기준으로 sort
# - sort 확장 활용 | lambda ~~ def, : ~~ return
#   + target.sort(key=lambda x : (-x[2],x[0],x[1] ) ) # + 튜플로 쓰네
#   + lambda: " ".  join(map  (lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ") )_map  )_join

##print(target) # [[1, 2, 1], [2, 1, 0], [3, 0, 2], [4, 3, 3], [5, 3, 0]]
# - 중간중간 바로 출력해서 검증하는 방법 좋다.
#   + 오류 되게 빨리 찾음. 후에 알고리즘 구체화때도 저 요소에 있는 값을 바로 볼 수 있어서, 구현 편하고 오류 덜할듯

# - str인 정수 : 파이썬은 C언어와 달리 아스키가 아니었던 것 같은데 대소관계가 str에서 어떠하지 -> 걍 정수형str이면 int로 바꿔서 비교해라. 정수형 아니면 대소관계 비교할 필요도 없음.
answer = 'yet'  # - min_answer의 초기최대값 생각해내기 귀찮아서 문자 넣고 처음에 값넣을땐 처음인지 조건따져좀   # - <- min이면, 반대로 최대값

from itertools import combinations  # 현재23m

def distance(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1])


# - combi 라이브러리순서 : 사용했을 떄 순서 안섞임
def self_combinations(target, haha):  # r=3처럼 개작은 경우 & # 근데 따로 함수로 만들어서 똑같이 전달하려면(저장꼴) *r못아낌. forforfor내에 하기엔 코드지저분 *r 아끼기도 가능
    temp = []
    for i in range(len(target)):
        for j in range(i + 1, len(target)):  # i+1. 반복이면 _
            for k in range(j + 1, len(target)):
                temp.append((target[i], target[j], target[k]))
    return temp

    # 한가지 리턴하고 끝나네 return (target[i], target[j], target[k])


# 4_i
# print( list(combinations([1,2], 3)) ) # []
# for a in []: # 에러 안나고 그냥 for 바로 탈출
#     print('00')
for aset in self_combinations(target, 3):  # ( [1, 2, 1], [2, 1, 0], [3, 0, 2]
    temp_answer = 0
    # [인덱스]쓸때 모양 그거 확실한지 생각.
    temp_answer += distance(se[0], aset[0][1:]) + distance(aset[2][1:], se[1])  # [1,2],
    temp_answer += distance(aset[0][1:], aset[1][1:]) + distance(aset[1][1:], aset[2][                                                                              1:])  # 한 aset에만 [1:]복붙 놓침실화냐 급해도 요소 하나하나 넘어가듯 봐라라쫌 # 문제 꽤 맞췄어도, 코드논리 틀렸을(,실수) 가능성 꽤됨.
    if answer == 'yet':
        answer = temp_answer
    else:
        answer = min(answer, temp_answer)
if answer == 'yet':
    print(-1)
else:
    print(answer)

# 4)
# n=2 -> 3개 못고름 -> -1 나와야함-> 특정케이스보다, 이정도는 논리로 전체케이스 체크
# 떨어져있는 값_논리뇌체크 = 값sort & 인덱스썼다#이부분굳이테스트케이스로?
# 아직 미처리한 케이스(answer=-1)뒤에다 적었어야.

# - nCr은 다항식이나 log,root등으로 표시시 ? 대략? _  & GPT근거수식()

# - 1h 23m : 공부용 필기를 주석에 했던 시간은 = 끽해봤자 5m되려나
#   + 1h 14m : 8퍼에서 틀림
#     + 1h 넘은 거라 그냥 틀린 테스트 케이스봄 -> 엣지라기보다 일반적인 케이스 틀렸구나 암
#   + 전체 논리의 '검증' : 아는 제일 어려운 케이스에서 전체 흐름 출력 체크?
#     -> temp_answer+=distance(aset[0][1:],aset[1][1:])+distance(aset[1][1:],aset[2][1:])  # 한 aset에만 [1:]복붙 놓침실화냐 급해도 요소 하나하나 넘어가듯 봐라라쫌 # 문제 꽤 맞췄어도, 코드논리 틀렸을(,실수) 가능성 꽤됨.