from itertools import permutations
N = int(input())
*A, = map(int, input().split())          # 수열.
add, sub, mul, div = map(int, input().split())     # +, -, x, / 연산자 수.
operations = '+'*add + '-'*sub + '*'*mul + '/'*div
cases = set(permutations(operations))   # tuple로 저장..
# 최대, 최소값 초기화
max_val = float('-inf')
min_val = float('inf')
for case in cases:
    val = A[0]
    for idx, op in enumerate(case, 1):
        if op=='+':
            val += A[idx]
        elif op=='-':
            val -= A[idx]
        elif op=='*':
            val *= A[idx]
        else:
            if val>0:
                val //= A[idx]
            else:
                val = -val
                val //= A[idx]
                val = -val
    if val>max_val:
        max_val = val
    if val<min_val:
        min_val = val
print(max_val, min_val, sep='\n')