num_open_tab = int(input())
salary = int(input())

for i in range(1, num_open_tab+1):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        exit()

else:
    print(salary)
