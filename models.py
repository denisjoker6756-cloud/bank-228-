from dataclasses import dataclass

# Константи для типів рахунків
class AccountType:
    DEBIT = "debit"      # Дебетовий
    CREDIT = "credit"    # Кредитний
    GOLD = "gold"        # Золотий (бонусний)

# Дані клієнта
@dataclass
class Client:
    id: int
    name: str
    rating: int  # Кредитний рейтинг (0-100)

# Дані рахунку
@dataclass
class Account:
    id: int
    client_id: int
    type: str
    balance: float