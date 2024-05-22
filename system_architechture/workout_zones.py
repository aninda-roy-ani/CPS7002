class WorkoutZone:
    def __init__(self, zone_id, name, equipment, attendant):
        self._zone_id = zone_id
        self._name = name
        self._equipment = equipment
        self._attendant = attendant
        self._updates = []
        self._class_schedules = []

    def get_zone_id(self):
        return self._zone_id

    def set_zone_id(self, zone_id):
        self._zone_id = zone_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_equipment(self):
        return self._equipment

    def set_equipment(self, equipment):
        self._equipment = equipment

    def get_attendant(self):
        return self._attendant

    def set_attendant(self, attendant):
        self._attendant = attendant

    def get_updates(self):
        return self._updates

    def get_class_schedules(self):
        return self._class_schedules

    def add_update(self, update):
        self._updates.append(update)

    def add_class_schedule(self, class_schedule):
        self._class_schedules.append(class_schedule)

