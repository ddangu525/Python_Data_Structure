from collections import deque

def bfs(q, t=1):
    while q:
        for _ in range(len(q)):
            cx, cy = q.popleft()  # 현재 위치.
            for dx, dy in knight:  # 8개 가능한 경우 중,
                nx, ny = cx + dx, cy + dy
                if nx >= 0 and ny >= 0 and nx < l and ny < l and not v[nx][ny]:  # 범위 안에 있고, 방문하지 않은데라면,
                    if (nx, ny) == (gx, gy):
                        print(t)
                        return
                    v[nx][ny] = True
                    q.append((nx, ny))
        t += 1

knight = ((1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1))
for _ in range(int(input())):
    l = int(input())
    v = [[False] * l for _ in range(l)]  # visit check
    x, y = map(int, input().split())  # 출발
    v[x][y] = True
    gx, gy = map(int, input().split())  # 도착 goal..
    if (x, y) == (gx, gy):
        print(0)
        continue
    q = deque()
    q.append((x, y))  # 큐에 출발 위치 추가.
    bfs(q)



