boards = []         # 5개의 판 정보 저장. 각각은 5x5

# 25줄에 걸쳐 input 받기.
for _ in range(5):
    board = [list(map(int, input().split())) for _ in range(5)]
    boards.append(board)

#
print(boards)