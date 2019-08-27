import sys
input = sys.stdin.readline
from collections import deque

# input, 보드생성, 구슬, 구멍 좌표 저장.
N, M = map(int, input().split())
board = []
for y in range(N):
    row = list(input().rstrip())
    for x in range(M):
        if row[x] == 'R':
            red = x, y
            row[x] = '.'
        elif row[x] == 'B':
            blue = x, y
            row[x] = '.'
        elif row[x] == 'O':
            row[x] = '.'
            hole = x, y
    board.append(row)

###################### move함수만 구현 ######################
# red좌표, blue좌표, 이동방향을 받아서 새로운 좌표 반환.. 구멍에 빠진다면 None을 반환..
def move(red, blue, d):
    rx, ry = red     # red 좌표
    bx, by = blue    # blue 좌표
    n_r = rx, ry
    n_b = bx, by
    if d == 'L':
        # 각 y값들에 대해서.. 두 개 거나 하나...
        for y in set((ry,by)):
            blank1 = blank2 = None
            for x in range(M):
                if board[y][x] == '.':
                    if not blank1:
                        blank1 = x
                    elif not blank2:
                        blank2 = x
                elif board[y][x] == '#' and blank1:
                    blank1 = blank2 = None
                # 현재 빨간색위치...
                elif (x, y) == (rx, ry):
                    # 이동시킬 수 있으면..
                    if blank1:
                        # 가는 도중 구멍이 있으면..
                        if y == hole[1] and blank1 <= hole[0] <= x:
                            n_r = None
                            blank2 = blank1

                        # 아니면 이동시켜주기.
                        else:
                            rx = blank1
                            n_r =  rx, ry
                            blank1 = None
                    elif blank2:
                        if y == hole[1] and blank2 <= hole[0] <= x:
                            n_r = None
                        else:
                            rx = blank2
                            n_r =  rx, ry
                # 파란구슬이라면..
                elif (x, y) == (bx, by):
                    if blank1:
                        # 가는 도중 구멍이 있으면..
                        if y == hole[1] and blank1 <= hole[0] <= x:
                            n_b = None
                            blank2 = blank1
                        # 아니면 이동시켜주기.
                        else:
                            bx = blank1
                            n_b = bx, by
                            blank1 = None
                    elif blank2:
                        if y == hole[1] and blank2 <= hole[0] <= x:
                            n_b = None
                        # 아니면 이동시켜주기.
                        else:
                            bx = blank2
                            n_b = bx, by

    elif d == 'R':
        for y in set((ry, by)):
            blank1 = blank2 = None
            for x in range(M-1,-1,-1):
                if board[y][x] == '.':
                    if not blank1:
                        blank1 = x
                    elif not blank2:
                        blank2 = x
                elif board[y][x] == '#' and blank1:
                    blank1 = blank2 = None
                elif (x, y) == (rx, ry):
                    # 이동시킬 수 있으면..
                    if blank1:
                        # 가는 도중 구멍이 있으면.. 빠짐..
                        if y == hole[1] and blank1 >= hole[0] >= x:
                            n_r = None
                            blank2 = blank1
                        # 아니면 이동시켜주기.
                        else:
                            rx = blank1
                            n_r = rx, ry
                            blank1 = None
                    elif blank2:
                        if y == hole[1] and blank2 >= hole[0] >= x:
                            n_r = None
                        else:
                            rx = blank2
                            n_r =  rx, ry
                elif (x, y) == (bx, by):
                    if blank1:
                        # 가는 도중 구멍이 있으면..
                        if y == hole[1] and blank1 >= hole[0] >= x:
                            n_b = None
                            blank2 = blank1
                        # 아니면 이동시켜주기.
                        else:
                            bx = blank1
                            n_b = bx, by
                            blank1 = None
                    elif blank2:
                        if y == hole[1] and blank2 >= hole[0] >= x:
                            n_b = None
                        else:
                            bx = blank2
                            n_b =  bx, by

    elif d == 'U':
        # 각 x값들에 대해서.. 두 개 거나 하나...
        for x in set((rx, bx)):
            blank1 = blank2 = None
            for y in range(N):
                if board[y][x] == '.':
                    if not blank1:
                        blank1 = x
                    elif not blank2:
                        blank2 = x
                elif board[y][x] == '#' and blank1:
                    blank1 = blank2 = None
                elif (x, y) == (rx, ry):
                    # 이동시킬 수 있으면..
                    if blank1:
                        # 가는 도중 구멍이 있으면..
                        if x == hole[0] and blank1 <= hole[1] <= y:
                            n_r = None
                        # 아니면 이동시켜주기.
                        else:
                            ry = blank1
                            n_r = rx, ry
                    # 아니면 벽에 붙어있는것.. 그대로..
                elif (x, y) == (bx, by):
                    if blank1:
                        # 가는 도중 구멍이 있으면..
                        if x == hole[0] and blank1 <= hole[1] <= y:
                            n_b = None
                        # 아니면 이동시켜주기.
                        else:
                            by = blank1
                            n_b = bx, by
    else:
        for x in set((rx, bx)):
            blank1 = blank2 = None
            for y in range(N-1,-1,-1):
                if board[y][x] == '.':
                    if not blank1:
                        blank1 = x
                    elif not blank2:
                        blank2 = x
                elif board[y][x] == '#' and blank1:
                    blank1 = blank2 = None
                elif (x, y) == (rx, ry):
                    # 이동시킬 수 있으면..
                    if blank1:
                        # 가는 도중 구멍이 있으면..
                        if x == hole[0] and blank1 >= hole[1] >= x:
                            n_r = None
                        # 아니면 이동시켜주기.
                        else:
                            ry = blank1
                            n_r = rx, ry
                    # 아니면 벽에 붙어있는것.. 그대로..

                elif (x, y) == (bx, by):
                    if blank1:
                        # 가는 도중 구멍이 있으면..
                        if y == hole[0] and blank1 >= hole[1] >= x:
                            n_b = None
                        # 아니면 이동시켜주기.
                        else:
                            by = blank1
                            n_b = bx, by

    return n_r, n_b

# 큐 만들어서 bfs 돌리기.
q = deque()
q.append((red, blue, 'U'))
q.append((red, blue, 'D'))
q.append((red, blue, 'L'))
q.append((red, blue, 'R'))
# 최대 10번까지만 시도.
for t in range(1, 11):
    print(f'queue: {q}')
    # 큐 전체에 대해 1번씩만 늘려가면서..q가 없어져도 ㄱㅊ
    for _ in range(len(q)):
        red, blue, path = q.popleft()
        print(f'red, blue, path = {red}, {blue}, {path}')
        d = path[-1]
        new_red, new_blue = move(red, blue, d)
        # 빨간색만 구멍에 빠진경우!  출력하고 종료!!
        print(f'new_red, new_blue = {new_red}, {new_blue}')
        if new_red is None and new_blue:
            print(t, path, sep="\n")
            exit()
        # 구슬들이 모두 남아있는 경우.. 새로 큐에 두 경우 추가..
        elif new_red and new_blue:
            # 방금 위나 아래로 이동했다면 다음엔 좌우 두 경우만 생각..
            if d in ('UD'):
                q.append((new_red, new_blue, path+'L'))
                q.append((new_red, new_blue, path+'R'))
            # 방금 왼쪽이나 오른쪽이었다면 다음에는 위아래만..
            else:
                q.append((new_red, new_blue, path+'U'))
                q.append((new_red, new_blue, path+'D'))
print(-1)


def move(red, blue, d):
    rx, ry = red     # red 좌표
    bx, by = blue    # blue 좌표
    n_r = n_b = None