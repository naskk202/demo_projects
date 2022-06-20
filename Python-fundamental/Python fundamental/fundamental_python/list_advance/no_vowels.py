text = input()
vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
pr_text = "".join([i for i in text if i not in vowels])
print(pr_text)