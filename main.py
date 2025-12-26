from services import BankFacade
from patterns import SmsObserver, EmailObserver
from models import Client, AccountType

def main():
    print("=== BANK SYSTEM START (UA) ===\n")

    # 1. Створюємо Банк (Фасад)
    bank = BankFacade()

    # 2. Підключаємо сповіщення (Observer)
    bank.setup_notifications(SmsObserver())
    bank.setup_notifications(EmailObserver())

    # 3. Створюємо клієнта
    user = Client(id=1, name="Олег", rating=75)

    print("--- Відкриття рахунків ---")
    # 4. Відкриваємо рахунки (Factory працює всередині Фасаду)
    acc_main = bank.open_account(user, AccountType.DEBIT)
    acc_bonus = bank.open_account(user, AccountType.GOLD) # Тут одразу буде бонус 100 грн

    print(f"Баланс Gold: {acc_bonus.balance} грн")

    print("\n--- Фінансові операції ---")
    # 5. Робимо переказ
    bank.transfer(acc_bonus, acc_main, 50.0)

    # 6. Беремо кредит
    bank.request_loan(user, acc_main, 5000.0)

    print("\n--- Фінальний результат ---")
    print(f"Рахунок Main: {acc_main.balance} грн")
    print(f"Рахунок Gold: {acc_bonus.balance} грн")

if __name__ == "__main__":
    main()