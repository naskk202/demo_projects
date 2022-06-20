import re

text = input()

pattern = r"www\.[A-Z\da-z\-\.]+\.[a-z]+"
while text:
    e_mails = re.finditer(pattern, text)
    for i in e_mails:
        print(i.group())
    text = input()