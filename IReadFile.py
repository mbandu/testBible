from abc import ABC, abstractmethod

class IReadFile(ABC):
    @abstractmethod
    def read(self):
        pass

