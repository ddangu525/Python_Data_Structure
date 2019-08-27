N, M = map(int, input().split())
# 빈 좌석 20개짜리 기차 N개..  인덱스 조심
trains = [[0]*21 for _ in range(N+1)]

# 명령받아서 수행하기..
for _ in range(M):
    *order, = map(int, input().split())
    # 태우기 명령. order[1]번째 기차에 order[2]번째 좌석에 태우기.
    if order[0]==1:
        trains[order[1]][order[2]] = 1
    # 내리기 명령
    elif order[0]==2:
        trains[order[1]][order[2]] = 0
    # 한칸씩 뒤로(20번째는 내려짐) order[1]번째 기차 한칸씩 뒤로..
    elif order[0]==3:
        trains[order[1]] = [0, 0] + trains[order[1]][1:-1]
    # 한칸씩 앞으로(1번째는 내려짐)
    else:
        trains[order[1]] = [0] + trains[order[1]][2:] + [0]
ans = 0
state_set = set()
# 1번기차부터 나가기
for t in range(1, N+1):
    # 본 상태가 아니면,
    state = ''.join(map(str, trains[t]))
    print(state)
    if state not in state_set:
        ans += 1
        state_set.add(state)
print(ans)