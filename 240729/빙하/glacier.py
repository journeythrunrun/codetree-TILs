# 빙하1 
# 1초당 빙하 물에 닿아있는 부분 녹음 but 빙하로 둘러싸여있는 물은 빙하못녹임

# 빙하가 전부 녹는데 걸리는 시간, 마지막으로 녹은 빙하의 크기(1의 개수)
# 2) while(len(left)!=0) for n  
#    1이 미방문 0 만났을 때 : 인접0다가가기로 벽만날수있으면->자신인1의 0화 # 잘못썼넹
# 둘러쌓임 : 
 
#(4) 엣지케이스 = 예제

# M2-> M1 # 가장 바깥 0부터 한층의 1을 0으로 하는 게 빨랐을 수


import sys
inpu=sys.stdin.readline

n,m=map(int, inpu().split())
amap=[ list(map(int, inpu().split())) for _ in range(n)]
# M1 - [1]~[n-2], [1]~[m-2] 범위에서, 위는 아래(반대방향)로1찾,.. 
# 단순직진 알고리즘으로 했을때 완벽하려나
## du, dd, dl, dr= [1,0],[-1,0], [0,1],[0,-1]
dudlr=[ [[1,0],[-1,0]], [[0,1],[0,-1]] ]

# print(dudd)
# print(dldr)
cnt=0
#for _ in range(1,n-1)
target_udlr=[ [ [ [k,i]  for i in range(1,m-1) ] for k in [0,n-1] ] ,  [ [ [i,k]  for i in range(1,n-1) ] for k in [0,m-1] ]]
#target_lr= [ [ [i,k]  for i in range(1,n-1) ] for k in [0,m-1] ]

## 디버깅 : 이전맵에서 동일하게 가야해. 중복1발견 주의
ones=0
for i in range(n):
    for j in range(m):
        if amap[i][j]==1:
            ones+=1

while(1):
    #~ 탈출조건 맞춰서 cnt위치
    change=[]# 중복되도 ㄱㅊ
    cnt+=1
    # print('thththththth')
    melt=0
    check=1
    for j in [0,1] : # udlr
        for k in [0,1]: # updown
            for i, u in enumerate( target_udlr[j][k]) :
                #i_ud=0
                two_bre=False
                #print(target_udlr[j][k][i][0])
                # 코드 합치다가 에러나네 # 아까꺼 주석해놓을걸 - ui넓은 거 --> 오류나면 주석처리고 뭐고 통쨰로 출력안보여서 합쳤을 때 디버깅 더 어렵
                while(amap[target_udlr[j][k][i][0]][target_udlr[j][k][i][1]]!=1): #u였# 1 안나오면: but 반넘어가면 무한탈출
                    #print('while',u)
                    nm=n if j==0 else m
                    # i_ud로 단순카운팅으로 하기엔, 중간부터시작하기도 하지. -> u,d,l,r인경우 조건 다른거 귀찮 -> 인덱스범위로
                    # if i_ud >= (nm+1)//2 -1 : # -1 : 번째의 인덱스화 # 이때도 0인거면 그만

                    new=[target_udlr[j][k][i][0]+dudlr[j][k][0],target_udlr[j][k][i][1]+dudlr[j][k][1]]# 막판업뎃1인놈orbreak대상들
                    if 0<=new[0]<n and 0<= new[1]<m: # 반배 더가는정도야뭐
                        target_udlr[j][k][i]=new

                    else :
                        #check[k]=1# 한놈만 1이 없어서 쭉갈수도 있으니 이걸로 최종완료체크안됨
                        # check전부 넘어가야함.                    
                        two_bre=True
                        # print('break')
                        break

                    #target_udlr[j][k][i]=[u[0]+dudlr[j][k][0],u[1]+dudlr[j][k][1]]# 막판업뎃1인놈orbreak대상들
                    # print(target_udlr[j][k][i])
                    #i_ud+=1
                if two_bre==True:
                    continue
                check*=0 # check가 0이 아니어야 탈출
                # print('haha',[target_udlr[j][k][i][0]],[target_udlr[j][k][i][1]])
                change.append([ target_udlr[j][k][i][0], target_udlr[j][k][i][1]])
                #amap[target_udlr[j][k][i][0]][target_udlr[j][k][i][1]]=0
    for a in change :
        if amap[a[0]][a[1]]==1:
            amap[a[0]][a[1]]=0
            melt+=1
            ones-=1
                
    # ## for k in [0,1]: #leftright
    #     for i, u in enumerate( target_lr[k]) : #~ for이 왜
    #         i_ud=0
    #         two_bre=False
    #         while(amap[u[0]][u[1]]!=1): # 1인 위치로 while탈출
    #             print('while',u)
    #             if i_ud >= (m+1)//2 -1 : # -1 : 번째의 인덱스화 # 이때도 0인거면 그만
    #                 # check[k+2]=1
    #                 two_bre=True
    #                 break
    #             target_lr[k][i]=[u[0]+dldr[k][0],u[1]+dldr[k][1]]
    #             print('--',target_lr[k][i])
    #             i_ud+=1
    #         if two_bre==True:
    #             continue
    #         check*=0 # check가 0이 아니어야 탈출
    #         melt+=1
    #         amap[u[0]][u[1]]=0
    # print(cnt, melt)

    # print(check)
    if ones==0 :
        break
    # if check!=0:
    #     break

