n = int(input())

arr = [] 

for _ in range(n):
    x, y = map(int,input().split(' '))
    arr.append((x,y))
arr = sorted(arr)

for i in arr:
    print(i[0], i[1])