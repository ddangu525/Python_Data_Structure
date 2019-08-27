from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
if N==M==1:
    print(1)
    exit()
maze = [list(input().rstrip()) for _ in range(N)]
visit = [[[False] * (K+1) for x in range(M)] for y in range(N)]

dx = 0, 0, 1, -1
dy = 1, -1, 0, 0
q = deque()
q.append((0, 0, 0))  # x, y, # of break
visit[0][0][0] = True
dist = 1
while q:
    for _ in range(len(q)):
        cx, cy, k = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            # 범위 안에 있을 때
            if nx >= 0 and ny >= 0 and nx < M and ny < N and not visit[ny][nx][k]:
                # 빈칸. 그냥 가능
                if maze[ny][nx] == '0':
                    visit[ny][nx][k] = True
                    q.append((nx, ny, k))
                    # 도착점이면.
                    if (nx, ny) == (M - 1, N - 1):
                        print(dist + 1)
                        exit()
                # 벽.. 아직 부술수 있을때만 가능
                if maze[ny][nx] == '1' and k < K:
                    visit[ny][nx][k + 1] = True
                    q.append((nx, ny, k + 1))
    dist += 1
print(-1)