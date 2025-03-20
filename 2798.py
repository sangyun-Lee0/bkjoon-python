N, M = map(int, input().split())
num_list = list(map(int, input().split()))

three_num = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = num_list[i] + num_list[j] + num_list[k]
            if sum <= M:
                three_num.append(sum)

print(max(three_num))

