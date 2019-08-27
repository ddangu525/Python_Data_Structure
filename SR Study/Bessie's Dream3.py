import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
visit = [[False] * M for _ in range(N)]
maze = []
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(M):
        # red는 다 방문처리..
        if row[x] == 0:
            visit[y][x] = 3
    maze.append(row)

# 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위쪽
dx = 1, 0, -1, 0
dy = 0, 1, 0, -1

q = deque()
q.append((1, 0, 0, 0)) # x, y, smellOrange, direction of the previous move.
q.append((0, 1, 0, 1))
# 얘는 그냥은 방문체크가 안되는 핑크인애들 반복 방지용으로!
q_set = set()
# q_set.add((1, 0, 0, 0))
# q_set.add((0, 1, 0, 1))
move = 1
while q:
    for _ in range(len(q)):
        cx, cy, o, d = q.popleft()
        print(f'현재 정보.. {cx, cy, o, d, move}')
        # 1. 도착하면 프린트하고 종료!
        if (cx, cy) == (M-1, N-1):
            print(move)
            exit()
        # 2. 방문한데면 넘어가기.
        if visit[cy][cx] == 3:
            continue
        # 3. 오렌지향 없는데 블루인경우.
        if maze[cy][cx] == 3 and not o:
            continue
        # 4. 핑크인경우
        if maze[cy][cx] == 1:
            if (cx, cy, o, d) in q_set:
                continue
            # 왼쪽으로.
            if cx>0:
                q.append((cx - 1, cy, o, 2))
            # 오른쪽으로
            if cx<M-1:
                q.append((cx + 1, cy, o, 0))
            # 위로
            if cy>0:
                q.append((cx, cy - 1, o, 3))
            # 밑
            if cy<N-1:
                q.append((cx, cy + 1, o, 1))
            # 오렌지향이 있으면 방문체크.
            if o:
                visit[cy][cx] = 3
            q_set.add((cx, cy, o, d))

        # 5. 오렌지인경우!
        if maze[cy][cx] == 2:
            # 왼쪽으로.
            if cx > 0:
                q.append((cx - 1, cy, 1, 2))
            # 오른쪽으로
            if cx < M - 1:
                q.append((cx + 1, cy, 1, 0))
            # 위로
            if cy > 0:
                q.append((cx, cy - 1, 1, 3))
            # 밑
            if cy < N - 1:
                q.append((cx, cy + 1, 1, 1))
            # 얘는 항상 방문체크 가능.
            visit[cy][cx] = 3

        # 6. 블루인경우! o==1이어야 이동가능. 아까 조건에서 o==0인경우는 거름.
        if maze[cy][cx] == 3:
            # 왼쪽으로.
            if cx > 0:
                q.append((cx - 1, cy, 1, 2))
            # 오른쪽으로
            if cx < M - 1:
                q.append((cx + 1, cy, 1, 0))
            # 위로
            if cy > 0:
                q.append((cx, cy - 1, 1, 3))
            # 밑
            if cy < N - 1:
                q.append((cx, cy + 1, 1, 1))
            # 얘도 항상 방문체크 가능.
            visit[cy][cx] = 3

        # 7. purple인경우!!!! 가장 중요!!!!!! 이거 방문체크 어떻게하냐.. 1이면 가로방향간것, 2면 세로방향, 3이면 둘 다 지난것.
        if maze[cy][cx] == 4:
            if d in (0, 2):
                # 이미 가로방향 갔으면 안됨
                if visit[cy][cx] == 1:
                    continue
                visit[cy][cx] += 1
            else:
                if visit[cy][cx] == 2:
                    continue
                visit[cy][cx] += 2
            # 다음칸으로 갈 수 있으면 가기!! 또 purple이거나, pink, orange인경우!
            nx, ny = cx + dx[d], cy + dy[d]
            # 범위내에있으면..이부분 다시..
            if nx>=0 and ny>=0 and nx<=M-1 and ny<=N-1:
                # 방문안한 핑크, 오렌지인경우 거기로 감..냄새 없어짐.
                if maze[ny][nx] in (1, 2):
                    if not visit[ny][nx]:
                        q.append((nx, ny, 0, d))
                # 또 보라색인경우..
                elif maze[ny][nx] == 4:
                    if d in (0, 2):
                        # 이미 가로방향 갔으면 안됨
                        if visit[ny][nx] == 1:
                            continue
                    else:
                        if visit[ny][nx] == 2:
                            continue
                    q.append((nx, ny, d, 0))
                # 현재 방향으로 다음칸이 red이거나 blue라서 못가는경우 그 칸에서 수직으로 이동가능
                else:
                    # 가로방향.. 세로방향으로 두 개..
                    if d in (0, 2):
                        # 위로
                        if cy > 0:
                            q.append((cx, cy - 1, 0, 3))
                        # 아래로
                        if cy < N - 1:
                            q.append((cx, cy + 1, 0, 1))
                    # 세로방향.. 가로방향으로 두 개.
                    else:
                        # 왼쪽
                        if cx > 0:
                            q.append((cx - 1, cy, 0, 2))
                        # 오른쪽
                        if cx < M - 1:
                            q.append((cx + 1, cy, 0, 0))
            # 벽에 막힘.. 더 이동 못함..
            else:
                # 가로방향.. 세로방향으로 두 개..
                if d in (0, 2):
                    # 위로
                    if cy > 0:
                        q.append((cx, cy - 1, 0, 3))
                    # 아래로
                    if cy < N - 1:
                        q.append((cx, cy + 1, 0, 1))
                # 세로방향.. 가로방향으로 두 개.
                else:
                    # 왼쪽
                    if cx > 0:
                        q.append((cx - 1, cy, 0, 2))
                    # 오른쪽
                    if cx < M - 1:
                        q.append((cx + 1, cy, 0, 0))
    move += 1
print(-1)

"""
이거 해결하기... 아직도 보라색이 구현이 틀리다.
5 5
1 0 1 4 4
1 0 4 0 4
1 4 4 4 1
0 0 1 1 3
1 0 2 3 1

정답은 DDRRRRUULLDDDDRR 이렇게 해서 16이 나와야함..
"""