class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = len(self.books)

    def show_books(self):
        return self.books
    
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"{book_name} added to the library!")
        self.no_of_books += 1 
    
    def how_many_books(self):
        return self.no_of_books
    
if __name__ == "__main__":
    print("Welcome to the library!")
    lib1 = Library()

    while True:
        print("\nOptions:\n1.Show all books\n2.Add a book\n3.How many books?\n4.Exit")
        user_input = input("Choose an option: ")

        match user_input:
            case "1":
                book_list = lib1.show_books()
                if book_list == []:
                    print("\nNo books yet!")
                else:
                    for book in book_list:
                        print(book)
            case "2":
                book_name = input("Enter the name of the book: ")
                lib1.add_book(book_name)
            case "3":
                number_of_books = lib1.how_many_books()
                if number_of_books != len(lib1.show_books()):
                    print("Book count not matching.")
                print(f"Library has {number_of_books} books!")
            case "4":
                break
            case _:
                print("Invalid input!")