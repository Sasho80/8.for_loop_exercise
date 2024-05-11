import sys

num = int(input())
max_num = -sys.maxsize
sum_num = 0
diff = 0

for i in range(1, num+1):
    n = int(input())
    sum_num += n
    if max_num < n:
        max_num = n
if max_num == sum_num - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    sum_num = sum_num - max_num
    diff = abs(max_num-sum_num)
    print("No")
    print(f"Diff = {diff}")
