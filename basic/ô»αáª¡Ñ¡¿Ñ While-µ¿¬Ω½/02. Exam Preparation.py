max_fails = int(input())
fail = 0
grades = 0
tests = 0
last_task = ""
finish = False
while fail < max_fails:
    task = input()
    if task == "Enough":
        finish = True
        break
    evaluation = int(input())
    if evaluation <= 4:
        fail += 1
    grades += evaluation
    tests += 1
    last_task = task
if finish:
    print(f"Average score: {grades / tests:.2f}\n"
          f"Number of problems: {tests}\n"
          f"Last problem: {last_task}")
else:
    print(f"You need a break, {fail} poor grades.")