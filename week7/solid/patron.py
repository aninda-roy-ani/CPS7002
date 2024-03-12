from week7.solid.library import Library


class Patron(Library):

    def add_patron(self, patron):
        self.patrons.append(patron)

    def remove_patron(self, patron):
        self.patrons.remove(patron)