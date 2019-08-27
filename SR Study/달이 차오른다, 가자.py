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
    for key in keys:
        visit[y][x][key] = True


q = deque()
q.append((sx, sy, set([0])))  # 좌표와, 열쇠정보. 0은 아무키도 없을때..
# visit[sy][sx][0] = True
dist = 0
while q:
    for _ in range(len(q)):
        cx, cy, keys = q.popleft()
        print(f'현재 큐: {cx}, {cy}, {keys}')
        # 네방향 탐색..
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            # 범위내에 있음..
            if nx >= 0 and ny >= 0 and nx < M and ny < N:
                # 갖고있는 모든 키에 대해서 하나라도 갖고 방문하지 않은 칸이라면.. 들어가본다.
                if any(visit[ny][nx][k] == False for k in keys):
                    # 탈출..
                    if maze[ny][nx] == '1':
                        print(dist + 1)
                        exit()
                    #
                    # 열쇠찾음.
                    elif maze[ny][nx] in 'abcdef':
                        new_keys = keys.copy()
                        new_keys.add(key[maze[ny][nx]])
                        check(nx, ny, new_keys)
                        q.append((nx, ny, new_keys))
                    # 벽.. 얘는 절대 못감.
                    elif maze[ny][nx] == '#':
                        visit[ny][nx] = [False] * 7
                    # 문. 키가 있어야 함.
                    elif maze[ny][nx] in 'ABCDEF':
                        # 키가 있으면
                        if key[maze[ny][nx].lower()] in keys:
                            check(nx, ny, keys)
                            q.append((nx, ny, keys.copy()))
                    # 빈칸.!
                    else:
                        check(nx, ny, keys)
                        q.append((nx, ny, keys.copy()))

    dist += 1
print(-1)
#
# 1 15
# abcdef0.ABCDEF1