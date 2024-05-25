
class WorkoutZone:
    def __init__(self, zone_id, name, attendant):
        self.__id = zone_id
        self.__name = name
        self.__attendant = attendant
        self.__equipments = []
        self.__schedule = []

    def get_id(self):
        return self.__id

    def set_id(self, zone_id):
        self.__id = zone_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_attendant(self):
        return self.__attendant

    def set_attendant(self, attendant):
        self.__attendant = attendant

    def add_schedule(self, schedule):
        self.__schedule.append(schedule)

    def remove_schedule(self, day):
        self.__schedule = [s for s in self.__schedule if s.get_day() != day]

    def list_schedule(self):
        return self.__schedule

    def communicate_update(self, message):
        # Implement communication logic (e.g., email, app notification)
        print(f"Update for {self.__name}: {message}")

    def communicate_promotion(self, message):
        # Implement promotion communication logic
        print(f"Promotion for {self.__name}: {message}")
