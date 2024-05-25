
class Management:
    def __init__(self):
        self.__gyms = []

    def add_gym(self, gym):
        self.__gyms.append(gym)

    def remove_gym(self, gym_id):
        self.__gyms = [gym for gym in self.__gyms if gym.get_id() != gym_id]

    def list_gyms(self):
        return self.__gyms
