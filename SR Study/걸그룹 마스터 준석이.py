import sys
input = sys.stdin.readline
N, M = map(int, input().split())
info = {}
for _ in range(N):
    group_name = input().rstrip()
    num = int(input())
    names = sorted(input().rstrip() for _ in range(num))
    info[group_name] = names
for _ in range(M):
    name = input().rstrip()
    q = int(input())
    # 1번 종류 문제. 멤버가 속한 팀의 이름 출력.
    if q:
        for k, v in info.items():
            if name in v:
                print(k)
                break
    # 0번 문제.. 사전순 출력.
    else:
        print('\n'.join(info[name]))