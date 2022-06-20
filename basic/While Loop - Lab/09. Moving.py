book = input()
books = 0
search = input()
while search != book:
    if search == "No More Books":
        print(f"The book you search is not here!\n"
              f"You checked {books} books.")
        break
    books += 1
    search = input()
    if book == search:
        print(f"You checked {books} books and found it.")
if book == search and books == 0:
    print(f"You checked {books} books and found it.")