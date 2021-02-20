#블랙잭

n,m = list(map(int,input().split(' ')))
card =list(map(int(input().split(' '))))

res = 0
length = len(card)

for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum_val = card[i] + card[j] + card[k]
            if sum_val <= m:
                res = max(res, sum_val)
print(res)