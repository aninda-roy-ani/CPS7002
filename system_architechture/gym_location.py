class Gym:
    def __init__(self, gym_id, name, location, manager):
        self._gym_id = gym_id
        self._name = name
        self._location = location
        self._manager = manager
        self._workout_zones = []
        self._members = []
        self._payments = []

    def get_gym_id(self):
        return self._gym_id

    def set_gym_id(self, gym_id):
        self._gym_id = gym_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_manager(self):
        return self._manager

    def set_manager(self, manager):
        self._manager = manager

    def get_workout_zones(self):
        return self._workout_zones

    def get_members(self):
        return self._members

    def get_payments(self):
        return self._payments

    def add_workout_zone(self, zone):
        self._workout_zones.append(zone)

    def add_member(self, member):
        self._members.append(member)

    def add_payment(self, payment):
        self._payments.append(payment)

    def get_membership_growth(self):
        return len(self._members)

    def get_revenue_trends(self):
        return sum(payment.amount for payment in self._payments)

    def get_trainer_schedules(self):
        schedules = {}
        for member in self._members:
            for appointment in member.appointments:
                if appointment.trainer not in schedules:
                    schedules[appointment.trainer] = []
                schedules[appointment.trainer].append(appointment)
        return schedules

    def get_equipment_maintenance(self):
        maintenance = {}
        for zone in self._workout_zones:
            maintenance[zone.name] = zone.attendant
        return maintenance
