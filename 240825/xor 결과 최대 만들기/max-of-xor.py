# 1) n개_0 이상의 정수 -> m개 뽑아 모두 xor -> 최대값 





# - 이미 있는 대상에서 'm개'의 숫자' '뽑'  # 그래도 중복해서 'm개'를 '뽑'을 수 있지 # X_-> 중복 불가능 -> combi
#   + 이건(특정값 순차적으로 사용(sort수준) DP로 푼) product(자리구별_미sort)는 아니고 해봐자 중복있는 'com_순차적으로 나열해서 풀어도됨_1대1대응'
#   > 이 DP는 특정숫자가 첫번째인걸로 치며 순차적으로 사용해나감. 
#   + 요소들에 대해 교환 법칙 성립하는 연산이라 sort된 한 버전으로 사용해도 괜찮음. 애초에 뽑는다고 하기도 함(?)
#   + combination 중에서도 반복(반복 시 메모리 초과) 없는 걸로 연산 간소화 가능한 이유
#     + 간소화 아니고 걍 문제 저 말이 반복 없는 걸로 고정된 걸수도 있음 # X_같은 것끼리 xor 하면 무조건 0임. 다른 것끼리 xor하면 각 개인보다 증가할 수도 감소할 수도 있지만, 0이상임. 음 근데 새 xor대상이 0이랑 해야 높은 값 가지는 놈일 수도 있는데 말이다.

#   
# - comb _ 굳이 DP로? 이긴함. 다른 유형 문제를 DP로 풀고, 고르기 문제는 라이브러리 4가지 유형 외우기 용으로 쓰자.
# - [[itertools]] 확통_중복 ㅠ : "product"
#   + [ㅠ]product(자리구별/반복뽑[중복] 가능) [[곱하기]] / [P]permutations(자리구별o/반복x)
#   + combinations_with_replacement() ( 자리구별x / "반복o")
#   + combinations( 변수_iterable/2차원 리스트도 ㄱㄴ/.. , r ) # 한 껍질 벗긴 것에서 r개 뽑아줌

#   + m1) product(list1, repeat=3)_list1의 요소[행이 될 수도 있음] 를 통째로repeat개 고름
#   + m2) product( *{2d_list} )_2d_list의 각 행에서 1개씩 고름 ## (모든 곳에서 두 껍질 들어가는 대신 그 안에선 1개씩만 가져옴 )_반환하는 각 튜플의 요소 수 = 2d_list의 행의 수  
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

# - n개에서 k개 뽑기 : 이전처럼 연속적인 수 아님= 그렇게 그 부분에 +1할 수 없음 _ "인덱스"이용 시 연속적임

def search (recent_index,cnt):
    # - 1> 재귀 탈출
    # - 문제 설명에 대한 알고리즘 풀이는 맞아도, 직접 테스트 케이스 넣었을 때 정답으로 나온 출력으로 다른거알았으면, 적어놓고 그부분 코드 추가 변경해야함.
    #   > 이론적으로 print( 4 xor) 안됨. 1개 짜리 xor하는 거 문제에서 얘기도 없었으나 정답은 4값으로 출력나와야 함
    # 근데 나중에 수정한 부분으로 인해 이부분 이제 없어도 될 수도 있음
    if cnt==m : # 1개면 바로 True라 ^ 연산 시도도 안됨
        amax[0]=max(amax[0], aset[-1][1]) 
        # - M_X 여기서 for xor연산_비효율.
        # -> 대상을 넘기지말고 연산결과를 넘겨야겠다 -> BUT, append는 ^= 한다쳐도, pop이 귀찮으니까(이전 요소만큼만 ^=취소해야함)  
        # -> (최종) 저장해나갈 때 병렬 요소 추가
        # ->  그것도 귀찮으니, 영향 없는(뇌로 암산) 시간복잡도 정도_ 새저장소 1개에 append 후 나중에 연산 
        #   -> But, [append('리스트')해버리면 주소참조라, '변경되는 리스트면 같이 변경돼서' 귀찮아짐. 대신 주소 참조하며 그런 방향으로 '전역화' 잘됐던 거일 수도 & append시 내부에 여러 개 여도 O(1)  # - 다른 변수의 순서, 추가, 전역화 : tuple 순서 있음 | (a=(3,) )== (a=tuple([3]_iterable) ) | 불변형이긴 한데 a=([3,3],) -> a+=([4,4],) | 순서 있음 | BUT 지역변수임,  str 동일 ] 
        return 

    # - 특정 부분 바꾸고 -> !!! 코드의 모든 흐름에서의 요소 체크
    for j in range(recent_index+1, len(amap)) :#  - 다음 요소부터 _ recent_index'+1'
    # for j in range(recent_index, len(amap)) :#  - 반복있는 comb

        aset.append([j,aset[cnt-1][1]^amap[j]]) # - j-1아니고 'cnt-1' : 'aset의 이전 요소'는 'cnt_aset관련_-1'임 > 이전 j값은 aset에 들어가있지도 않았을 수 있음.
        search(j, cnt+1)
        aset.pop()


for i in range(len(amap)) : # - 반복 없는 comb이면 -m개 이용해서 마지막 부분 좀 줄이는 것도 있긴함
    aset.append([i,amap[i]]) # - 요소 첫 개일때, 함꼐 xor할 대상은 0이긴 하지만((동일한 식에서 xor하기 위한 상대대상 초기값)), 1개여도 그 xor 결과를 넣는 코드 위치임. 0이미 지났고 해당 값. 
    search(i,1)
    aset.pop()

print(amax[0])

# 4)  m,n = 1,1_(print( 1 xor 0과 한다고 친다보다. ))_0보단? 
# - 1,5 _ '테스트셋 제대로 만들어'서 안돌리고 1시간제출함 
# - m=n


# - 1h 29m 
# - 맨 위에 좀 적음

# - 값을 '오름차순'으로 안주더라도 어차피 순서 무관인 연산결과값 쓰는 거라 상관없음 & 어차피 인덱스로 +1하는 코드고 말이다.
# - xor ^