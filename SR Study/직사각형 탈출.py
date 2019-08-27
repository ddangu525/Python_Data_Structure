from collections import deque
import sys
input = sys.stdin.readline
dx = 0, 0, 1, -1
dy = 1, -1, 0, 0

N, M = map(int, input().split())
info = [input().rstrip().split() for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

# 안되는 경우 바로 -1.
if Fc>M-W+1 or Fr>N-H+1:
    print(-1)
    exit()

if any(info[y][x] == '1' for x in range(Fc-1, Fc-1+W) for y in range(Fr-1, Fr-1+H)):
    print(-1)
    exit()

if (Sr, Sc) == (Fr, Fc):
    print(0)
    exit()

visit = [[False] * M for _ in range(N)]
q = deque()
q.append((Sc-1, Sr-1))
visit[Sr-1][Sc-1] = True
moves = 1
while q:
    for _ in range(len(q)):
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            # 일단 범위 확인 + 방문확인
            if 0 <= nx <= M - W and 0 <= ny <= N - H and not visit[ny][nx]:
                if (nx, ny) == (Fc-1, Fr-1):
                    print(moves)
                    exit()
                # 범위내에 벽이 없다면. 항상 다 검사하지 말고 추가되는 점들 H, 혹은 W개만 새로 검사.
                # d 가 0 1 2 3 -> 아래 위 오른쪽 왼쪽
                # 새로 추가되는 밑면 W개만 검사.
                visit[ny][nx] = True
                # 1. 아래
                if d == 0:
                    if all(info[ny+H-1][x] == '0' for x in range(nx, nx + W)):
                        q.append((nx, ny))
                # 2. 위
                elif d == 1:
                    if all(info[ny][x] == '0' for x in range(nx, nx + W)):
                        q.append((nx, ny))
                # 3. 오른쪽
                elif d == 2:
                    if all(info[y][nx+W-1] == '0' for y in range(ny, ny + H)):
                        q.append((nx, ny))
                # 4. 왼쪽
                elif d == 3:
                    if all(info[y][nx] == '0' for y in range(ny, ny + H)):
                        q.append((nx, ny))
    moves += 1
print(-1)

"""
6 7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 1 1 0 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 1
2 3 1 1 5 5

4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
2 2 1 1 3 3

"""