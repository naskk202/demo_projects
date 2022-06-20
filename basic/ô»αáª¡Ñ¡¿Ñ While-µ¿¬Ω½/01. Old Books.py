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






book = input()
books = 0
is_book_found = False
current_book = input()
while current_book != "No More Books":
    if current_book == book:
        is_book_found = True
        print(f"You checked {books} books and found it.")
        break
    books += 1
    current_book = input()
if not is_book_found:
    print(f"The book you search is not here!\n"
          f"You checked {books} books.")