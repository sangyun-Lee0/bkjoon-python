import sys
from collections import deque

queue = deque()
N = int(input())
for _ in range(N):
    comment = list(sys.stdin.readline().split())
    if comment[0] == 'push':
        queue.append(comment[1])
    elif comment[0] == 'pop':
        if not queue:
            print(-1)
        else: 
            print(queue.popleft())
    elif comment[0] == 'size':
        print(len(queue))
    elif comment[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif comment[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif comment[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])