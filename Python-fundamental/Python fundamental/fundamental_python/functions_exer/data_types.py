def data_type(type, data):
    if type == "int":
        result = int(data) * 2
    elif type == "real":
        result = f"{float(data) * 1.5:.2f}"
    else:
        result = "$" + data + "$"
    return result


type = input()
data = input()
print(data_type(type, data))