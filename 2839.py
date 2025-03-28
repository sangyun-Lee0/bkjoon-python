N = int(input())
num = 0

while N>=0:
    if N%5 == 0:
        num += (N//5)
        break
    N -= 3
    num +=1

if N <0:
    print(-1)
else:
    print(num)

