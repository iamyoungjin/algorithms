
import sys
def find(x):
    if p[x]==x:
        return x
    else:
        y = find(p[x])
        p[x] = y#시간을 줄이는 요소
        return y
 
 
 
def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        p[y]=x#루트노드 합치기
        cnt[x]=cnt[y]+cnt[x]#루트노드 수합치기

test_case =int(input())
for _ in range(test_case):
    p = {}
    cnt = {}
    f=int(input())
    for _ in range(f):
        x,y= input().split()
        if x not in p:#f1이 딕셔너리에 없다면
            p[x]=x
            cnt[x]=1
        if y not in p:#f2이 딕셔너리에 없다면
            p[y]=y
            cnt[y]=1
 
        union(x,y)
        print(cnt[find(x)])
