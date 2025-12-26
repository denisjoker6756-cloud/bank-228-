# container.py
# Імпортуємо всі наші класи.
from services import ConsoleLogger, SmsNotifier, BankOperationsService, CreditService, DepositService

class DIContainer:
    def __init__(self):
        # 1. Створюємо "низькорівневі" об'єкти (інструменти).
        self.logger = ConsoleLogger()       # Створили логер.
        self.notifier = SmsNotifier()       # Створили СМС-сповіщувач.

        # 2. Створюємо сервіси і ВРУЧНУ передаємо їм інструменти.
        # BankOperationsService не створює логер сам, він бере готовий.
        self.operations = BankOperationsService(self.logger, self.notifier)
        
        self.credit = CreditService(self.logger)
        self.deposit = DepositService(self.logger)

    # Методи, щоб отримати готові до роботи сервіси у main.py.
    def get_operations_service(self):
        return self.operations

    def get_credit_service(self):
        return self.credit
    
    def get_deposit_service(self):
        return self.deposit