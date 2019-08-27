from collections import deque

state = [list(input()) for _ in range(12)]  # 입력  .:빈공간 / RGBPY:뿌요 색깔. list로 저장해주기.


# 4개 이상인 애를 찾아서, 터트리고 return True. 재귀 말고 While문으로 반복해서 돌리자.
def check():
    visit = [[False] * 6 for _ in range(12)]  # 방문체크..
    chain = False
    for y in range(12):
        for x in range(6):
            if not visit[y][x] and state[y][x] != '.':  # 방문하지 않았고 뿌요가 있다면.
                color = state[y][x]  # 현재뿌요 색깔!
                visit[y][x] = True
                q = deque()  # bfs돌기..
                q.append((x, y))
                puyos = [(x, y)]
                while q:
                    cx, cy = q.popleft()
                    if cx > 0 and not visit[cy][cx - 1] and state[cy][cx - 1] == color:
                        visit[cy][cx - 1] = True
                        puyos.append((cx - 1, cy))
                        q.append((cx - 1, cy))
                    if cx < 5 and not visit[cy][cx + 1] and state[cy][cx + 1] == color:
                        visit[cy][cx + 1] = True
                        puyos.append((cx + 1, cy))
                        q.append((cx + 1, cy))
                    if cy > 0 and not visit[cy - 1][cx] and state[cy - 1][cx] == color:
                        visit[cy - 1][cx] = True
                        puyos.append((cx, cy - 1))
                        q.append((cx, cy - 1))
                    if cy < 11 and not visit[cy + 1][cx] and state[cy + 1][cx] == color:
                        visit[cy + 1][cx] = True
                        puyos.append((cx, cy + 1))
                        q.append((cx, cy + 1))
                if len(puyos) > 3:  # 4개 이상이 붙어있으면 터뜨리기.
                    chain = True
                    for x, y in puyos:
                        state[y][x] = '.'

    if chain:
        return True
    else:
        return False
# 뿌요 밑에 빈 공간이 생기면, 거기로 떨어뜨려주기.
def nextState():
    for x in range(6):
        is_empty = False  # 빈 공간이 있나..
        std_idx = 11  # 위에 있는 뿌요가 떨어질 index. 맨 밑칸.. 11
        for y in range(11, -1, -1):  # column별로 밑에서부터 검사..
            if not is_empty and state[y][x] == '.':
                is_empty = True
                std_idx = y  # 위에 있는 뿌요가 여기로 떨어짐..
            if is_empty and state[y][x] != '.':  # 위에 뿌요가 떨어짐..
                state[std_idx][x], state[y][x] = state[y][x], '.'  # 떨어뜨려주고
                std_idx -= 1  # 다음 떨어질 애는 그 위칸..


chain = 0  # 몇연쇄인지..
while check():  # 4개이상 붙은 뿌요가 있는동안. 터트리고
    nextState()  # 떨어뜨리기..
    for y in range(12):
        print(''.join(state[y]))
    print('\n\n')
    chain += 1

print(chain)