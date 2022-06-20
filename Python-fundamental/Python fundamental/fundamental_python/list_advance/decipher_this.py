# def replace_char(word):
#     lis_code = []
#     first_letter = ""
#     for ch in word:
#         if ch.isnumeric():
#             first_letter += ch
#         else:
#             lis_code.append(ch)
#     first_el = lis_code.pop(0)
#     if lis_code:
#         second_el = lis_code.pop(-1)
#         lis_code.insert(0, second_el)
#         lis_code.append(first_el)
#     else:
#         lis_code.append(first_el)
#     code = "".join(i for i in lis_code)
#     new_code = chr(int(first_letter)) + code
#     return new_code
#
#
# text = [i for i in input().split()]
# decipher = [replace_char(decode) for decode in text]
# for i in decipher:
#     print(i, end=" ")





def replace_first_char(word):
    code = []
    first_letter = ""
    for ch in word:
        if ch.isnumeric():
            first_letter += ch
        else:
            code += ch
    code.insert(0, chr(int(first_letter)))
    return code

def decipher_word(word):
    new_word = replace_first_char(word)
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    return "".join(new_word)


text = [i for i in input().split()]
decipher = [decipher_word(decode) for decode in text]
print(" ".join(decipher))
