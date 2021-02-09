#hanoi
'''

'''
n = int(input())

def hanoi(n,from_,middle,to_):
    if n == 1:
        print(from_,to_)
    else:
        hanoi(n-1,from_,to_,middle) #1->2
        print(from_,to_) # 1->3
        hanoi(n-1,middle,from_,to_) #2->3

sum =1
for i in range(n-1):
    sum = sum * 2+1

print(sum)
hanoi(n,1,2,3)