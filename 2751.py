import sys

N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

"""for i in range(len(num_list)-1):
    for j in range(i+1,len(num_list)):
        if num_list[i] > num_list[j]:
            temp = num_list[j]
            num_list[j] = num_list[i]
            num_list[i] = temp"""

for k in num_list:
    print(k)
