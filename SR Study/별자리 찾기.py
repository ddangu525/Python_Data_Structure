import sys
input = sys.stdin.readline
m = int(input())
constellation = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
stars = set(tuple(map(int, input().split())) for _ in range(n))

cx, cy = constellation[0]
for bx, by in stars:
    dx, dy = bx - cx, by - cy
    found = True
    for rx, ry in constellation[1:]:
        if (rx + dx, ry + dy) not in stars:
            found = False
            break
    if found:
        print(dx, dy)
        break