# 1) 동전 있 1 / 없 0
# 3*3 격자에서 동전의 개수 최대
import sys
n=int(sys.stdin.readline()) # - int() :  문자열의 앞뒤에 있는 공백을 무시[GPT]
amap=[ list(map(int, sys.stdin.readline().split() )) for _ in range(n) ] 

answer=0
for i in range(n-2):
    for j in range(n-2):# 해당위치에서부터 3x3
        count=0
        for kk in range (i,i+3):
            count+=sum([ amap[kk][j+k] for k in range(3) ] ) # 2차원인덱싱 : 다른 방법으로도 했었는데 굳이 찾진말자 ## 9개밖에 없으니까 그냥
        answer=max(answer, count)
print(answer)
# 10m : 입력받는 방식 sys로 전환
# 8m: 문제푸는 시간