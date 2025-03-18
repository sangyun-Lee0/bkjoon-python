X = int(input())
line = 1 #대각선 개수

while X > line: #위치 보기
    X -= line
    line += 1

if line %2 == 1:
    numerator = line-X+1
    denominator = X
else:
    numerator = X
    denominator = line-X+1

print(f"{numerator}/{denominator}")
