class Member:
    def __init__(self, member_id, name, membership_type, personal_details, health_info):
        self._member_id = member_id
        self._name = name
        self._membership_type = membership_type
        self._personal_details = personal_details
        self._health_info = health_info
        self._appointments = []
        self._attendance_records = []

    def get_member_id(self):
        return self._member_id

    def set_member_id(self, member_id):
        self._member_id = member_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_membership_type(self):
        return self._membership_type

    def set_membership_type(self, membership_type):
        self._membership_type = membership_type

    def get_personal_details(self):
        return self._personal_details

    def set_personal_details(self, personal_details):
        self._personal_details = personal_details

    def get_health_info(self):
        return self._health_info

    def set_health_info(self, health_info):
        self._health_info = health_info

    def get_appointments(self):
        return self._appointments

    def get_attendance_records(self):
        return self._attendance_records

    def add_appointment(self, appointment):
        self._appointments.append(appointment)

    def cancel_appointment(self, appointment_id):
        self._appointments = [apt for apt in self._appointments if apt.get_appointment_id() != appointment_id]

    def add_attendance_record(self, record):
        self._attendance_records.append(record)
