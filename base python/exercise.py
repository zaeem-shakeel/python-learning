# # true value means 3 to 16 code run

# st = input("enter  message :")
# words = st.split(" ")
# coding = True  # True means code exist to 1 to 16 and Flse means code exists to 18 to 23
# if coding:
#     nwords =[]
#     for word in words:
#         if len(word) >= 3:
#             r1 = "dsf"
#             r2 = "jkr"
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))
# else:
#     nwords = []
#     for word in words:
#         stnew = word[3:-3]
#         stnew = stnew[-1] + stnew[:-1]
#         nwords.append(stnew)
#     print(" ".join(nwords))




#Libery Mangent

class Library:
    def __init__(self):
        self.no_of_books = 0 
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def get_books(self):
        return self.books

    def get_no_of_books(self):
        return self.no_of_books

    def print_books(self):
        if self.no_of_books == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

# Create a Library object
library = Library()

# Add books to the library
library.add_book("The Great Gatsby")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")

# Print all books in the library
library.print_books()

# Get the number of books in the library
print(f"Total number of books: {library.get_no_of_books()}")


