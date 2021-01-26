#basic
#소수 판별 함수 (2이상의 자연수에 대해)

def is_prime_number(x):
    for i in range(2,x): #2부터 (x-1)까지 모든 수를 확인하며 x가 해당 수로 나누어 떨어지면 소수가 아님
        if x%i == 0:
            return False
    return True

print(is_prime_number(7))