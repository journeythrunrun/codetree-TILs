# 1) 2번에 걸쳐서 특정 구간 제거

import sys

n=int(sys.stdin.readline()) # int() : split() 필요없음
amap=[ int(sys.stdin.readline() ) for _ in range(n)]
target_th=[]
target_th.append(list(map(int,sys.stdin.readline().split())))  # split 다양한 종류의 공백을 없애며 split
target_th.append(list(map(int,sys.stdin.readline().split())))  ## '번째'
# 입력 -> 'int' // list(map(int,

for i in range(2): ## target_th[i] : [2,4] 
    # m1 : '줄여진 거에서 다시 'n번째'
    for j in range(  target_th[i][0]-1, target_th[i][1]-1 +1 ) : # 번째라서  ## 이 인덱스 뺀다. # range 오른쪽 끝 포함안되는
        amap.pop(target_th[i][0]-1) # pop, remove / PR
        # print('--',j) # pop하면 이미 인덱스가 땡겨져있어버림

    # m2 위 구간 아닌, 왼쪽 리스트 + 오른쪽 리스트
    # amap=amap[:target_th[i][0]-1  +1-1 ]+amap[target_th[i][1]-1 +1 : ] 
print(len(amap)) ## 남은 블록 수
print (*amap, sep='\n') # *변수 & 그 사이들 sep가능
# - 20m
# - prefix등 알아야 코딩 속도 가능한 알고리즘 : 기출 보며 유용한 것 먼저?