def is_valid(indexes: int, text):
    if 0 <= int(indexes) < len(text):
        return True
    return False


def exchange(indexes: int, text):
    if is_valid(indexes, text):
        new_text = text[indexes + 1:] + text[:indexes + 1]
        return new_text
    else:
        print("Invalid index")
        return text


def max_min_even_odd(text, num, mm):
    new_lis = ev_odd(text, num)
    if not new_lis:
        return "No matches"
    if mm == "max":
        number = len(text) - text[::-1].index(max(new_lis)) - 1
    else:
        number = len(text) - text[::-1].index(min(new_lis)) - 1
    return number


def ev_odd(text, ev_odd):
    if ev_odd == "even":
        return [i for i in text if i % 2 == 0]
    else:
        return [i for i in text if not i % 2 == 0]


def counter(text, numbers, ev_od, first_last):
    new_lis = ev_odd(text, ev_od)
    if is_valid(int(numbers) - 1, text):
        if len(new_lis) > int(numbers):
            if first_last == "first":
                return [new_lis[i] for i in range(int(numbers))]
            else:
                rev_new_list = new_lis[::-1]
                rev_new_list = [rev_new_list[i] for i in range(int(numbers))]
                return rev_new_list[::-1]
        else:
            return new_lis
    else:
        return "Invalid count"


nums = [int(i) for i in input().split()]
command = input()
new_lis = 0
while not command == "end":
    command = command.split()
    if "exchange" in command:
        nums = exchange(int(command[1]), nums)
        command = input()
        continue
    elif "max" in command or "min" in command:
        new_lis = max_min_even_odd(nums, command[1], command[0])
    elif "first" in command or "last" in command:
        new_lis = counter(nums, command[1], command[2], command[0])
    print(new_lis)
    command = input()
print(nums)
