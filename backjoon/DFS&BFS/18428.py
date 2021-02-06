#https://www.acmicpc.net/problem/18428
#감시 피하기

'''
선생님이 존재하는 칸 : T / 장애물이 존재하는 칸 : O / 학생들이 존재하는 칸 : S / 
아무것도 존재하지 않는 칸 X
N x N 크기의 복도에 학 생 및 선생님 위치 정보가 주어졌을때 장애물을 정확히 3개 설치하여 
모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력
'''

#풀이 
#1. 장애물을 놓을 수 있는 공간을 리스트로 저장 
#2. combination을 활용하여 장애물을 놓을 수 있는 위치의 조합별로 확인
#3(2)를 기반으로 장애물 설치
#4 선생님에게 잡힌 학생이 없는지 확인
#5. 선생님 위치마다 동서남북 4방향으로 T를 채워넣는다(징애물이 없는 경우) DFS
#6. DFS가 끝나면 각 학생의 위치의 board가 T인지 S인지 확인하여 S가 아닌 경우
#   1명이라도 선생님에게 잡힌 경우이니 이 장애물 배치는 False이다
#7. 모든 장애불 배치에 대해 감시를 피하는 경우가 없다면 no 아니면 yes출력

from itertools import combinations
from sys import stdin

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(map(str, stdin.readline().split())) for _ in range()]

emptys = []
teacher = []
student = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 'X':
            emptys.append([i,j])
        elif board[i][j] == 'T':
            teacher.append([i,j])
        elif board[i][j] == 'S':
            student.append([i,j])


def DFS(board,x,y,idx):
    global n 
    if x<0 or x>=n or y<0 or y>=n or board[x][y] == '0':
        return 
    else:
        board[x][y] == 'T':
        DFS(board,x+dx[idx],y+dy[idx],idx)

def check():
    copy_board = deepcopy(board)
    for [x,y] in teacher:
        for i in range(4):
            DFS(copy_board,x,y,i)
    for [x,y] in student:
        if copy_board[x][y] != 'S'
        return False
    return True

for case in list(combinations(emptys,3)):
    for [x,y] in case:
        board[x][y] = '0'
    if check():
        print("Yes")
        exit()
    for [x,y] in case:
        board[x][y] = 'X'
print("No")