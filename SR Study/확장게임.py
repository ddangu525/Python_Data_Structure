from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

dx = 0, 0, 1, -1
dy = 1, -1, 0, 0

N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
num_castles = [0] * (P + 1)
castle_info = defaultdict(list)
board = [list(input().rstrip()) for _ in range(N)]
left_cell = N * M
visit = [[False] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        if board[y][x] == '#':
            visit[y][x] = True
            left_cell -= 1
        elif board[y][x] != '.':
            player = int(board[y][x])
            castle_info[player].append((x, y))
            num_castles[player] += 1
            visit[y][x] = True
            left_cell -= 1

def go():
    global left_cell
    changed = True
    while changed:
        changed = False
        # 1번부터..가장 최근 추가된 가장자리 성에서만 검사.
        for i in range(1, P + 1):
            q = deque(castle_info[i])
            new_castles = []
            dist = 1
            while q and dist <= S[i]:
                for _ in range(len(q)):
                    cx, cy = q.popleft()
                    for d in range(4):
                        nx, ny = cx + dx[d], cy + dy[d]
                        if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx]:
                            q.append((nx, ny))
                            visit[ny][nx] = True
                            num_castles[i] += 1
                            left_cell -= 1
                            changed = True
                            if dist == S[i]:
                                new_castles.append((nx, ny))
                if left_cell == 0:
                    return
                dist += 1
            castle_info[i] = new_castles
    return
go()

print(' '.join(map(str, num_castles[1:])))

"""
3 4 4
1 1 2 1
....
####
1234
무한루프..
"""
