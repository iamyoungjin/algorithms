import heapq

#내림차순 힙 정렬
def heapsort(iterable):
    h=[]
    result =[]
    for value in iterable: #모든 원소 차례대로 삽입
        heapq.heappush(h,-value) #+
    for i in range(len(h)): #힙에 삽입된 모든원소 차례대로 꺼내어 담기 
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,2,4,6])
print(result)