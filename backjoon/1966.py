#프린터 큐

cases = int(input())

for _ in range(cases):
    n,m = list(map(int, input().split( )))
    q = list(map(int, input().split( )))
    idx = list(range(len(q)))
    idx[m] = 'target'

    # 순서  
    order = 0
    
    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if q[0]==max(q):
            order += 1
                        
            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0]=='target':
                print(order)
                break
            else:
                q.pop(0)
                idx.pop(0)
        else:
            q.append(q.pop(0))
            idx.append(idx.pop(0))  