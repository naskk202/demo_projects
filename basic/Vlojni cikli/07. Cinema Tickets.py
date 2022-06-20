movie_name = input()
standard = 0
student = 0
kid = 0
while movie_name != "Finish":
    seats = int(input())
    ticket = input()
    ticket_counter = 0
    while ticket != "End":
        if ticket == "Finish":
            break
        elif ticket == "standard":
            standard += 1
        elif ticket == "student":
            student += 1
        else:
            kid += 1
        ticket_counter += 1
        if seats > ticket_counter:
            ticket = input()
        else:
            break
    print(f"\n{movie_name} - {(ticket_counter / seats) * 100:.2f}% full.")
    if ticket == "Finish":
        break
    movie_name = input()
sum = student + standard + kid
print(f"Total tickets: {sum}\n"
      f"{(student / sum) * 100:.2f}% student tickets.\n"
      f"{(standard / sum) * 100:.2f}% standard tickets.\n"
      f"{(kid / sum) * 100:.2f}% kids tickets.")