from abc import ABC, abstractmethod


class INotification(ABC):

    @abstractmethod
    def notify():
        pass
