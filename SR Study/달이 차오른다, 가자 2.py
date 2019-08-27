from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
sx = sy = 0
for y in range(N):
    row = input().rstrip()
    for x in range(M):
        if row[x] == '0':
            sx, sy = x, y
    maze.append(row)

visit = [[[False] * 7 for _ in range(M)] for _ in range(N)]
dx = 0, 0, 1, -1
dy = 1, -1, 0, 0
key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


# 방문 체크해주는 함수.
def check(x, y, keys):
    # for key in keys:
    #     visit[y][x][key] = True
    for key in range(7):
        if 1<<key&keys:
            visit[y][x][key] = True

q = deque()
q.append((sx, sy, 1))  # 좌표와, 열쇠정보. 1은 아무키도 없을때.. 2^0
visit[sy][sx][0] = True
dist = 0
while q:
    print(f'dist = {dist+1}')
    for _ in range(len(q)):
        cx, cy, keys = q.popleft()
        have_keys = tuple(i for i in range(7) if (1<<i)&keys)
        print(f'현재 큐: {cx}, {cy}, {keys}')
        print(f'현재 갖고있는 키. {have_keys}')
        # 네방향 탐색..
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            # 범위내에 있음..
            if nx >= 0 and ny >= 0 and nx < M and ny < N:
                # 갖고있는 모든 키에 대해서 하나라도 갖고 방문하지 않은 칸이라면.. 들어가본다.
                # 이부분 비트마스크 이렇게 쓰면 되나..
                if any(visit[ny][nx][k] == False for k in range(7) if 1<<k&keys):
                    # 탈출..
                    if maze[ny][nx] == '1':
                        print(dist + 1)
                        exit()
                    # 열쇠찾음.
                    elif maze[ny][nx] in 'abcdef':
                        new_keys = keys | 1<<key[maze[ny][nx]]
                        check(nx, ny, new_keys)
                        q.append((nx, ny, new_keys))
                    # 벽.. 얘는 절대 못감.
                    elif maze[ny][nx] == '#':
                        visit[ny][nx] = [False] * 7
                    # 문. 키가 있어야 함.
                    elif maze[ny][nx] in 'ABCDEF':
                        # 키가 있으면
                        if 1<<key[maze[ny][nx].lower()] & keys:
                            print(f'{maze[ny][nx]} 통과')
                            check(nx, ny, keys)
                            q.append((nx, ny, keys))
                    # 빈칸.!
                    else:
                        check(nx, ny, keys)
                        q.append((nx, ny, keys))

    dist += 1
print(-1)

"""
10 5
#a##1
#B##A
.....
####.
.....
C####
.....
##.#.
...#.
c##b0

a:2, b:4, c:8, d:16, e:32, f: 64 
"""