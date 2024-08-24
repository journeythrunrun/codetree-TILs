# 1) n개_0 이상의 정수 -> m개 뽑아 모두 xor -> 최대값 





# - 이미 있는 대상에서 'm개'의 숫자' 뽑  # 그래도 중복해서 'm개'를 '뽑'을 수 있지 # X_-> 중복 불가능 -> combi
#   + 이건(특정값 순차적으로 사용(sort수준) DP로 푼) product(자리구별_미sort)는 아니고 해봐자 중복있는 'com_순차적으로 나열해서 풀어도됨_1대1대응'
#   > 이 DP는 특정숫자가 첫번째인걸로 치며 순차적으로 사용해나감. 
#   + 요소들에 대해 교환 법칙 성립하는 연산이라 sort된 한 버전으로 사용해도 괜찮음. 애초에 뽑는다고 하기도 함(?)
#   + combination 중에서도 반복 없는 걸로 풀어도 되는 이유(메모리에러 났었나) : 

#   
# - comb _ 굳이 DP로? 이긴함. 다른 유형 문제를 DP로 풀고, 고르기 문제는 라이브러리 4가지 유형 외우기 용으로 쓰자.
# - [[itertools]] 확통_중복 ㅠ : "product"
#   + [ㅠ]product(자리구별/반복뽑[중복] 가능) [[곱하기]] / [P]permutations(자리구별o/반복x)
#   + combinations_with_replacement() ( 자리구별x / "반복o")
#   + combinations( 변수_iterable/2차원 리스트도 ㄱㄴ/.. , r ) # 한 껍질 벗긴 것에서 r개 뽑아줌

#   + m1) product(list1, repeat=3)_list1의 요소[행이 될 수도 있음] 를 통째로repeat개 고름
#   + m2) product( *{2d_list} )_2d_list의 각 행에서 1개씩 고름 ## (모든 곳에서 두 껍질 들어가는 대신 그 안에선 1개씩만 가져옴 )_반환하는 각 튜플의 요소 수 = 2d_list의 행의 수  

# - DP
import sys
n, m = map(int, sys.stdin.readline().split())
amap = list(map(int, sys.stdin.readline().split()))

if m==1 and n==1:
    print(amap[0])
    exit()
elif m==1:
    print(max(amap))
    exit()
aset=[]
amax=[0]

target=[]

# 32+101
# 011
# 이전처럼 연속적인 수 아님 _ 인덱스가 연속적임
temp=[0]
def search (recent_index,cnt):
    # 재귀 탈출
    # print(cnt)
    # 1개면 ^ 연산 안되고 바로 cnt==m되구나. 하긴 알고리즘상은 맞아도 애초에 문제에서 비대상 xor은 말안하긴했음 -> 출력으로 다른거알았으면 그부분 추가로 코드에 반영해놔야함.
    if cnt==m :
        # print(target)
        # print(aset)
        
        temp[0]+=1
        # print(temp[0])
        target.append(aset)
        # print(aset)
        amax[0]=max(amax[0], aset[-1][1]) # X_ 여기서 xor_for 보단 대상을 넘기지말고 연산결과를 넘겨야겠다._ append는 ^=한다쳐도, -> pop이 귀찮으니까 병렬 저장 요소 추가 ->  그것도 귀찮으니 시간복잡도 보다 적은 저장소1개추가[append(순서있는리스트)해버리면 주소참조귀찮아짐 tuple+=(j,) or str. .]
        return 

    # 바꾸고 코드의 모든 흐름에서의 요소 체크
    for j in range(recent_index+1, len(amap)) :#  # - 2_연달아가능하게recent+1로  ~
    # for j in range(recent_index, len(amap)) :#  메모리 초과. 어차피 xor
        # print('111',j)
        # print('f',amap[j])
        # print(aset[cnt-1][1])
        aset.append([j,aset[cnt-1][1]^amap[j]]) # j-1 cnt-1
        # print(aset)
        search(j, cnt+1)
        aset.pop()
# 4 1
# 3 7 234 346
# 12345라

# m개 검사 굳이?
for i in range(len(amap)) : # 사실 -m개 이용해서 마지막 부분 좀 줄일 수 있긴함. 

    aset.append([i,amap[i]]) # 첫번째 께 반영이 안됐었네 
    search(i,1)#
    aset.pop()
print(amax[0])
# amax=temp_max=0
# print(target)
# for a in target:
#     for b in a:
#         temp_max^=amap[b]
#     amax=max(amax,temp_max)
# print(target)
# print(amax)
# 4)  m,n = 1,1_(print( 1 xor 0과 한다고 친다보다. ))_0보단? | 1,5 _ 테스트셋 제대로 만들어서 안돌리고 1시간제출함 | m=n


## 중복숫자도 뺄 수 있어야하려나


# - '오름 차순'으로 안주더라도 어차피 순서 무관인 연산결과값 쓰는 거라 상관없음

# - 자연수 0 여부 

# - xor ^ 

# - 1h 29m