# Root node를 찾아주는 함수
def find(x):
    if x == parent[x]:
        return x
    else:
        parent_x = find(parent[x])
        parent[x] = parent_x
        return parent[x]

# y의 Root 노드가 x의 Root 노드와 같지 않으면 
# y의 Root 노드가 x의 Root 노드의 자식이 되도록 하는 함수
def union(x,y):
    x = find(x)
    y = find(y)

    if x!=y:
