from interfaces import ILogger, IObserver
from models import Account, AccountType

# === ПАТЕРН SINGLETON (Одинак) ===
class SingletonLogger(ILogger):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
        return cls._instance

    def log(self, text: str):
        print(f"[LOG]: {text}")

# === ПАТЕРН FACTORY METHOD (Фабрика) ===
class AccountFactory:
    @staticmethod
    def create_account(acc_type: str, acc_id: int, client_id: int) -> Account:
        initial_balance = 0.0
        # Логіка: Золотий рахунок отримує бонус при відкритті
        if acc_type == AccountType.GOLD:
            initial_balance = 100.0
        
        return Account(id=acc_id, client_id=client_id, type=acc_type, balance=initial_balance)

# === ПАТЕРН OBSERVER (Спостерігач) ===
class NotificationManager:
    def __init__(self):
        self._subscribers = []  # Список підписників

    def subscribe(self, observer: IObserver):
        self._subscribers.append(observer)

    def notify_all(self, message: str):
        for subscriber in self._subscribers:
            subscriber.update(message)

# Конкретний спостерігач: СМС
class SmsObserver(IObserver):
    def update(self, message: str):
        print(f" >> [SMS]: {message}")

# Конкретний спостерігач: Email
class EmailObserver(IObserver):
    def update(self, message: str):
        print(f" >> [EMAIL]: {message}")