from week7.solid.library import Library


class Book(Library):

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)


