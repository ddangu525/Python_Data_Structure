from collections import deque

N, M = map(int, input().split())
piet = [list(input()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
DP = 0  # 오른쪽.
CC = -1  # 왼쪽.(DP에 대한 상대적 방향임!!)
color = ''
blocks = {}  # block의 번호: 색깔, 포함된 코델의 좌표들 저장..  cf) blocks[1]= (A, [(1,3), (2,4), 0...])
k = 1  # 블록의 번호
# 일단 블록들 번호 붙여주기.. 검은색 아닌애들만!!
for y in range(N):
    for x in range(M):
        if piet[y][x] != 'X' and not visit[y][x]:
            q = deque()
            q.append((x, y))
            c = piet[y][x]
            blocks[k] = [c, [(x, y)]]  # k번째 블록의 정보(색, 좌표들) 저장.
            piet[y][x] = k  # 블록 이름으로 바꿔주기.
            visit[y][x] = True  # 방문 체크.
            # BFS 돌면서 블록내 코델들 다 찾아 작업..
            while q:
                cx, cy = q.popleft()
                if cx > 0 and not visit[cy][cx - 1] and piet[cy][cx - 1] == c:
                    piet[cy][cx - 1] = k
                    blocks[k][1].append((cx - 1, cy))
                    q.append((cx - 1, cy))
                    visit[cy][cx - 1] = True
                if cx < M - 1 and not visit[cy][cx + 1] and piet[cy][cx + 1] == c:
                    piet[cy][cx + 1] = k
                    blocks[k][1].append((cx + 1, cy))
                    q.append((cx + 1, cy))
                    visit[cy][cx + 1] = True
                if cy > 0 and not visit[cy - 1][cx] and piet[cy - 1][cx] == c:
                    piet[cy - 1][cx] = k
                    blocks[k][1].append((cx, cy - 1))
                    q.append((cx, cy - 1))
                    visit[cy - 1][cx] = True
                if cy < N - 1 and not visit[cy + 1][cx] and piet[cy + 1][cx] == c:
                    piet[cy + 1][cx] = k
                    blocks[k][1].append((cx, cy + 1))
                    q.append((cx, cy + 1))
                    visit[cy + 1][cx] = True
            k += 1

k = 1  # 맨 왼쪽 위 1번 블록부터 시작..
color += blocks[1][0]  # 일단 맨 왼쪽위 블록색깔!!
while True:  # 종료될때까지 계속 반복.
    print(f'현재 블록번호 = {k}, 방문경로 = {color}')
    end = False
    cc_changed = False
    for case in range(8):  # 최대 8가지 검사 후 안되면 프로그램 종료
        # 현재 DP, CC로 검사.
        searched = False
        if DP == 0:  # 오른쪽.. x값이 커야하고.. 같으면 y값 비교..CC가 왼쪽(-1)이면 y 작은거.. 아니면 큰거..
            nx, ny = sorted(blocks[k][1], key=lambda x: (-x[0], -CC * x[1]))[0]
            # 안되는 경우..
            if nx == M - 1 or piet[ny][nx + 1] == 'X':
                pass
            # 되는경우!
            else:
                k = piet[ny][nx + 1]
                searched = True
        elif DP == 1:  # 아래쪽. y값이 커야하고, 같으면 x값 비교.CC가 왼쪽이면 x 큰거..
            nx, ny = sorted(blocks[k][1], key=lambda x: (-x[1], CC * x[0]))[0]
            if ny == N - 1 or piet[ny + 1][nx] == 'X':
                pass
            else:
                k = piet[ny + 1][nx]
                searched = True
        elif DP == 2:  # 왼쪽. x값이 작아야하고, 같으면 y값 비교. CC가 1이면 y 작은거 선택.
            nx, ny = sorted(blocks[k][1], key=lambda x: (x[0], CC * x[1]))[0]
            if nx == 0 or piet[ny][nx - 1] == 'X':
                pass
            else:
                k = piet[ny][nx - 1]
                searched = True
        else:  # 위.. y값 작아야 하고, 같으면 x값 비교.. CC가 오른쪽이면 x 큰거.
            nx, ny = sorted(blocks[k][1], key=lambda x: (x[1], -CC * x[0]))[0]
            if ny == 0 or piet[ny - 1][nx] == 'X':
                pass
            else:
                k = piet[ny - 1][nx]
                searched = True

        # 찾았으면 더해주고 다음으로 넘어감.
        if searched:
            color += blocks[k][0]
            break
        # 안되면 바꿔줌.. CC가 한번 바꼈다면, DP를 바꿔줘야함. 시게방향 90도 회전.
        if cc_changed:
            DP = (DP + 1) % 4
            cc_changed = False
        else:
            CC *= -1
            cc_changed = True
        if case==7:
            end = True
    if end:
        break
print(color)