
class Appointment:
    def __init__(self, appointment_type, date, time):
        self.__type = appointment_type
        self.__date = date
        self.__time = time

    def get_type(self):
        return self.__type

    def set_type(self, appointment_type):
        self.__type = appointment_type

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time
