import sys
input = sys.stdin.readline

N, B = map(int, input().split())
locs = [tuple(map(int, input().split())) for _ in range(N)]

min_max = float('inf')
for j in range(N):
    for i in range(N):
        a, b = locs[i][0] + 1, locs[j][1] + 1
        ul = ur = dl = dr = 0
        for x, y in locs:
            if x < a:
                if y > b:
                    ul += 1
                else:
                    dl += 1
            else:
                if y > b:
                    ur += 1
                else:
                    dr += 1
        max_val = max(ul, ur, dl, dr)
        if max_val < min_max:
            min_max = max_val
print(min_max)