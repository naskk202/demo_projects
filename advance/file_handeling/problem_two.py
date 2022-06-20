punctuation_marks = {'.', ',', '!', '?', ':', '"', '-', "'", ';', '_'}

with open("problem_two_content.txt", "r") as file, open("problem_two_solution.txt", "w") as solution:
    index = 1
    for line in file:
        letters = 0
        marks = 0
        for el in line:
            if el in punctuation_marks:
                marks += 1
            elif el.isalpha():
                letters += 1
        solution.write(f"Line {index}: {line.strip()} ({letters})({marks})\n")
        index += 1