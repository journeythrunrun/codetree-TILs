# 1) 동전 있 1 / 없 0
# 3*3 격자에서 동전의 개수 최대
import sys
n=int(sys.stdin.readline()) # \n split하면 없어지네#.split() # 엔터는 뭐임
# amap=[print(sys.stdin.readline().split() )for _ in range(3)]
amap=[ list(map(int, sys.stdin.readline().split() )) for _ in range(n) ] # int

answer=0
# print(amap)
for i in range(n-2):
    for j in range(n-2):# 해당위치에서부터 3x3
        count=0
        for kk in range (i,i+3):
            count+=sum([ amap[kk][j+k] for k in range(3) ] ) # 2차원인덱싱 # 9개밖에 없으니까 그냥

        answer=max(answer, count)
print(answer)
# 10m 입력 받는거 sys로 바꿔사용한 시간