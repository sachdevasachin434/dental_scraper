from abc import ABC, abstractmethod

class NotifierInterface(ABC):
    @abstractmethod
    def notify(self, data):
        pass
