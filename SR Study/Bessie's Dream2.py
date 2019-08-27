import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
# 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위쪽
dx = 1, 0, -1, 0
dy = 0, 1, 0, -1

q = deque()
q.append((1, 0, 0, 0))   # x, y, d, o, p d: 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위. 이전에 무슨방향이었는지.. 이전에 보라였는지..
q.append((0, 1, 1, 0))
visit[0][0] = True
q_set = set()
move = 1
while q:
    for _ in range(len(q)):
        cx, cy, d, o = q.popleft()   # 현재 좌표, 이전 방향, 오렌지.. 유효한 좌푠지 확인하고 진행..
        # 배열 범위 벗어난경우.. 안됨.
        if cx<0 or cx==M or cy<0 or cy==N:
            continue
        # print(f'{cx}, {cy}, {move}')
        # 이미 확인한 state.
        if (cx, cy, d, o) in q_set:
            # print(f'여기서 {cx}, {cy}, {d}, {o} 걸러짐')
            continue
        # 정답 찾은경우
        if (cx, cy) == (M-1, N-1):
            print(move)
            exit()
        # red거나 오렌지향이 아닌 피라냐칸.. 안됨.. 그리고 방문한 오렌지 칸인 경우도 안됨.
        if maze[cy][cx]==0 or (maze[cy][cx]==3 and o==0) or visit[cy][cx]:
            continue

        # 현재 상태가 가능한지 여부..
        possible = False
        # 핑크면 그냥 가능. pink visit체크하면 안되겠다..
        if maze[cy][cx] == 1:
            possible = True
        # 오렌지도 가능. visit 체크. o=1로 만들어주기
        elif maze[cy][cx] == 2:
            o = 1
            visit[cy][cx] = True
            possible = True
        # 오렌지향이 있으면 블루도 가능.
        elif maze[cy][cx] == 3 and o:
            possible = True
        # 현재상태가 가능하면 네방향으로 다시 이동.
        if possible:
            # 현재 상태 set에 추가.
            q_set.add((cx, cy, d, o))
            if cx>0:
                q.append((cx - 1, cy, 2, o))
            if cx<M-1:
                q.append((cx + 1, cy, 0, o))
            if cy>0:
                q.append((cx, cy - 1, 3, o))
            if cy<N-1:
                q.append((cx, cy + 1, 1, o))
        # 여기서 주의!! 배열 끝의 보라색일경우!!
        if maze[cy][cx]==4:
            # 오른쪽으로 미끄러지는데 오른쪽 끝칸이 보라색인경우.. 상, 하로 이동가능. + blue가 나온경우.. 그칸에서 진행..
            if d == 0 and cx == M-1 or (cx < M-1 and maze[cy][cx + 1] == 3):
                q.append((cx, cy + 1, 1, 0))
                q.append((cx, cy - 1, 3, 0))
            # 아래로 가는데 끝칸인경우
            elif d == 1 and cy == N-1 or (cy < N-1 and maze[cy + 1][cx] == 3):
                q.append((cx + 1, cy, 0, 0))
                q.append((cx - 1, cy, 2, 0))
            # 왼쪽으로 가고 왼쪽 끝칸..
            elif d == 2 and cx == 0 or (cx > 0 and maze[cy][cx - 1] == 3):
                q.append((cx, cy + 1, 1, 0))
                q.append((cx, cy - 1, 3, 0))
            # 위로가고 위쪽 끝칸..
            elif d == 3 and cy == 0 or (cy > 0 and maze[cy - 1][cx] == 3):
                q.append((cx + 1, cy, 0, 0))
                q.append((cx - 1, cy, 2, 0))
            # 그 외의 경우 전에 온 방향으로만 다시 한칸 더 감.
            else:
                visit[cy][cx] = True
                q.append((cx + dx[d], cy + dy[d], d, 0))
    move += 1
print(-1)