def correct_password(pas):
    digit = 0
    bad_char = 0
    its_ok = True
    if not 5 < len(pas) < 11:
        print("Password must be between 6 and 10 characters")
        its_ok = False
    for i in pas:
        if 47 < ord(i) < 58:
            digit += 1
        if not 47 < ord(i) < 58 and not 64 < ord(i) < 91 and not 96 < ord(i) < 123:
            bad_char += 1
    if bad_char > 0:
        print("Password must consist only of letters and digits")
        its_ok = False
    if not digit > 1:
        print("Password must have at least 2 digits")
        its_ok = False
    if its_ok:
        print("Password is valid")
    return


password = input()
correct_password(password)