name_actor = input()
point_academy = float(input())
num_assessors = int(input())

total_points = 0.0
points_first_actor = 0.0
leave_points = 0.0

points_new_actor = point_academy

VALUE_NOMINATION = 1250.5


for i in range(num_assessors):
    name = input()
    total_points = 0.0
    rater_points = float(input())
    total_points += points_new_actor + ((len(name) * rater_points)/2)
    points_new_actor = total_points
    if total_points > VALUE_NOMINATION:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    leave_points = abs(total_points-VALUE_NOMINATION)
    print(f"Sorry, {name_actor} you need {leave_points:.1f} more!")
