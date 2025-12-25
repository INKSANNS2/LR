class BankAccount:
    """Класс для представления банковского счета."""
    
    def __init__(self, account_holder: str, balance: float = 0):
        """
        Инициализация банковского счета.
        
        Args:
            account_holder: Владелец счета
            balance: Начальный баланс (по умолчанию 0)
        """
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        """
        Пополняет счет на указанную сумму.
        
        Args:
            amount: Сумма для пополнения
        """
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        """
        Снимает деньги со счета.
        
        Args:
            amount: Сумма для снятия
        
        Если на счету недостаточно средств, выводит сообщение об ошибке.
        """
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
    
    def get_balance(self) -> float:
        """
        Возвращает текущий баланс.
        
        Returns:
            Текущий баланс счета
        """
        return self.balance
# Пример использования
account = BankAccount("Ivanov", 100)
account.deposit(50)
account.withdraw(200) 
account.withdraw(80)
print(account.get_balance()) 