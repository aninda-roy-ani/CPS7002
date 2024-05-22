class Payment:
    def __init__(self, payment_id, member, amount, payment_date, subscription_type, discount=None):
        self._payment_id = payment_id
        self._member = member
        self._amount = amount
        self._payment_date = payment_date
        self._subscription_type = subscription_type
        self._discount = discount if discount else 0

    def get_payment_id(self):
        return self._payment_id

    def set_payment_id(self, payment_id):
        self._payment_id = payment_id

    def get_member(self):
        return self._member

    def set_member(self, member):
        self._member = member

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_payment_date(self):
        return self._payment_date

    def set_payment_date(self, payment_date):
        self._payment_date = payment_date

    def calculate_total(self):
        return self._amount - self._discount
