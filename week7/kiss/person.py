class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def set_contact_info(self, address=None, email=None, phone=None):
        self.address = address
        self.email = email
        self.phone = phone

    def get_information(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id}"
