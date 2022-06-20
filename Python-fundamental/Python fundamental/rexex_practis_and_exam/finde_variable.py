import re

pattern = r"((?<= _)[A-Z\da-z]+\b)"

data = input()

data_to_print = re.findall(pattern, data)

print(",".join(data_to_print))