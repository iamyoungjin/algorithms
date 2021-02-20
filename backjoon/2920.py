#음계

a = list(map(int,input().split(' ')))

asc = True
des = True

for i in range(1,8):
    if a[i]>a[i-1]:
        des = False
    elif a[i]<a[i-1]:
        asc = False

if asc:
    print("ascending")
elif des:
    print("descending")
else:
    print("mixed")

'''
a = list(map(int,input().split(' ')))
asc = a
des = a
asc.sort()
des.reverse()
if a == asc:
    print("ascending")
elif a == des:
    print("descending")
else:
    print("mixed")
'''