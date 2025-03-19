while True:
    a = int(input())
    if a == (-1):
        break
    else:
        divisor = []
        for i in range(1, a//2+1):
            if a % i != 0:
                continue
            else:
                divisor.append(i)

        if a == sum(divisor):
            print(a, '=', ' + '.join(map(str,divisor)))
        else:
            print(a, 'is NOT perfect.')


