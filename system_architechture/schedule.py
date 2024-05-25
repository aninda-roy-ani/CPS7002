
class Schedule:
    def __init__(self, day, start_time, end_time):
        self.__day = day
        self.__start_time = start_time
        self.__end_time = end_time

    def get_day(self):
        return self.__day

    def set_day(self, day):
        self.__day = day

    def get_start_time(self):
        return self.__start_time

    def set_start_time(self, start_time):
        self.__start_time = start_time

    def get_end_time(self):
        return self.__end_time

    def set_end_time(self, end_time):
        self.__end_time = end_time
