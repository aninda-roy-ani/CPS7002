from week7.solid.library import Library


class Transaction(Library):

    def lend_book(self, book, patron):
        if book in self.books and patron in self.patrons:
            self.transactions.append((book, patron))
            self.books.remove(book)
            return True
        else:
            return False

    def return_book(self, book):
        for transaction in self.transactions:
            if transaction[0] == book:
                self.books.append(book)
                self.transactions.remove(transaction)
                return True
        return False