#모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1,score2,score3 =0,0,0
    
    for i in range(answers):
        if (answers[i] === person1[i % 5]):
            score1+=1
        if (answers[i] === person2[i % 8]):
            score2+=1
        if (answers[i] === person3[i % 10]):
            score3+=1