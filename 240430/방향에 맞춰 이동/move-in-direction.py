# M2 - 속도비교
import sys
n= int(sys.stdin.readline())
x,y=0,0

dict1={'N':[0,1], 'S':[0,-1],'E':[1,0], 'W':[-1,0]}
for _ in range(n) :
    data = sys.stdin.readline().split()
    x,y=x+dict1[data[0]][0]*int(data[1]),y+dict1[data[0]][1]*int(data[1])
print(x,y)


# M1
# n= int(input())
# # data=[ list(input().split()) for _ in range(n)] # 'N','3'

# x,y=0,0
# dict1={'N':[0,1], 'S':[0,-1],'E':[1,0], 'W':[-1,0]}
# for _ in range(n) :
#     data = list(input().split())
#     # 속도비교
#     x,y=x+dict1[data[0]][0]*int(data[1]),y+dict1[data[0]][1]*int(data[1])
#     # print(data, x,y)
# print(x,y)