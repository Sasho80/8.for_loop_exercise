num = int(input())

counter_200 = 0
counter_200_399 = 0
counter_400_599 = 0
counter_600_799 = 0
counter_800 = 0

for i in range(1, num+1):
    n = int(input())
    if n < 200:
        counter_200 += 1
    elif 399 >= n >= 200:
        counter_200_399 += 1
    elif 599 >= n >= 400:
        counter_400_599 += 1
    elif 799 >= n >= 600:
        counter_600_799 += 1
    else:
        counter_800 += 1

print(f"{(counter_200/ num) * 100: .2f}%")
print(f"{(counter_200_399 / num) * 100: .2f}%")
print(f"{(counter_400_599 / num) * 100: .2f}%")
print(f"{(counter_600_799 / num) * 100: .2f}%")
print(f"{(counter_800     / num) * 100: .2f}%")
