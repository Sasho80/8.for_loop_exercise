num_group_climber = int(input())

total_num_people = 0
percent_musala = 0
percent_monblant = 0
percent_klimandjaro = 0
percent_k2 = 0
percent_everest = 0
num_musala = 0
num_monblant = 0
num_klimandjaro = 0
num_k2 = 0
num_everest = 0

for i in range(num_group_climber):
    num_people_group = int(input())
    total_num_people += num_people_group
    if num_people_group <= 5:
        num_musala += num_people_group
    elif 12 >= num_people_group >= 6:
        num_monblant += num_people_group
    elif 25 >= num_people_group >= 13:
        num_klimandjaro += num_people_group
    elif 26 <= num_people_group <= 40:
        num_k2 += num_people_group
    elif 41 <= num_people_group:
        num_everest += num_people_group

percent_musala = (num_musala / total_num_people) * 100
percent_monblant = (num_monblant/total_num_people) * 100
percent_klimandjaro = (num_klimandjaro/total_num_people) * 100
percent_k2 = (num_k2/total_num_people) * 100
percent_everest = (num_everest/total_num_people) * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblant:.2f}%")
print(f"{percent_klimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
