import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
v1 = [[False] * N for _ in range(N)]   # 일반 방문체크
v2 = [[False] * N for _ in range(N)]   # 적록색약 방문체크
paint = [input().rstrip() for _ in range(N)]

diff = ((0,1),(0,-1),(1,0),(-1,0))
a1 = a2 = 0  # 일반, 색약 구역의 수.
for y in range(N):
    for x in range(N):
        if not v1[y][x]:
            v1[y][x] = True
            color = paint[y][x]
            q = deque()
            q.append((x,y))
            while q:
                cx, cy = q.popleft()
                for dx, dy in diff:
                    nx, ny = cx+dx, cy+dy
                    if nx>=0 and ny>=0 and nx<N and ny<N and not v1[ny][nx] and paint[ny][nx]==color:
                        q.append((nx,ny))
                        v1[ny][nx] = True
            a1 += 1
        if not v2[y][x]:
            v2[y][x] = True
            color = paint[y][x]
            if color == 'G':   # RG를 같게..
                color = 'R'
            q = deque()
            q.append((x,y))
            while q:
                cx, cy = q.popleft()
                for dx, dy in diff:
                    nx, ny = cx+dx, cy+dy
                    if nx>=0 and ny>=0 and nx<N and ny<N and not v2[ny][nx]:
                        if color == 'R' and paint[ny][nx]!='B':
                            q.append((nx,ny))
                            v2[ny][nx] = True
                        elif color =='B' and paint[ny][nx] == 'B':
                            q.append((nx,ny))
                            v2[ny][nx] = True
            a2 += 1
print(a1, a2)