print(cnt, melt)

# M2 시간 복잡도 초과
# ones=[]
# for i in range(n):
#     for j in range(m):
#         if amap[i][j]==1:
#             ones.append([i,j])
# visited=[[False]*m for _ in range(n)]
# di=[0,0,-1,1]
# dj=[1,-1,0,0]
# from collections import deque



# def bfs2(v):#인접0다가가기로 벽만날수있으면->1화  

#     visited2=[[False]*m for _ in range(n)]
#     visited2[v[0]][v[1]]=True
#     aque2=deque([v]) #~ 이름v

#     while(aque2):
#         v2=aque2.popleft()
#         # 출력
        
#         for i in range(4):
#             ni,nj=v2[0]+di[i],v2[1]+dj[i]#v2[0]+di[0],v2[1]+dj[1]
#             if 0<=ni<n and 0<=nj<m and visited2[ni][nj]==False and amap[ni][nj]==0:
#                 aque2.append([ni,nj])  # aque2 # 2헷갈리니 아예이름이 다른게 낫
#                 visited2[ni][nj]=True #visited2
                
#                 if ni==1 or nj==1 or ni==n-2 or nj==m-2:
#                     return True
#     return False


# def bfs(v):
#     visited[v[0]][v[1]]=True
#     aque=deque([v])
#     # print(v)
#     while(aque):
#         w=aque.popleft()
#         # 출
        
#         for i in range(4):
#             ni,nj=w[0]+di[i],w[1]+dj[i] # i대신 0,1실화냐
#             if 0<=ni<n and 0<=nj<m and visited[ni][nj]==False and amap[ni][nj]==0:
#                 if bfs2([ni,nj])==True:#인접0다가가기로 벽만날수있으면->1의 0화     
#                     # 한번에 바껴야함 amap[v[0]][v[1]]=0
#                     return True# 걍 자신이 변하는지 하나씩 볼거라. 어라 복잡하게 풀었네 걍 네곳 보면 되는데.(아마 초반에 1<->0변함관계잘못봐서)
#                 # 1 한개씩 넣을거라 while로 여러 1 볼필요 없음
#                 #aque.append([ni,nj])
#                 #visited[ni][nj]=True
#     return False


# numb=0
# cnt=0
# while(ones):# 다음초
#     visited=[[False]*m for _ in range(n)]
#     cnt+=1

#     #left=alln-numb
#     left=len(ones)
#     # 아 'pop'하면 인덱스 밀리네 | ones 길이로 while문 종료 판단
#     # 멍
#     # len(ones)-1
#     # print('second')
#     # ones.pop빼는 알고리즘으로 바꾸기 전에 모든 ones 사용 위치 찾아봤어야지. 
#     post=0
#     change=[]
#     for i in range(len(ones)): # 하나씩보다 bfs로 한번에가 낫나.   # pop되면 어케되려나 이미첨에 계산했으니?     
#         # 전체 검사
#         i+=post
#         if bfs(ones[i])==True: # True면 pop, 바뀔놈
#             #numb+=1
#             #print(numb)
#             change.append(ones[i])

#             ones.pop(i)
#             post-=1
#     for v in change :
#         amap[v[0]][v[1]]=0

# print(cnt,left )#~


# - 시간많이듬+
#   + 딴 생각 쫌 함
#   > 16분 디버깅 오타
#   + 딴 생각 들거나 멍 때려지면 : 노래 크게 듣기?

#