# # version = [int(i) for i in input().split(".")]
# # for i in range(-1, len(version) - 1):
# #     if version[i] < 9:
# #         version[i] += 1
# #         break
# #     else:
# #         version[i] = 0
# #         version[i - 1] += 1
# #         break
# # for i in range(len(version)):
# #     print(version[i], end = "")
# #     if not i == len(version) - 1:
# #         print(".", end = "")
# #
# ver = list(map(lambda x: int(x), input().split(".")))
# for i in range(-1, len(ver) - 1):
#     if ver[i] < 9:
#         ver[i] += 1
#         break
#     else:
#         ver[i] = 0
#         ver[i + 1] += 1
#         if ver[i + 1] == 10:
#             ver[i + 1] = 0
#             ver[i + 2] += 1
#             break
#         break
# for i in range(len(ver)):
#      print(ver[i], end = "")
#      if not i == len(ver) - 1:
#          print(".", end = "")




version = [int(i) for i in input().split(".")]
for i in range(-1, len(version) - 1):
    if version[i] < 9:
        version[i] += 1
        break
    else:
        version[i] = 0
        version[i - 1] += 1
        if version[i - 1] == 10:
            version[i - 1] = 0
            version[i - 2] += 1
        break
for i in range(len(version)):
    print(version[i], end = "")
    if not i == len(version) - 1:
        print(".", end = "")




version.join(i for i in input().split("."))