
class Gym:
    def __init__(self, gym_id, name, location, manager):
        self.__id = gym_id
        self.__name = name
        self.__location = location
        self.__manager = manager
        self.__workout_zones = []
        self.__members = []

    def get_id(self):
        return self.__id

    def set_id(self, gym_id):
        self.__id = gym_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_manager(self):
        return self.__manager

    def set_manager(self, manager):
        self.__manager = manager

    def add_workout_zone(self, zone):
        self.__workout_zones.append(zone)

    def remove_workout_zone(self, zone_id):
        self.__workout_zones = [zone for zone in self.__workout_zones if zone.get_id() != zone_id]

    def list_workout_zones(self):
        return self.__workout_zones

    def add_member(self, member):
        self.__members.append(member)

    def remove_member(self, member_id):
        self.__members = [member for member in self.__members if member.get_id() != member_id]

    def list_members(self):
        return self.__members
