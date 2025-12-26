from patterns import SingletonLogger, AccountFactory, NotificationManager
from models import Client, Account

# === ПАТЕРН FACADE (Фасад) ===
class BankFacade:
    def __init__(self):
        # Ініціалізуємо підсистеми
        self.logger = SingletonLogger()
        self.notifier = NotificationManager()
        self.accounts_db = []  # Імітація бази даних

    # Налаштування сповіщень
    def setup_notifications(self, observer):
        self.notifier.subscribe(observer)

    # Відкриття рахунку (через Фабрику)
    def open_account(self, client: Client, acc_type: str) -> Account:
        new_id = len(self.accounts_db) + 1
        account = AccountFactory.create_account(acc_type, new_id, client.id)
        self.accounts_db.append(account)
        
        self.logger.log(f"Створено рахунок '{acc_type}' для клієнта {client.name}")
        return account

    # Переказ коштів
    def transfer(self, acc_from: Account, acc_to: Account, amount: float):
        self.logger.log(f"Транзакція: Рахунок #{acc_from.id} -> #{acc_to.id}, Сума: {amount} грн")
        
        if acc_from.balance >= amount:
            acc_from.balance -= amount
            acc_to.balance += amount
            self.notifier.notify_all(f"Переказ успішний! {amount} грн отримано.")
        else:
            self.logger.log("Помилка: Недостатньо коштів")

    # Кредитування
    def request_loan(self, client: Client, account: Account, amount: float):
        self.logger.log(f"Запит на кредит від {client.name} на суму {amount} грн")
        
        if client.rating > 50:
            account.balance += amount
            self.logger.log("Кредит схвалено.")
            self.notifier.notify_all(f"Вам нараховано кредитні кошти: {amount} грн")
        else:
            self.logger.log("Кредит відхилено (низький рейтинг).")