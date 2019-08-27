from collections import deque

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 테두리의 개수 순서대로 바깥쪽에서 0번째, 1번째, i번째 테두리의 원소들.
# 각 리스트의 첫번재 인덱스는 (i,i)이고 시계방향으로 저장.
num_edges = min(N, M) // 2
edges_coor = [[] for _ in range(num_edges)]  # 얘는 테두리의 좌표 저장!       (y, x)로 저장하자.
edges_val = [deque() for _ in range(num_edges)]  # 얘는 값.. 얘를 rotate 시킨다.

# 테두리 원소 추가해주기.
for i in range(num_edges):
    # 1. 윗면
    for x in range(i, M - i):
        edges_coor[i].append((i, x))  # 기준 좌표 저장.
        edges_val[i].append(A[i][x])  # 값 저장
    # 2. 오른쪽면
    for y in range(i + 1, N - 1 - i):
        edges_coor[i].append((y, M - 1 - i))
        edges_val[i].append(A[y][M - 1 - i])
    # 3. 아랫면
    for x in range(M - 1 - i, i - 1, -1):
        edges_coor[i].append((N - 1 - i, x))
        edges_val[i].append(A[N - 1 - i][x])
    # 4. 왼쪽면
    for y in range(N - 2 - i, i, -1):
        edges_coor[i].append((y, i))
        edges_val[i].append(A[y][i])

# 값들 회전 해주기..
for edge in edges_val:
    edge.rotate(-R)

# 값들 바꿔주기
for i in range(num_edges):  # i번째 테두리에서
    for k in range(len(edges_coor[i])):  # i번째 테두리 원소들을 돌면서
        y, x = edges_coor[i][k]  # k번째 원소의 좌표..
        A[y][x] = edges_val[i][k]  # 회전한 결과값으로 바꿔주기!

# 출력
for y in range(N):
    print(' '.join(map(str, A[y])))