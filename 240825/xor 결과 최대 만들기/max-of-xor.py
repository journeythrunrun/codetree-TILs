# 1) n개_0 이상의 정수 -> m개 뽑아 모두 xor -> 최대값


# - 이미 있는 대상에서 'm개'의 숫자' '뽑'  # 그래도 중복해서 'm개'를 '뽑'을 수 있지 #X_-> 중복 불가능 -> combi
#   + 이건 product[자리구별=not sorted]는 아니고 해봐자 중복있는 'combinations[sort된 꼴로(순차적으로 나열해서)풀어도됨]'
#   >> 이 Backtracking는 특정숫자가 첫번째인걸로 치며 순차적으로 사용해나감.

#   + xor(요소들에 대해 교환 법칙 성립) 연산임 -> 특정 sorted 케이스로 사용해도 괜찮음. [ 애초에 '뽑는다'고만 하기도 함 ~ combi]
#   + combination 중에서도 반복(반복 시 메모리 초과) 없는 걸로 연산 간소화 가능한 이유
#     +걍 문제의 저 설명이 반복 없는 걸로 고정된 건가 #X_같은 것끼리 xor 하면 무조건 0임. 다른 것끼리 xor하면 각 개인보다 증가할 수도 감소할 수도 있지만, 0이상임. 음 근데 새 xor대상이 0이랑 해야 높은 값 가지는 놈일 수도 있는데 말이다.

# - [[itertools <-> Backtracking로 구현]]
#   > 문풀 시 : M1라이브러리, M2 Backtracking로 각각 두 방법으로 다 구현하기는 굳이. 
#
# - 문제에 따라 방법 선정
#   + (i) 각 세트들이 '어차피' 있는 전체 세트를 '생성'해야하는 경우
#     + O( r*nCr) [라이브러리], X_Backtracking 구현.
#     + 대부분 괜찮을듯
#   + (ii) 전체 세트를 생성하지 않고, 각 세트들에서 '각 r 개의 요소 저장'안하고 바로 연산O(1)하면 되는 경우
#     + 생성 파트 대신, O(nCr +을 더하는 게 [Backtracking 구현]하는 게, '최종 시간복잡도'에서 의의가 있는가?
    #   + (ii)-(i).1[라이브러리] 더해지는 생성파트 항(+nCr *r) 정도는 괜찮으면 -> 라이브러리 사용_코딩속도 개이득
    #   + (ii)-(i).2[라이브러리]  for문에서 생성된 combinations의 길이인 nCr을 돌 때, r보다 큰 n 등을 곱하면, 시간 복잡도에서 더해지는 생성항 r*nCr은 날려짐

    #   + (ii)-(ii) /r 의의있으면 : Backtracking로 구현. *n이나 r안하는 이렇게 간단한 문제 나올 확률이 적을 듯 최종이 O(nCr)인 거니까 말이다. 기본 골격 Backtracking구현만 하는 문제의 경우

# - ((itertools)) 확통_중복 ㅠ : "product"
#   + [ㅠ]product(자리구별/반복뽑[중복] 가능[repeat]) [[곱하기]] / [P]permutations(자리구별o/반복x)
#   + combinations_with_replacement() ( 자리구별x / "반복o")
#   + combinations( 변수_iterable/2차원 리스트도 ㄱㄴ/.. , r ) # 한 껍질 벗긴 것에서 r개 뽑아줌

#   + m1) product(list1, repeat=3)_list1의 요소[행이 될 수도 있음] 를 통째로repeat개 고름
#   + m2) product(  *  {2d_list} )_2d_list의 각 행에서 1개씩 고름 ## (모든 곳에서 두 껍질 들어가는 대신 그 안에선 1개씩만 가져옴 )_반환하는 각 튜플의 요소 수 = 2d_list의 행의 수
import sys

n, m = map(int, sys.stdin.readline().split())
amap = list(map(int, sys.stdin.readline().split()))

if m == 1 and n == 1:
    print(amap[0])
    exit()
elif m == 1:
    print(max(amap))
    exit()
aset = []
amax = [0]


# - n개에서 k개 뽑기 : 언제나 +1로 풀 수 있기 위해서 인덱스 사용 #이전처럼 연속적인 수 아님= 그렇게 그 부분에 +1할 수 없음 _ "인덱스"이용 시 연속적임

