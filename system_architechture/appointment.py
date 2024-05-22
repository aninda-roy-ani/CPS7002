class Appointment:
    def __init__(self, appointment_id, member, trainer, date, time, type_of_session):
        self._appointment_id = appointment_id
        self._member = member
        self._trainer = trainer
        self._date = date
        self._time = time
        self._type_of_session = type_of_session

    def get_appointment_id(self):
        return self._appointment_id

    def set_appointment_id(self, appointment_id):
        self._appointment_id = appointment_id

    def get_member(self):
        return self._member

    def set_member(self, member):
        self._member = member

    def get_trainer(self):
        return self._trainer

    def set_trainer(self, trainer):
        self._trainer = trainer

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def get_type_of_session(self):
        return self._type_of_session

    def set_type_of_session(self, type_of_session):
        self._type_of_session = type_of_session
