class GymLocation:
    def __init__(self, gym_id, city, manager):
        self.gym_id = gym_id
        self.city = city
        self.manager = manager
        self.workout_zones = []
        self.members = []

    def add_workout_zone(self, zone):
        self.workout_zones.append(zone)

    def add_member(self, member):
        self.members.append(member)
