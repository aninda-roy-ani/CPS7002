import csv
import os

class User:
    def __init__(self, username, password, user_type):
        self.__username = username
        self.__password = password
        self.__user_type = user_type

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_user_type(self):
        return self.__user_type

    def to_dict(self):
        return {
            'username': self.__username,
            'password': self.__password,
            'user_type': self.__user_type
        }

    @staticmethod
    def from_dict(data):
        return User(data['username'], data['password'], data['user_type'])

    @staticmethod
    def load_users(file_path='users.csv'):
        users = {}
        if os.path.exists(file_path):
            with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User.from_dict(row)
                    users[user.get_username()] = user
        return users

    @staticmethod
    def save_users(users, file_path='users.csv'):
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['username', 'password', 'user_type']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users.values():
                writer.writerow(user.to_dict())
