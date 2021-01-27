#투포인터 알고리즘은 리스트에 순차즉어로 접근해야 할 때 두개의 점의 위치를 기록하며 처리하는 알고리즘
#ex)2~7번까지의 학생 

#특정한 합을 가지는 부분 연속 수열 찾기 문제
'''
N개의 자연수로 구성된 수열에서 합이 M인 부분 연속 수열의 개수 구하기 (수행시간 제한 O(N))
완전탐색을 이용할 경우 N*2만큼의 수행시간이 소요
'''

'''
아이디어
1. 시작점과(start) 끝점이(end) 첫 번째 원소의 인덱스(0)을 가리키도록 한다
2. 현재 부분 합이 M과 같다면 카운트한다
3. 현재 부분합이 M보다 작다면 end를 1증가 시킨다(부분 합 증가)
4. 현재 부분합이 M보다 크거나 같다면, start를 1 증가시킨다 (부분 합 감소)
5. 모든 경우를 확인할 때 까지 2번부터 4번까지의 과정을 반복한다
'''

n=5 #데이터의 개수 N
m=5 #찾고자 하는 부분의 합 M
data = [1,2,3,2,5] #전체 수열

count = 0
interval_sum = 0
end = 0

for start in range(n): #start를 차례대로 증가시키며 반복
    while interval_sum < m and end <n: #end를 가능한 만큼 이동 
        interval_sum += data[end]
        end +=1
    if interval_sum == m: #부분합이 m일 때 카운트 증가
        count +=1
    interval_sum -= data[start]

print(count) 