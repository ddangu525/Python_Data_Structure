from collections import deque
import sys
sys.stdin = open("./test_data/labudovi.i06", "r")
# input = sys.stdin.readline
R, C = map(int, input().split())

# 호수 입력받고, 백조 두 마리의 현재 좌표 저장.
# 이동 가능: '.' / 빙판(이동불가): '#' / 백조: 'L'
lake = [list(input().rstrip())]
swans = []
# 다음날 녹을 빙판들... 큐 돌면서 빙판 녹여주고, 다음에 녹을애들 다시 큐에 저장..
# 돌 때 카피한 다음에 지워줘야함!! 검사는 복사본으로.
# 물 탐색 후에 다음 큐를 얘네로 쓴다!
toBeMelted = set()

# 일단 첫번째 줄..얘는 좌우만..
for x in range(C):
    if lake[0][x] == 'L':
        swans.append((x, 0))
    elif x > 0 and lake[0][x] == 'X' and lake[0][x - 1] in '.L':
        toBeMelted.add((x, 0))
    elif x < C-1 and lake[0][x] == 'X' and lake[0][x + 1] in '.L':
        toBeMelted.add((x, 0))

# 그 다음줄부터는 위, 옆 검사..
for y in range(1, R):
    row = list(input().rstrip())
    for x in range(C):
        if row[x] == 'L':
            swans.append((x, y))
        # 왼쪽이 물이면..
        elif x > 0 and row[x] == 'X' and row[x - 1] in '.L':
            toBeMelted.add((x, y))
        # 오른쪽이 물이면..
        elif x < C - 1 and row[x] == 'X' and row[x + 1] in '.L':
            toBeMelted.add((x, y))
        # 위가 물이면..
        elif row[x] == 'X' and lake[y - 1][x] in '.L':
            toBeMelted.add((x, y))
        # 이전줄에서 밑에가 물인애 찾기.. 얘는 elif로 쓰면 안되지!
        if row[x] in '.L' and lake[y - 1][x] == 'X':
            toBeMelted.add((x, y - 1))
    lake.append(row)

# # 첫번째 줄 밑에 라인 검사 다시.
# for x in range(C):
#     if lake[0][x] == 'X' and lake[1][x] == '.':
#         toBeMelted.add((x, 0))
#     elif lake[0][x] == 'X' and lake[1][x] == '.':
#         toBeMelted.add((x, 0))

# 이제부터
# 1. 백조 1 위치에서 연결된 모든 물을 탐색.
# 2. 백조 2를 찾으면 종료, 없으면 하루가 지나 빙판을 녹인다.
# 3. 다시 이동가능하면 1로 채운다. 백조2를 찾을때까지 반복(L)

# print(f'녹을 애들 좌표 {toBeMelted}')
# print(len(toBeMelted))
dx = 0, 0, 1, -1
dy = 1, -1, 0, 0

visit = [[False] * C for _ in range(R)]

q = deque()
q.append(swans[0])
visit[swans[0][1]][swans[0][0]] = True
day = 0
while True:
    # 1. 백조1에서부터 물 지역 탐색. 가장자리를 저장해놔야하는데..
    next_q = deque()
    while q:
        cx, cy = q.popleft()
        lake[cy][cx] = '1'
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if nx >= 0 and ny >= 0 and nx < C and ny < R and not visit[ny][nx]:
                # 물 탐색..
                if lake[ny][nx] == '.':
                    q.append((nx, ny))
                    visit[ny][nx] = True
                # 빙판이면 얘는 다음에 녹으니까 얘부터 시작..
                elif lake[ny][nx] == 'X':
                    next_q.append((nx, ny))
                    visit[ny][nx] = True
                elif lake[ny][nx] == 'L':
                    # print('찾았따')
                    # for i in range(R):
                    #     print(''.join(lake[i]))
                    print(day)
                    exit()
    # 다음에는 얘네부터
    q = next_q
    # 2. 빙판 녹여주기.
    day += 1
    copied = toBeMelted.copy()
    next_melted = set()
    for _ in range(len(copied)):
        cx, cy = toBeMelted.pop()
        lake[cy][cx] = '.'
        # 현재 녹을 애가 아닌 안쪽의 빙판이면 다음에 녹을애에 추가.
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            # 범위 안에 있고
            if nx >= 0 and ny >= 0 and nx < C and ny < R:
                # 현재 녹지 않는 빙판이라면..
                if lake[ny][nx] == 'X' and (nx, ny) not in copied:
                    next_melted.add((nx, ny))
    # print(f'{day}번 녹이고 나서 호수 모습..')
    # for i in range(R):
    #     print(''.join(lake[i]))
    toBeMelted = next_melted

