from abc import ABC, abstractmethod


class IUser(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def delete(self):
        pass
