import math
#시간복잡도 : O(N*1/2)
#소수 판별 함수(2 이상의 자연수에 대하여) 약수의 원리 활용
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1): #2부터 x의 제곱근까지의 모든 수를 확인하여 x가 해당수로 나누어 떨어지면 소수가 아님
        if x % i ==0:
            return False
    return True

print(is_prime_number(4))