class Attendance:
    def __init__(self, attendance_id, member, date, class_attended=None):
        self._attendance_id = attendance_id
        self._member = member
        self._date = date
        self._class_attended = class_attended

    def get_attendance_id(self):
        return self._attendance_id

    def set_attendance_id(self, attendance_id):
        self._attendance_id = attendance_id

    def get_member(self):
        return self._member

    def set_member(self, member):
        self._member = member

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_class_attended(self):
        return self._class_attended

    def set_class_attended(self, class_attended):
        self._class_attended = class_attended
