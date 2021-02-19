#두 개 뽑아서 더하기
#https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

def solution(numbers):
    answer = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum in answer:
                pass
            else:
                answer.append(sum)
    answer.sort()
    return answer           

numbers=[2,1,3,4,1]