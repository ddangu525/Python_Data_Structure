N, M = map(int, input().split())
# 빈 좌석 20개짜리 기차 N개.. 1은 아무도 안타있는 상태. 2^0
trains = [1] * (N + 1)
tot = 2**21 - 1
# 명령받아서 수행하기..
for _ in range(M):
    *order, = map(int, input().split())
    # 태우기 명령. order[1]번째 기차에 order[2]번째 좌석에 태우기.
    if order[0]==1:
        trains[order[1]] |= 1<<order[2]
    # 내리기 명령.. 태우기 처럼 쉽게 안되나??
    elif order[0]==2:
        # 그 칸에 사람이 있으면.. 없으면 그냥 놔두기.
        if trains[order[1]] & 1<<order[2]:
            trains[order[1]] -= 1<<order[2]
    # 한칸씩 뒤로(20번째는 내려짐) order[1]번째 기차 한칸씩 뒤로..
    elif order[0]==3:
        trains[order[1]] = ((trains[order[1]]<<1)&tot) - 1
    # 한칸씩 앞으로(1번째는 내려짐)
    else:
        trains[order[1]] = ((trains[order[1]]>>1)&tot)|1
print(len(set(trains)))