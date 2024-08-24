# 1)
# 1<= <=N 숫자 중 => M개의 숫자를 골라 만들 수 있는 모든 조합

# 2) combinations _m1
# - 예시 => '중복' 없음
# 2) m2_DP=해설

# - 케이스 부분 앞으로 이동

# import sys
# from itertools import combinations
# inpu=sys.stdin.readline
# n,m= map(int, inpu().split())

# for a in combinations( range(1,n+1) ,m ): # m개씩
#     # print()
#     for i,one in enumerate(a): # m개
#         if i== len(a)-1:           
#         # if one == a[-1]: # 튜플 인덱싱
#             print(one)

#         else :
#             print(one, end=' ')

# 4) m,n=1,2이상-> 개수 아니라 아무것도 출력 안해야함 | 1,1 | m=n

# - 12m (라이브러리 사용) | (DP)

# - 해설 풀이
n,m=map(int, input().split())
combination=[]

def print_combination():
    print(' '.join(map(str, combination))) # - 숫자를 원하는 형식으로 출력하기 위해서 -> map으로 str화 & join

# 지금까지 뽑은 개수와 '마지막으로(가장 높은값 말고 뽑힌 시각의 흐름에서)' 뽑힌 숫자를 추적하여 그 다음에 뽑힐 수 있는 원소의 후보를 정함
def find_combination(cnt, last_num): # 처음엔 first_num이긴 함
    if cnt==m: # m개 다뽑았으면 탈출
        print_combination()
        return 

    for i in range(last_num+1, n+1): # 이미 뽑힌 거의 다음 번째 숫자 ~ 최대값 n 
        combination.append(i) # 뽑
        find_combination(cnt+1, i) # - 재귀함수_그 경우에 가능한 세트들
        combination.pop() # 한 요소를 pop 해야, 반복 안하고 차근차근 하나씩만 덜 쓰면서 해나갈 수 있음 (1,2,  3)에서 (1,2,  4) 만들 때 처음부터 안해도됨 

for i in range(1, n+1): # 값 대상 한번 훑으면서 저장
    combination.append(i) # i가 첫 번째 숫자인 경우
    find_combination(1,i) # 그 경우에서 가능한 세트들, 이미 i 1개는 뽑음
    combination.pop()