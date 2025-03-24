from datetime import datetime


class User:
    username: str
    firstname: str
    lastname: str
    emailaddress: str
    mobilenumber: str
    dob: datetime.date
    age: int

    def __init__(self):
        self.get_age()

    def to_dict(self):
        return self.__dict__

    def from_dict(self, data):
        self.__dict__.update(data)
        return self

    def get_age(self):
        self.age = datetime.today - datetime(self.dob)
