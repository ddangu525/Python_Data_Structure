N = int(input())
signal = input()
bins = N // 5

reshaped = []
for i in range(0, N - bins+1, bins):
    row = list(signal[i:i + bins])
    reshaped.append(row)
print('\n'.join(map(str, reshaped)))

ans = ''
x = 0
while x < bins:
    # 숫자를 찾은경우
    if reshaped[0][x] == '#':
        # 0~9 까지 숫자 빡코딩..

        # 0, 1, 6, 8 먼저 찾아보자. 맨 왼쪽 줄이 모두 '#'인경우.
        if reshaped[1][x] == reshaped[2][x] == reshaped[3][x] == reshaped[4][x] == '#':
            # 1 찾기
            if x+1==bins or reshaped[0][x + 1] == '.':
                ans += '1'
                x += 2
            # 0 찾기
            elif reshaped[2][x + 1] == '.':
                ans += '0'
                x += 4
            # 6 찾기
            elif reshaped[1][x + 2] == '.':
                ans += '6'
                x += 4
            # 나머지 하나는 8인경우.
            else:
                ans += '8'
                x += 4

        # 남은애들은, 2, 3, 4, 5, 7, 9
        # 2, 3, 5, 9 찾기. 맨 아래줄이 모두 '#'인경우.
        elif reshaped[4][x] == reshaped[4][x + 1] == reshaped[4][x + 2] == '#':
            # 2 찾기
            if reshaped[3][x + 2] == '.':
                ans += '2'
            # 3 찾기
            elif reshaped[1][x] == '.':
                ans += '3'
            # 5 찾기
            elif reshaped[1][x + 2] == '.':
                ans += '5'
            else:
                ans += '9'
            x += 4

        # 남은건 4, 7
        else:
            # 4 찾기
            if reshaped[0][x + 1] == '.':
                ans += '4'
            else:
                ans += '7'
            x += 4
    # 아니면 한칸만 오른쪽으로..
    else:
        x += 1

print(ans)