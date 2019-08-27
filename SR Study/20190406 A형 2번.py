# 백준 문제 형식
def search(board_set, a=5, b=5, c=5, d=5, e=5, used=0):
    global min_nums
    if used == min_nums:
        return
    if any(i < 0 for i in (a, b, c, d, e)):
        return
    if not board_set:
        min_nums = used
        return
    cx, cy = min(board_set, key=lambda x: (x[1],x[0]))
    if all((x, y) in board_set for x in range(cx, cx + 5) for y in range(cy, cy + 5)):
        new_board = board_set.difference(set((x, y) for x in range(cx, cx + 5) for y in range(cy, cy + 5)))
        search(new_board, a, b, c, d, e - 1, used + 1)
    if all((x, y) in board_set for x in range(cx, cx + 4) for y in range(cy, cy + 4)):
        new_board = board_set.difference(set((x, y) for x in range(cx, cx + 4) for y in range(cy, cy + 4)))
        search(new_board, a, b, c, d - 1, e, used + 1)
    if all((x, y) in board_set for x in range(cx, cx + 3) for y in range(cy, cy + 3)):
        new_board = board_set.difference(set((x, y) for x in range(cx, cx + 3) for y in range(cy, cy + 3)))
        search(new_board, a, b, c - 1, d, e, used + 1)
    if all((x, y) in board_set for x in range(cx, cx + 2) for y in range(cy, cy + 2)):
        new_board = board_set.difference(set((x, y) for x in range(cx, cx + 2) for y in range(cy, cy + 2)))
        search(new_board, a, b - 1, c, d, e, used + 1)
    temp = set()
    temp.add((cx, cy))
    search(board_set.difference(temp), a - 1, b, c, d, e, used + 1)

board = set()
for y in range(10):
    row = input().split()
    for x in range(10):
        if row[x] == '1':
            board.add((x, y))

if not board:
    print(0)
    exit()

min_nums = float('inf')
search(board)
print(min_nums!=float('inf') and min_nums or -1)