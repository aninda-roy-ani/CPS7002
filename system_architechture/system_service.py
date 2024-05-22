from system_architechture.gym_location import Gym
from system_architechture.management import Management
from system_architechture.member import Member



class SystemService:
    def __init__(self):
        self.management = Management()

    # Gym Management
    def add_gym(self, gym_id, gym_name, location, manager):
        gym = Gym(gym_id, gym_name, location, manager)
        self.management.add_gym(gym)

    def find_gym_by_id(self, gym_id):
        return self.management.find_gym_by_id(gym_id)

    def delete_gym(self, gym):
        self.management.delete_gym(gym)

    # Location Management
    def add_location_to_gym(self, gym_id, location_id, location_name, attendant):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            location = Location(location_id, location_name, attendant)
            gym.add_location(location)
            return True
        return False

    def find_location_by_id(self, gym_id, location_id):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            return gym.find_location_by_id(location_id)
        return None

    def delete_location_from_gym(self, gym_id, location_id):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            return gym.delete_location(location_id)
        return False

    # Member Management
    def add_member_to_gym(self, gym_id, member_id, name, membership_type, personal_details, health_info):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            member = Member(member_id, name, membership_type, personal_details, health_info)
            gym.add_member(member)
            return True
        return False

    def find_member_by_id(self, gym_id, member_id):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            return gym.find_member_by_id(member_id)
        return None

    def delete_member_from_gym(self, gym_id, member_id):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            return gym.delete_member(member_id)
        return False

    # Appointment Management
    def schedule_appointment(self, gym_id, appointment_id, member_id, appointment_type, date_time):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            appointment = Appointment(appointment_id, member_id, appointment_type, date_time)
            gym.schedule_appointment(appointment)
            return True
        return False

    def cancel_appointment(self, gym_id, appointment_id):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            return gym.cancel_appointment(appointment_id)
        return False

    # Payment Management
    def make_payment(self, gym_id, payment_id, member_id, amount, payment_method, date_time):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            payment = Payment(payment_id, member_id, amount, payment_method, date_time)
            gym.make_payment(payment)
            return True
        return False

    def view_payment_history(self, gym_id, member_id):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            return gym.view_payment_history(member_id)
        return None

    # Management Dashboard
    def generate_reports(self, gym_id):
        gym = self.find_gym_by_id(gym_id)
        if gym:
            return gym.generate_reports()
        return None
