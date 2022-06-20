command = input()
results_course = {}
results_points = {}

while not command == "exam finished":
    if "ban" in command:
        banned = command.split("-")
        results_points.pop(banned[0])
    else:
        name, course, points = command.split("-")
        points = int(points)
        if course not in results_course:
            results_course[course] = []
        results_course[course].append(name)
        if name not in results_points:
            results_points[name] = 0
        if points > results_points[name]:
            results_points[name] = points
    command = input()
sorted_results = sorted(results_points.items(), key=lambda x: (-x[1], x[0]))
sorted_class = sorted(results_course.items(), key=lambda x: (-len(x[1]), x[0]))
print("Results:")
for k, v in sorted_results:
    print(f"{k} | {v}")
print("Submissions:")
for k, v in sorted_class:
    print(f"{k} - {len(v)}")