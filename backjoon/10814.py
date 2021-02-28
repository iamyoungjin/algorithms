num_user = int(input())
lst_user = []

for _ in range(num_user):
    age_user, name_user = map(str,input().split(' '))
    age_user = int(age_user)
    lst_user.append((age_user,num_user))