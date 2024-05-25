
class Member:
    def __init__(self, member_id, name, age, height, weight, plan):
        self.__id = member_id
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__plan = plan
        self.__appointments = []

    def get_id(self):
        return self.__id

    def set_id(self, member_id):
        self.__id = member_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_plan(self):
        return self.__plan

    def set_plan(self, plan):
        self.__plan = plan

    def add_appointment(self, appointment):
        self.__appointments.append(appointment)

    def cancel_appointment(self, appointment_type, date):
        self.__appointments = [appt for appt in self.__appointments if not (appt.get_type() == appointment_type and appt.get_date() == date)]

    def list_appointments(self):
        return self.__appointments

    def update_membership_status(self, new_plan):
        self.__plan = new_plan
