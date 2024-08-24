# 1) n개_0 이상의 정수 -> m개 뽑아 모두 xor -> 최대값 

# 이미 있는 대상에서 'm개의 숫자' 뽑 중복 가능 -> combi
import sys
n, m = map(int, sys.stdin.readline().split())
amap = list(map(int, sys.stdin.readline().split()))

if m==1 and n==1:
    print(amap[0])
    exit()

aset=[]
amax=[0]

target=[]

# 이전처럼 연속적인 수 아님 _ 인덱스가 연속적임

def search (recent_index,cnt):
    # 재귀 탈출
    # print(cnt)
    if cnt==m :

        # print(target)
        target.append(aset)
        
        amax[0]=max(amax[0], aset[-1][1]) # X_ 여기서 xor_for 보단 대상을 넘기지말고 연산결과를 넘겨야겠다._ append는 ^=한다쳐도, -> pop이 귀찮으니까 병렬 저장 요소 추가 ->  그것도 귀찮으니 시간복잡도 보다 적은 저장소1개추가[append(순서있는리스트)해버리면 주소참조귀찮아짐 tuple+=(j,) or str. .]
        return 

    # 바꾸고 코드의 모든 흐름에서의 요소 체크
    for j in range(recent_index, len(amap)) :#  # - 2_연달아가능하게recent+1로  ~
    # for j in range(recent_index+1, len(amap)) :#  # - 2_연달아가능하게recent+1로  ~
        # print('111',j)
        aset.append([j,aset[cnt-1][1]^amap[j]]) # j-1 cnt-1
        # print(aset)
        search(j, cnt+1)
        aset.pop()

# m개 검사 굳이?
for i in range(len(amap)) : # 사실 -m개 이용해서 마지막 부분 좀 줄일 수 있긴함. 
    aset.append([i,0])
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
# 4)  m,n = 1,1_(print( 1 xor 0과 한다고 친다보다. ))_0보단? | 1,5


## 중복숫자도 뺄 수 있어야하려나


# - '오름 차순'으로 안주더라도 어차피 순서 무관인 연산결과값 쓰는 거라 상관없음

# - 자연수 0 여부 

# - xor ^