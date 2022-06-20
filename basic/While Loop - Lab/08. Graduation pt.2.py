name = input()
sum_evaluation = 0
chances = 1
for graduation in range(12):
	evaluation = float(input())
	if evaluation < 4:
		chances -= 1
	else:
		sum_evaluation += evaluation
	if chances < 0:
		print(f"{name} has been excluded at {graduation} grade")
		break
	if graduation == 11:
		print(f"{name} graduated. Average grade: {sum_evaluation / 12:.2f}")
