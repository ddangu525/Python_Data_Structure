from collections import deque, defaultdict
import sys
input = sys.stdin.readline
hex_dic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
# 구멍개수:문자
hole_dic = {0: 'W', 1: 'A', 2: 'K', 3: 'J', 4: 'S', 5: 'D'}
tc = 0
while 1:
    # input
    H, W = map(int, input().split())
    # 종료조건
    if H == 0:
        break
    # 현재 몇번 case인지..
    tc += 1
    # 그림 배열..
    paint = []
    # H줄 받아서 바꾸고 추가..
    for _ in range(H):
        row = ''
        for i in input().rstrip():
            row += hex_dic[i]
        paint.append(list(row))
    visit = [[False] * (W * 4) for _ in range(H)]

    # # 바탕에 0 다 찾아 방문체크.
    # q = deque()
    # q.append((0, 0))
    # visit[0][0] = True
    # while q:
    #     x, y = q.popleft()
    #     if x > 0 and not visit[y][x - 1] and paint[y][x - 1] == '0':
    #         q.append((x - 1, y))
    #         visit[y][x - 1] = True
    #     if x < (W * 4) - 1 and not visit[y][x + 1] and paint[y][x + 1] == '0':
    #         q.append((x + 1, y))
    #         visit[y][x + 1] = True
    #     if y > 0 and not visit[y - 1][x] and paint[y - 1][x] == '0':
    #         q.append((x, y - 1))
    #         visit[y - 1][x] = True
    #     if y < H - 1 and not visit[y + 1][x] and paint[y + 1][x] == '0':
    #         q.append((x, y + 1))
    #         visit[y + 1][x] = True

    # 포함된 문자들..
    chars = ''
    # 문자 번호..
    num = 0
    # 각 문자의 구멍이 몇갠지..
    char_hole = defaultdict(int)
    # 이제 문자 찾기.. 반드시 한 문자를 찾고 나서 그 안에 구멍(0)이 나온다.!!
    for y in range(H):
        for x in range(W*4):
            # 문자인경우.. 얘가 뭔지는 나중에 결정
            if not visit[y][x] and paint[y][x] == '1':
                # 그 다음 번호로 붙여주기
                num += 1
                q = deque()
                visit[y][x] = True
                paint[y][x] = num
                q.append((x, y))
                while q:
                    cx, cy = q.popleft()
                    if cx > 0 and not visit[cy][cx - 1] and paint[cy][cx - 1] == '1':
                        visit[cy][cx - 1] = True
                        paint[cy][cx - 1] = num
                        q.append((cx - 1, cy))
                    if cx < (W * 4) - 1 and not visit[cy][cx + 1] and paint[cy][cx + 1] == '1':
                        visit[cy][cx + 1] = True
                        paint[cy][cx + 1] = num
                        q.append((cx + 1, cy))
                    if cy > 0 and not visit[cy - 1][cx] and paint[cy - 1][cx] == '1':
                        visit[cy - 1][cx] = True
                        paint[cy - 1][cx] = num
                        q.append((cx, cy - 1))
                    if cy < H - 1 and not visit[cy + 1][cx] and paint[cy + 1][cx] == '1':
                        visit[cy + 1][cx] = True
                        paint[cy + 1][cx] = num
                        q.append((cx, cy + 1))

            # 0인경우... 얘는 바탕일 수도 있고, 빈칸일 수도 있다.
            # 바탕인경우는 그냥 check만, 구멍인경우 그 문자 구멍 수에 추가.
            # 그 다음 남은 구멍들을 통해서 찾아준 문자들이 뭔지 정보 update해가기
            elif not visit[y][x] and paint[y][x] == '0':
                # 지금 찾는 0들이 배경인지 여부..
                background = False
                q = deque()
                q.append((x, y))
                while q:
                    cx, cy = q.popleft()
                    # 찾는도중에 테두리가 있으면 그 그룹은 배경임!
                    if cx==0 or cy==0 or cx==(W*4)-1 or cy==H-1:
                        background = True
                    if cx > 0 and not visit[cy][cx - 1] and paint[cy][cx - 1] == '0':
                        visit[cy][cx - 1] = True
                        q.append((cx - 1, cy))
                    if cx < (W * 4) - 1 and not visit[cy][cx + 1] and paint[cy][cx + 1] == '0':
                        visit[cy][cx + 1] = True
                        q.append((cx + 1, cy))
                    if cy > 0 and not visit[cy - 1][cx] and paint[cy - 1][cx] == '0':
                        visit[cy - 1][cx] = True
                        q.append((cx, cy - 1))
                    if cy < H - 1 and not visit[cy + 1][cx] and paint[cy + 1][cx] == '0':
                        visit[cy + 1][cx] = True
                        q.append((cx, cy + 1))
                # 배경이 아닌경우!!
                if not background:
                    # 몇번 문자 안의 구멍인지.. 이거 나중에 해줘야. 반드시 왼쪽에 문자의 번호가 위치함!
                    n_hole = paint[y][x - 1]
                    # 일단 그 문자의 구멍 하나 추가해주기!
                    char_hole[n_hole] += 1

    # 이제 다 됐나..?
    # print(f"case #{tc}: {''.join(sorted(hole_dic[char_hole[k]] for k in range(1, num+1)))}")
    print(f'case #{tc}:', ''.join(sorted(hole_dic[char_hole[k]] for k in range(1, num+1))))