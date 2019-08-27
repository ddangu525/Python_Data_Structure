from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
r = deque([int(input()) for _ in range(n)])

min_moves = float('inf')
for _ in range(n):
    moves = sum(i * r[i] for i in range(n))
    if moves<min_moves:
        min_moves = moves
    r.rotate(1)
print(min_moves)