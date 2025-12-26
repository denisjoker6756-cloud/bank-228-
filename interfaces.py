from abc import ABC, abstractmethod

# Патерн Observer: Інтерфейс для тих, хто отримує сповіщення
class IObserver(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Інтерфейс для Логера
class ILogger(ABC):
    @abstractmethod
    def log(self, text: str):
        pass