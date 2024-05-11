age_lily = int(input())
price_washing_machine = float(input())
singular_price_toy = int(input())

num_toys = 0
sum_money = 0
counter_money = 0
money_take_brother = 1
quantity_money_take_brother = 0
total_save_money = 0
sell_toys = 0
leave_money = 0
counter_take_money_brother = 0

SAVE_MONEY = 10

for birthday_lily in range(1, age_lily + 1):
    if birthday_lily % 2 == 0:
        sum_money += SAVE_MONEY
        counter_money += sum_money
        counter_take_money_brother += 1
    else:
        num_toys += 1

sell_toys = num_toys * singular_price_toy
quantity_money_take_brother = counter_take_money_brother * money_take_brother
total_save_money = (counter_money + sell_toys) - quantity_money_take_brother
leave_money = abs(total_save_money - price_washing_machine)

if total_save_money >= price_washing_machine:
    print(f"Yes! {leave_money:.2f}")
else:
    print(f"No! {leave_money:.2f}")
