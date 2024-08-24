# # 1. 
# # nxm, 1_빙하 0_물
# # 1_1초에 물에 닿아있는 부분들 동시에 녹음, 1빙하로 둘러쌓인 0물은 빙하를 못 녹임
# # -> 바깥 쪽의 0들이 안쪽의 1을 녹임
# # => 빙하가 전부 녹는데 걸리는 시간 t, 마지막으로 녹은 빙하의 크기(1의 수)
# # (while t+=1, len)
# # -> 바깥의 0 저장

# # - 해설 방법 
# # - # 한 물에서 bfs 시작-> 물이면 움직임대상 q에 추가, 빙하면 녹일 빙하에 추가-> 녹일 빙하를 다음 bfs 시작인q화
# # -> 네곳씩만 보면서, 내부로 bfs. 그 네 방면 쪽을 q에 넣고 bfs돌리기. 
# # -> q : 첨에 끝에서 시작해서 1아니게 만나는 애들 다
# # -> copy이유 : 녹은 걸 이제 다음 번 녹일 때 출발점으로 사용

# # - 생각보다 해설 이해하는 순수시간 적게 드네
# #   + 하다가 시간 꽤지나면 해설로 넘어가기
# #     >  첨엔 해설 길어서 해설 방법 이해가 더 꽤 걸릴 줄 쫄

# # - 담번에 이 방법으로 직접 풀어보기 ? 그건 새문제로 구현하면서 하는 게 낫나 

# from collections import deque
# import enum

# class Element(enum.Enum):
#     WATER = 0
#     GLACIER = 1
    
# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))

# a = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# # bfs에 필요한 변수들 입니다.
# q = deque()
# glaciers_to_melt = deque()
# visited = [
#     [False for _ in range(m)]
#     for _ in range(n)
# ]
# cnt = 0

# dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# # 소요 시간과 가장 마지막으로 녹은 빙하의 수를 저장합니다.
# elapsed_time = 0
# last_melt_cnt = 0

# # 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < m

# # 범위를 벗어나지 않으면서 물이여야 하고 방문한적이 
# # 없어야 갈 수 있습니다.
# def can_go(x, y):
#     return in_range(x, y) and a[x][y] == Element.WATER.value and not visited[x][y]


# # 범위를 벗어나지 않으면서 빙하여야 하고 이미 
# # 선택된 적이 없어야 중복 없이 녹아야할 빙하 목록에 
# # 해당 빙하를 문제 없이 추가할 수 있습니다.
# def is_glacier(x, y):
#     return in_range(x, y) and a[x][y] == Element.GLACIER.value and not visited[x][y]


# # 아직 방문해보지 못한 빙하에 둘러쌓여 있지 않은 물 영역을 더 탐색해주는 BFS입니다.
# def bfs():
#     while q:
#         # queue에서 가장 먼저 들어온 원소를 뺍니다.
#         x, y = q.popleft()
        
#         # queue에서 뺀 원소의 위치를 기준으로 네 방향을 확인합니다.
#         for dx, dy in zip(dxs, dys):
#             new_x, new_y = x + dx, y + dy

#             # 더 갈 수 있는 곳이라면 Queue에 추가합니다.
#             if can_go(new_x, new_y):
#                 q.append((new_x, new_y))
#                 visited[new_x][new_y] = True
#             # 만약 아직 방문하지 않은 빙하가 있는 곳이라면
#             elif is_glacier(new_x, new_y):
#                 # 빙하에 둘러쌓여 있지 않은 물에 인접한 빙하이므로 이번에 녹아야 할 빙하이므로 
#                 # 따로 저장해줍니다.
#                 # 중복되어 같은 빙하 정보가 기록되는 것을 막기위해
#                 # 이때에도 visited 값을 true로 설정해줍니다.
#                 glaciers_to_melt.append((new_x, new_y))
#                 visited[new_x][new_y] = True


# # 녹여야 할 빙하들을 녹여줍니다.
# def melt():
#     while glaciers_to_melt:
#         x, y = glaciers_to_melt.popleft()
#         a[x][y] = Element.WATER.value
        
        
# # 빙하를 한 번 녹입니다.
# def simulate():
#     global elapsed_time, last_melt_cnt, q

#     # 빙하에 둘러쌓여 있지 않은 물의 영역을 넓혀보며
#     # 더 녹일 수 있는 빙하가 있는지 봅니다. 
#     bfs()
    
#     # 더 녹일 수 있는 빙하가 없다면 시뮬레이션을 종료합니다.
#     if not glaciers_to_melt:
#         return False
    
#     # 더 녹일 빙하가 있다면 답을 갱신해주고
#     # 그 다음 시뮬레이션에서는 해당 빙하들의 위치를 시작으로
#     # 빙하에 둘러쌓여 있지 않은 물의 영역을 더 탐색할 수 있도록 queue에 
#     # 녹아야 할 빙하들의 위치를 넣어줍니다.
#     elapsed_time += 1
#     last_melt_cnt = len(glaciers_to_melt)

#     q = glaciers_to_melt.copy() ## copy이유 : 녹은 걸 이제 다음 번 녹일 때 출발점으로 사용

#     # 녹아야 할 빙하들을 녹여줍니다.
#     melt()
    
#     return True
    
    
# # 처음에는 (0, 0) 에서 시작하여 초기 빙하에 둘러쌓여 있지 않은 물들을 찾을 수 있도록 합니다.
# q.append((0, 0))
# visited[0][0] = True

# while True:
#     is_glacier_exist = simulate()
    
#     # 빙하에 둘러쌓여 있지 않은 물의 영역을 넓혀보며 더 녹일 수 있는 빙하가 있는지 봅니다.
#     if not is_glacier_exist:
#         break
        
# print(elapsed_time, last_melt_cnt)







from collections import deque
import enum


import sys
inpu=sys.stdin.readline

m,n=map(int,inpu().split())
amap=[list(map(int, inpu().split()  )  ) for _ in range(n) ]

visited=[[False]*m for _ in range(n) ]

class Element(enum.Enum):
    water=0
    glacier=1
def is_glacier(x,y):
    return True if 0<=x<n and 0<=y<m and amap[x][y]==Element.glacier.value and visited[x][y]==False else False

def can_go(x,y):
    return True if 0<=x<n and 0<=y<m and amap[x][y]==Element.water.value and visited[x][y]==False else False

# def is_g

q=deque()
t=0

dx, dy=[0,0,1,-1],[1,-1,0,0]
from copy import deepcopy
def bfs(v):
    visited[v[0]][v[1]]=True
    q.append(v)
    while(q):
        x,y=q.popleft() #~ popleft
        visited[x][y]=True
        # print('1111', x,y)

        for i in range(4):
            nx, ny= x+dx[i], y+dy[i]
            if is_glacier(nx,ny):
                glaciers.append( (nx,ny) )
                visited[nx][ny]=1
            elif can_go(nx,ny):
                # print(nx,ny)
                q.append( (nx,ny) )
                visited[nx][ny]=True

    return 

old_len=0
while(1):
    glaciers=deque() # 다음 시작 전 타겟 얼음 리셋

    

    bfs((0,0))
    
    # 처음부터 탈출케이스도 커버 가능하도록
    if len(glaciers)==0: 
        break
    t+=1    
    
    # 길이가 0이 아닐 때라 이전 길이
    old_len=len(glaciers) # 다이어그램알고리즘 및 코드 위치 먼저 할걸?

    q=glaciers.copy()

print(t,old_len)



# + 실수 : 조건문 ==, True오타 , append 때 괄호 ( (x ,y) )
# queue copy