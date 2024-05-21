class WorkoutZone:
    def __init__(self, zone_id, type_of_exercise, attendant):
        self.zone_id = zone_id
        self.type_of_exercise = type_of_exercise
        self.attendant = attendant
        self.updates = []

    def add_update(self, update):
        self.updates.append(update)
