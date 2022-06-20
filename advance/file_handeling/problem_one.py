marks = {"-", ",", ".", "!", "?"}

with open("problem_one_content.txt", "r") as file:
    counter = 0
    content = file.read()
    for el in content:
        if el in marks:
            content = content.replace(el, "@")
    for row in content.split("\n"):
        if counter % 2 == 0:
            print(" ".join(row.split()[::-1]))
        counter += 1