import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
if N%2==0:  # 짝수일땐 전체가 폭탄.. 이것만 해줘도 속도 반..5960->2716ms
    ans = f"{'O'*C}\n" * R
    print(ans.rstrip())
    exit()

if N==1:    # N이 1일경우 초기폭탄.. 그대로 출력
    print('\n'.join([input().rstrip() for _ in range(R)]))
    exit()

# 그 외 경우..
board = []
for y in range(R):
    row = list(input().rstrip())
    for x in range(C):
        if row[x] == 'O':
            row[x] = '0'  ################ 숫자 0으로 저장! 심은 시간.
    board.append(row)


def printBoard():
    for y in range(R):
        for x in range(C):
            if board[y][x] != '.':
                board[y][x] = 'O'
    print('\n'.join(map(''.join, board)))

t = 2  # 2부터 시작.
for _ in range(2):  # 3, 4번 반복 실행..최대 2번 터진 이후 계속 반복..
    # 2초, 4초일때 폭탄심기.
    for y in range(R):
        for x in range(C):
            if board[y][x] == '.':
                board[y][x] = str(t)  # 심은 시간으로

    t += 1  # 3초, 5초에 터짐..얘네 둘이 이제 반복됨.
    for y in range(R):
        for x in range(C):
            if board[y][x] == '.':
                continue
            if int(board[y][x]) == t - 3:
                board[y][x] = '.'
                if x > 0 and board[y][x - 1] == str(t-1):  # 같이 터지는 애가 아니라면
                    board[y][x - 1] = '.'
                if x < C - 1 and board[y][x + 1] == str(t-1):
                    board[y][x + 1] = '.'
                if y > 0 and board[y - 1][x] == str(t-1):
                    board[y - 1][x] = '.'
                if y < R - 1 and board[y + 1][x] == str(t-1):
                    board[y + 1][x] = '.'
    # N = 4K-1의 꼴.. 3초인애와 같다. 얘 먼저 하면 됨.. 이 꼴이 아니라면 for문이 한번 더 돈다.
    if t == 3 and (N+1)%4==0:
        printBoard()
        exit()
    if t == 5:
        print('here')
        printBoard()
        exit()
    t += 1