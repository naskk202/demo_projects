text = input()
rev_text = ""
for a in range(len(text) -1, -1, -1):
    rev_text += text[a]
print(rev_text)




print(text[::-1])