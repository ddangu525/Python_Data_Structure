import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

q = deque()
q.append((0, 0, 0, 0))   # x, y, o, move!
visit[0][0] = True
min_move = float('inf')
found = False
q_set = set()
while q:
    cx, cy, o, move = q.popleft()
    print(cx, cy, move)
    # move가 많거나 이미 본 상태이면 넘어가기
    if move>=min_move or (cx,cy,o) in q_set:
        # print(f'여기서 {cx}, {cy}, {o} 걸러짐')
        continue
    q_set.add((cx,cy,o))
    # 일단 방문여부부터.
    # 1. 얘는 왼쪽으로 가는경우.. x가 작아짐. 이 경우에는 답이 나올 수가 없다.
    if cx > 0 and not visit[cy][cx - 1]:
        # red로 못감
        if maze[cy][cx - 1] == 0:
            visit[cy][cx - 1] = True
        # pink는 그대로 진행
        elif maze[cy][cx - 1] == 1:
            visit[cy][cx - 1] = True
            q.append((cx - 1, cy, o, move+1))
            # q_set.add((cx - 1, cy, o))
        # orange인경우 오렌지냄새가 생김! 방문체크 해줘야하나...
        elif maze[cy][cx - 1] == 2:
            visit[cy][cx - 1] = True
            q.append((cx - 1, cy, 1, move+1))
            # q_set.add((cx - 1, cy, 1))
        # blue인경우 오렌지향이 있어야만 가능
        elif maze[cy][cx - 1] == 3 and o == 1:
            visit[cy][cx - 1] = True
            q.append((cx - 1, cy, 1, move+1))
            # q_set.add((cx - 1, cy, 1))
        # !!!!! purple인경우. 그 방향으로 nonpurple이 나오거나, 못가는 칸이 나올때까지 진행.냄새도 없어짐.
        elif maze[cy][cx - 1] == 4:
            for x in range(cx - 1, -1, -1):
                move += 1
                # 이동못하면 이전칸에 멈추기.
                if maze[cy][x] == 0 or maze[cy][x] == 3:
                    q.append((x + 1, cy, 0, move-1))
                    # q_set.add((x + 1, cy, 0))
                    break
                # 이동가능하고 nonpurple인경우 그 칸에 멈추기
                elif maze[cy][x] == 1 or maze[cy][x] == 2 or x == 0:
                    q.append((x, cy, 0, move))
                    # q_set.add((x, cy, 0))
                    break

    # 2. 오른쪽으로 가는 경우. 이 경우엔 답 나올 수 있음..
    if cx < M - 1 and not visit[cy][cx + 1]:
        # 답인경우!
        if (cx + 1, cy) == (M - 1, N - 1):
            if move<min_move:
                min_move = move
                found = True
                continue
        # red로 못감
        if maze[cy][cx + 1] == 0:
            visit[cy][cx + 1] = True
        # pink는 그대로 진행
        elif maze[cy][cx + 1] == 1:
            visit[cy][cx + 1] = True
            q.append((cx + 1, cy, o, move + 1))
            # q_set.add((cx + 1, cy, o))
        # orange인경우 오렌지냄새가 생김! 방문체크 해줘야하나...
        elif maze[cy][cx + 1] == 2:
            visit[cy][cx + 1] = True
            q.append((cx + 1, cy, 1, move + 1))
            # q_set.add((cx + 1, cy, 1))
        # blue인경우 오렌지향이 있어야만 가능
        elif maze[cy][cx + 1] == 3 and o == 1:
            visit[cy][cx + 1] = True
            q.append((cx + 1, cy, 1, move + 1))
            # q_set.add((cx + 1, cy, 1))
        # !!!!! purple인경우. 그 방향으로 nonpurple이 나오거나, 못가는 칸이 나올때까지 진행.냄새도 없어짐.
        elif maze[cy][cx + 1] == 4:
            for x in range(cx + 1, M):
                move += 1
                # 이동못하면 이전칸에 멈추기.
                if maze[cy][x] == 0 or maze[cy][x] == 3:
                    q.append((x - 1, cy, 0, move-1))
                    # q_set.add((x - 1, cy, 0))
                    break
                    # 이동가능하고 nonpurple인경우 그 칸에 멈추기
                elif maze[cy][x] == 1 or maze[cy][x] == 2 or x == M - 1:
                    q.append((x, cy, 0, move))
                    # q_set.add((x, cy, 0))
                    break

    # 3. 위로 가는경우.. 이경우 답 안나옴.
    if cy > 0 and not visit[cy - 1][cx]:
        # red로 못감
        if maze[cy - 1][cx] == 0:
            visit[cy - 1][cx] = True
        # pink는 그대로 진행
        elif maze[cy - 1][cx] == 1:
            visit[cy - 1][cx] = True
            q.append((cx, cy - 1, o, move + 1))
            # q_set.add((cx, cy - 1, o))
        # orange인경우 오렌지냄새가 생김! 방문체크 해줘야하나...
        elif maze[cy - 1][cx] == 2:
            visit[cy - 1][cx] = True
            q.append((cx, cy - 1, 1, move + 1))
            # q_set.add((cx, cy - 1, 1))
        # blue인경우 오렌지향이 있어야만 가능
        elif maze[cy - 1][cx] == 3 and o == 1:
            visit[cy - 1][cx] = True
            q.append((cx, cy - 1, 1, move + 1))
            # q_set.add((cx, cy - 1, 1))
        # !!!!! purple인경우. 그 방향으로 nonpurple이 나오거나, 못가는 칸이 나올때까지 진행.냄새도 없어짐.
        elif maze[cy - 1][cx] == 4:
            for y in range(cy - 1, -1, -1):
                move += 1
                # 이동못하면 이전칸에 멈추기.
                if maze[y][cx] == 0 or maze[y][cx] == 3:
                    q.append((cx, y + 1, 0, move-1))
                    # q_set.add((cx, y + 1, 0))
                    break
                    # 이동가능하고 nonpurple인경우 그 칸에 멈추기
                elif maze[y][cx] == 1 or maze[y][cx] == 2 or y == 0:
                    q.append((cx, y, 0, move))
                    # q_set.add((cx, y, 0))
                    break

    # 4. 아래로 가는 경우! 답 가능
    if cy < N - 1 and not visit[cy + 1][cx]:
        # 답인경우!
        if (cx, cy + 1) == (M - 1, N - 1):
            if move<min_move:
                min_move = move
                found = True
                continue
        # red로 못감
        if maze[cy + 1][cx] == 0:
            visit[cy + 1][cx] = True
        # pink는 그대로 진행
        elif maze[cy + 1][cx] == 1:
            visit[cy + 1][cx] = True
            q.append((cx, cy + 1, o, move + 1))
            # q_set.add((cx, cy + 1, o))
        # orange인경우 오렌지냄새가 생김! 방문체크 해줘야하나...
        elif maze[cy + 1][cx] == 2:
            visit[cy + 1][cx] = True
            q.append((cx + 1, cy, 1, move + 1))
            # q_set.add((cx, cy + 1, 1))
        # blue인경우 오렌지향이 있어야만 가능
        elif maze[cy + 1][cx] == 3 and o == 1:
            visit[cy + 1][cx] = True
            q.append((cx, cy + 1, 1, move + 1))
            # q_set.add((cx, cy + 1, 1))
        # !!!!! purple인경우. 그 방향으로 nonpurple이 나오거나, 못가는 칸이 나올때까지 진행.냄새도 없어짐.
        elif maze[cy + 1][cx] == 4:
            for y in range(cy + 1, N):
                move += 1
                # 이동못하면 이전칸에 멈추기.
                if maze[y][cx] == 0 or maze[y][cx] == 3:
                    q.append((cx, y - 1, 0, move - 1))
                    # q_set.add((cx, y - 1, 0))
                    break
                    # 이동가능하고 nonpurple인경우 그 칸에 멈추기
                elif maze[y][cx] == 1 or maze[y][cx] == 2 or y == N - 1:
                    q.append((cx, y, 0, move))
                    # q_set.add((cx, y, 0))
                    break
if found:
    print(min_move)
else:
    print(-1)