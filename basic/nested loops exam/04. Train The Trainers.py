judges = int(input())
presentation_name = input()
all = 0
exams = 0
while presentation_name != "Finish":
    sum = 0
    for evaluations in range(judges):
        evaluation = float(input())
        sum += evaluation
        all += evaluation
        exams += 1
    print(f"\n{presentation_name} - {sum / judges:.2f}.")
    presentation_name = input()
print(f"Student's final assessment is {all / exams:.2f}.")