def search(recent_index, cnt):
    # - 1재귀 탈출
    # - 문제 설명 -> 알고리즘 논리는 맞아도, 직접 테스트 케이스 넣었을 때 정답으로 나온 출력을 보고 '나와야 하는 결과'가 다른 거 알았으면, 적어놓고 그 부분 코드 추가 변경해야함.
    #   > 이론적으로 print( 4 xor) 안됨. 1개 짜리 xor하는 거 문제에서 얘기도 없었으나 정답은 4값으로 출력나와야 함

    # 근데 위 경우로 때문에 후수정한 코드로 인해서, 아래 부분 이제 없어도 될 수도 있음
    if cnt == m:  # 가능한 대상이 '1개면' 바로  cnt==m이라 '뒷부분 코드인 ^ 연산 시도도 안됨'
        amax[0] = max(amax[0], aset[-1][1])
        # - M _ X 여기서 for_xor연산_비효율.
       
        # -> aset에 대상 추가 대신 연산결과를 저장해나가야겠다.
        #   + -> BUT, append는 ^= 한다쳐도, 'pop이 귀찮'으니까(이전 요소만큼만 ^=취소해야함)
        
        # -> (최종) 저장해나갈 때 병렬 요소 추가. aset에서 이전 요소(대상들)와 값을 이용해나갈 수 있음
        
        # -> 코드 구현 속도 빠른 방법_& 시간 복잡도가 영향 없는(뇌로 암산) 정도 : 새저장소 1개에 여기 aset을 append 후, 반복문 아예 밖에서 새저장소로 연산
        #   -> But, [append('리스트')해버리면 주소참조라, '변경되는 리스트면 같이 변경돼서' 귀찮아짐
        #   -> + 대신 리스트는 주소 참조하는 그런 방향으로 '전역화' 잘됐던 거일 수도 & append 때 내부 요소 여러 개 여도 O(1)
        #   -> + 다른 변수에 대한 순서, 추가, 전역화
        #   ->   + tuple 순서 있음 | + a=(3,) == a=tuple([3]_iterable) | 불변형이긴 한데 append도 됨(그러나 시간복잡도는 ..) a=([3,3],) -> a += ([4,4],) | BUT 지역변수임,  str 동일 ]
        return

        # - 코드에서 특정 부분 바꿨을 때 -> !!! 코드의 모든 흐름에서의 요소 체크
    for j in range(recent_index + 1, len(amap)):  # - => 다음 요소부터 : recent_index'+1'
        # for j in range(recent_index, len(amap)) :#  - 반복있는 combi : recent_index

        aset.append([j, aset[cnt - 1][1] ^ amap[j]])  # - j-1아니고 'cnt-1' : 'aset의 이전 요소'는 'cnt[aset 요소 개수 관련]_-1'임. 이전 j값은 aset에 들어가있지도 않았을 수 있음.
        search(j, cnt + 1)
        aset.pop()


for i in range(len(amap)):  # - 반복 없는 comb이면 -m개 이용해서 for문(시작 요소에 대한 for문) 범위 마지막 부분 좀 줄이는 것도 가능하긴 하겠지만 굳이 안함.
    aset.append([i, amap[i]])  # - => amap[i] : 첫 번째 요소를 넣었을 때의 결과 값으로, 0과 xor한 자기 자신의 값을 넣음 = 원랜 혼자서는 xor 못하는 거긴 함. 그렇지만, 코드 상에서 혼자인 케이스 따로 조건 식 만들어서 처리해주기도 했고, 정답이라는 출력이 혼자서라도 0과 xor하는 것임
    # - 첫 번째 요소가 들어오기 전엔 함께 xor될 대상이 초기값0이긴 하지만((동일한 식에서 xor하기 위한 상대대상 초기값)), 그 연산결과값을 '1개 받는 것부터 시작'하여서 0을 초기값으로 안씀. #1개여도 그 xor 결과를 넣는 코드 위치임. 0이미 지났고 해당 값.
    search(i, 1)
    aset.pop()

print(amax[0])
# 4)  m,n = 1,1_(  print( 1 xor )하면 에러이긴 한데, 정답이라는 결과 보니 0과 한다고 치나보다. ))_0보단?
# - 1,5 _ '테스트셋 제대로 만들어'서 안돌리고 1시간제출함
# - m=n


# - 1h 29m
# - O(nCr)_Backtracking로 *r부분 효율화된 문제. 전체 comb 세트 생성 및 '각 r 개의 요소 저장' 아니고, 해당 위치에서 연산이라서임


# - 코드 전에도 좀 필기함

# - 입력값을 '오름차순'으로 안줬더라도 상관없음. 어차피 순서 무관인 연산결과값이기 때문임. (, 어차피 인덱스로 +1하는 코드)
# - xor : ^


# - 1,2차 복습 시 : 1. 문제 읽고 풀이법 떠올리기 2. - 주석 읽기
# - 피드백에서 번역체라는 말을 들었는데 오늘 복습하면서 읽어보니까 진짜 더 와닿네. 유독 그게 부각돼서 보인 걸 수도 있긴 한데 아무튼 그런 부분도 있는 것 같음 >> (찐이면 분석 잘하시네..나도 전혀 몰랐다 내가 번역체 부분 있는지 ㅎㅋㅋㅋ) across, have pp, (수식 등) 이런 게 뇌에 먼저 스치고 한국어로 쓰게 되는 경우, 한국어로 바로 떠올랐긴 해도 have pp같은 말투 등.
#   + 한국어 구조 쓸 때도 영어에서 추출할 부분은, 수식이 길어지면 명사 말하고 후치수식
# - => 쓰기&읽기 시간 효율을 위해서, 나만 알아보면 되는 정도로 필기했는데, 시간 많이 흐르면 나도 꽤 잊음. 주어 생략 덜 해야겠다.
#

# - 복습 및 수정 시 : 파이참2021 에서 하고 옮기는 게 가시성 나은듯. 풀 땐 에디터가 힌트줘서 안됨