import sys
sys.setrecursionlimit(10**5)
X, Y, M = map(int, input().split())
max_size = float('-inf')
def pour(pail=None, tot = 0):
    global max_size
    if tot>M:
        if tot-pail > max_size:
            max_size = tot-pail
        return
    pour(X, tot+X)
    pour(Y, tot+Y)
pour()
print(max_size)