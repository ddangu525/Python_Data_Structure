import sys
input = sys.stdin.readline
from itertools import combinations
N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]
num_coords = {(N-2)*(y-1)+x:(x,y) for y in range(1,N-1) for x in range(1,N-1)}  # x,y순서로 저장.
# 최소값 초기화
min_value = float('inf')
for c1, c2, c3 in combinations(range(1,(N-2)**2+1), 3):   # 전체 중에 3개 선택.
    x1, y1 = num_coords[c1]
    x2, y2 = num_coords[c2]
    x3, y3 = num_coords[c3]
    # 겹치는 경우 그냥 넘어가기
    if abs(x1-x2)+abs(y1-y2)<=2 or abs(x1-x3)+abs(y1-y3)<=2 or abs(x2-x3)+abs(y2-y3)<=2:
        continue
    # 되는 경우 5평의땅 모두 구해주기.
    v1 = price[y1][x1] + price[y1 - 1][x1] + price[y1 + 1][x1] + price[y1][x1 - 1] + price[y1][x1 + 1]
    v2 = price[y2][x2] + price[y2 - 1][x2] + price[y2 + 1][x2] + price[y2][x2 - 1] + price[y2][x2 + 1]
    v3 = price[y3][x3] + price[y3 - 1][x3] + price[y3 + 1][x3] + price[y3][x3 - 1] + price[y3][x3 + 1]
    value = v1 + v2 + v3
    if value<min_value:
        min_value = value
print(min_value)