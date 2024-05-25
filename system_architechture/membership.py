
class Membership:
    def __init__(self, subscription_plan, start_date, end_date):
        self.__subscription_plan = subscription_plan
        self.__start_date = start_date
        self.__end_date = end_date

    def get_subscription_plan(self):
        return self.__subscription_plan

    def set_subscription_plan(self, subscription_plan):
        self.__subscription_plan = subscription_plan

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def calculate_fee(self):
        # Dummy calculation based on the subscription plan
        if self.__subscription_plan == "monthly":
            return 30
        elif self.__subscription_plan == "quarterly":
            return 80
        elif self.__subscription_plan == "annual":
            return 300
        else:
            return 0

    def apply_discount(self, discount):
        fee = self.calculate_fee()
        return fee - (fee * discount / 100)
