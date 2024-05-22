class GymManager:
    def __init__(self, manager_id, name):
        self._manager_id = manager_id
        self._name = name

    def get_manager_id(self):
        return self._manager_id

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_daily_operations_report(self, gym):
        report = {
            'membership_growth': gym.get_membership_growth(),
            'revenue_trends': gym.get_revenue_trends(),
            'trainer_schedules': gym.get_trainer_schedules(),
            'equipment_maintenance': gym.get_equipment_maintenance()
        }
        return report
