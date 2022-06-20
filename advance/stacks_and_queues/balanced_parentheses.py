pattern = input()
example = {
    "[": "]",
    "{": "}",
    "(": ")"
}
stack = []
it_work = True
for i in pattern:
    if i in example.keys():
        stack.append(i)
    else:
        if len(stack) == 0:
            it_work = False
            break
        last_opening_bracket = stack.pop()
        if example[last_opening_bracket] != i:
            it_work = False
            break
if it_work and len(stack) == 0:
    print("YES")
else:
    print("NO")
