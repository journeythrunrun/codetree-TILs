# 1)
# 1<= <=N 숫자 중 => M개의 숫자를 골라 만들 수 있는 모든 조합

# 2) combinations _m1
# - 예시 => '중복' 없음
# 2) m2_DP=해설


import sys
from itertools import combinations
inpu=sys.stdin.readline
n,m= map(int, inpu().split())

for a in combinations( range(1,n+1) ,m ): #m개씩
    for i,one in enumerate(a): #m개
        if i== len(a)-1:  
        # - 튜플 : 인덱싱 가능             
        #if one == a[-1]: 
            print(one)
        else :
            print(one, end=' ')

# 4) m,n = 1,2이상-> 개수 아니라 아무것도 출력 안해야함 | 1,1 | m=n



# - 12m (라이브러리 사용) | (DP)
# - 그래도 특정 문제에 관해선, 라이브러리 보다 *r간소화 되는 경우(r개 요소 저장할 필요 없는 경우)도 있으니까 각 itertools을 DP로 구현할줄 알기


# # - 해설 풀이
# n,m=map(int, input().split())
# combination=[]

# def print_combination():
#     print(' '.join(map(str, combination))) # - m2_리스트 속 int를 원하는 형식으로 출력하기 위해서 -> map으로 str화 & join

# #지금까지 뽑은 개수와 '마지막으로(가장 높은값 말고 뽑힌 시각의 흐름에서)' 뽑힌 숫자를 추적하여 그 다음에 뽑힐 수 있는 원소의 후보를 정함
# def find_combination(cnt, last_num): # 처음엔 first_num이긴 함
#     if cnt==m: # m개 다뽑았으면 탈출
#         print_combination()
#         return 

#     for i in range(last_num+1, n+1): # - 이미 뽑힌 거의 다음 번째 숫자 ~ 최대값 n 
#         combination.append(i) # - 뽑
#         find_combination(cnt+1, i) # - 재귀함수_ 위에서 뽑은 경우에 가능한 경우들 (세트들)
#         combination.pop() # -  한 개 뺌. 다 사용한 경우의 수이기때문임. #한 요소를 pop 해야, 반복 안하고 차근차근 하나씩만 덜 쓰면서 해나갈 수 있음 (1,2,  3)에서 (1,2,  4) 만들 때 처음부터 안해도됨 

# for i in range(1, n+1): # - 가능한 값의 대상들을 쭉 한번 훑으면서, 경우들 리스트에 저장해나감
#     combination.append(i) # - i가 첫 번째 요소인 경우(로 고정)
#     find_combination(1,i) # - 위에서 뽑은 경우에 가능한 경우들 (세트들) #그 경우에서 가능한 세트들, 이미 i 1개는 뽑음
#     combination.pop()