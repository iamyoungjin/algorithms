num = input()
num = [int(n) for n in num]

orderd_num = sorted(num, reverse=True)

for i in orderd_num:
    print(i, end='')