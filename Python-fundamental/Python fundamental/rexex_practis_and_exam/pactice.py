# import re
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# names = input()
# full_name = re.findall(pattern, names)
# print(*full_name)


# import re
# pattern = r"\+359([ -])2(\1)\d{3}(\1)\d{4}"
# names = input()
# full_name = re.finditer(pattern, names)
# number = [i.group() for i in full_name]
# print(", ".join(number))


# import re
# pattern = r"(?P<day>\d{2})(?P<separator>[/.-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
# datas = input()
# date = re.finditer(pattern, datas)
# for i in date:
#     cur_data = i.groupdict()
#     print(f"Day: {cur_data['day']}, Month: {cur_data['month']}, Year: {cur_data['year']}")


# import re
# pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
#
# data = input()
#
# data_to_read = re.finditer(pattern, data)
# a = [i.group() for i in data_to_read]
# print(*a)



