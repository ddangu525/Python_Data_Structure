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

dx = 0, 0, 1, -1
dy = 1, -1, 0, 0
key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# 방문했던 상태들 저장.
visited = set()

q = deque()
q.append((sx, sy, 1))  # 좌표와, 열쇠정보. 1은 아무키도 없을때.. 2^0
visited.add((sx, sy, 1))
dist = 0
while q:
    for _ in range(len(q)):
        cx, cy, keys = q.popleft()
        # 네방향 탐색..
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            # 범위내에 있고 벽이 아니라면
            if nx >= 0 and ny >= 0 and nx < M and ny < N and maze[ny][nx] != '#':
                # 방문하지 않은 상태라면
                if (nx, ny, keys) not in visited:
                    # 탈출..
                    if maze[ny][nx] == '1':
                        print(dist + 1)
                        exit()
                    # 열쇠찾음.
                    elif maze[ny][nx] in 'abcdef':
                        new_keys = keys | 1<<key[maze[ny][nx]]
                        visited.add((nx, ny, new_keys))
                        q.append((nx, ny, new_keys))
                    # 문. 키가 있어야 함.
                    elif maze[ny][nx] in 'ABCDEF':
                        # 키가 있으면
                        if 1<<key[maze[ny][nx].lower()] & keys:
                            visited.add((nx, ny, keys))
                            q.append((nx, ny, keys))
                    # 빈칸.!
                    else:
                        visited.add((nx, ny, keys))
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