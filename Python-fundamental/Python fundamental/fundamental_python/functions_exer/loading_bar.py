# def loading_bar(num):
#     str = ""
#     load = False
#     if loaded == 100:
#         print("100% Complete!")
#         load = True
#     num = num / 10
#     for i in range(10):
#         if num > 0:
#             str += "%"
#             num -= 1
#         else:
#             str += "."
#     str = "[" + str + "]"
#     if not load:
#         print(f"{loaded}% {str}")
#         print("Still loading...")
#     else:
#         print(str)
#     return
#
#
# loaded = int(input())
# loading_bar(loaded)

# def loading_bar(num):
#     ready = ("%" * int(num / 10))
#     remain = (".") * int(10 - num / 10)
#     bar = ready + remain
#     return bar
#
# loaded = int(input())
# if loaded == 100:
#     print(f"100% Complete!\n"
#           f"[{loading_bar(loaded)}]")
# else:
#     print(f"{loaded}% [{loading_bar(loaded)}]\n"
#           f"Still loading...")



def loading_bar(num):
    str = ""
    num = num / 10
    for i in range(10):
        if num > 0:
            str += "%"
            num -= 1
        else:
            str += "."
    return str


loaded = int(input())
loading_bar(loaded)
if loaded == 100:
    print(f"100% Complete!\n"
          f"[{loading_bar(loaded)}]")
else:
    print(f"{loaded}% [{loading_bar(loaded)}]\n"
          f"Still loading...")