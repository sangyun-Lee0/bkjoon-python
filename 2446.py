N = int(input())
for i in range(N):
    print(' '*i+'*'*(2*N-1-2*i))
for i in range(N-1):
    print(' '*(N-2-i)+'*'*(2*i+3))