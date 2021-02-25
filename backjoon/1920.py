# 속도를 위해 이진탐색 사용
n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int,input().split()))


for i in range(m):
    start = 0
    end = n-1
    target = i
    res = 0
    while (start <= end):
        mid = (start+end) //2
        if n_list[mid] == target:
            res = 1
            break
        elif target < n_list[mid]:
            end = mid-1
        else:
            start = mid+1
    print(res)