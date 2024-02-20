
class LibraryCatalogue:
    library_name = "DontKnow"
    next_book_id = 2000

    def __init__(self, title, author, genre):
        self.id = self.next_book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = True
        self.next_book_id += 1

