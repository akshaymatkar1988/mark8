from abc import ABC, abstractmethod


class IMessageQueueing(ABC):

    @abstractmethod
    def connect():
        pass

    @abstractmethod
    def disconnect():
        pass

    @abstractmethod
    def queue():
        pass

    @abstractmethod
    def dequeue():
        pass
