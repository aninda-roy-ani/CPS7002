class Management:
    def __init__(self):
        self.gyms = []

    def get_gyms(self):
        return self.gyms

    def add_gym(self, gym):
        self.gyms.append(gym)

    def find_gym_by_id(self, gym_id):
        pass