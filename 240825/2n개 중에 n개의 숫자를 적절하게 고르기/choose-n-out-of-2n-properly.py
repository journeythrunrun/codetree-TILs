# 1) 2n개의 숫자 -> n개씩 2개의 그룹으로 분리 -> '각 그룹 원소합'의 차_ 최소값

# 2) - ~ O(N^4), N=2n=20 
# n개 뽑 : 두 가지로 나누는 거라, 각 값을 선정했으면 

# 시간복잡도 허가범위 빠른 풀이 : 'n'_range생성?*'n'*nCr['n'* r[2]] *'n'[for] *'n'[in]# N,n 대략화 ## n이 10 이라 (2도있긴한데 대충 저만큼이다) 'n^2'도 100이라 O(N^4)
# + 오히려 생각보다 더 복잡해지기도 하는 것 같은 기분



import sys
inpu=sys.stdin.readline
n=int(inpu())
amap=list( map(int, inpu().split()) )#[] 


from itertools import combinations
# for aset in combinations(amap, n): # 인덱스로
min_answer='initial'
for aset_index in combinations( range(2*n) , n):# - range도 iterable # 인덱스로 amap~ len(amap화) # - aset은 aset_index
    sums=[0,0]

    # - ! 2n안되고 2*n
    #print(aset_index) #(0, 1)
    # - 이중 놉 # for i in aset_index : 
    for j in range(2*n):
        if j in aset_index : # set화는 굳이?
            sums[0]+=amap[j]
        else :
            sums[1]+=amap[j]
    
    temp_answer=abs(sums[0]-sums[1] )
    if min_answer=='initial':
        min_answer=temp_answer
    else :
        min_answer=min(temp_answer,min_answer)
print(min_answer)
            




# - 저번꺼 DP. 굳이?