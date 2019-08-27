from itertools import combinations
from collections import deque
A = [input() for _ in range(5)]
info = {5*y+x:(x,y, A[y][x]) for x in range(5) for y in range(5)}  # y, x, 무슨파인지..
ans = 0
# 0~24번 중 7명 선택.
for case in combinations(range(25), 7):
    # 선택한 애들 돌면서..
    # 1. 임도연파가 4개 이상이면 안되는경우. 바로 통과.
    if sum(1 for i in case if info[i][2]=='Y')>3:
        continue
    # 2. 이제 붙어있는지를 검사..(x,y)를 받고 얘를 더한값을 정렬해서 차이를 보기.. 정확하지 않은뎁..ㅜㅠㅠ
    coords = set((info[k][0],info[k][1]) for k in case)
    q = deque()
    q.append(coords.pop())
    while q:
        x, y = q.popleft()
        if x>0 and (x-1,y) in coords:
            q.append((x - 1, y))
            coords.remove((x-1,y))
        if x<4 and (x+1, y) in coords:
            q.append((x + 1, y))
            coords.remove((x + 1, y))
        if y>0 and (x, y-1) in coords:
            q.append((x, y - 1))
            coords.remove((x, y - 1))
        if y<4 and (x, y+1) in coords:
            q.append((x, y + 1))
            coords.remove((x, y + 1))
    if not coords:
        print(case)
        ans += 1
print(ans)