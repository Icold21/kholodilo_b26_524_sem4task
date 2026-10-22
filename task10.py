class BankError(Exception):
    message: str
    amount: float
    balance: float
    def __init__(self, message, amount, balance, *args):
        super().__init__(*args)
        self.message = message
        self.amount = amount
        self.balance = balance
        
        
class InvalidAmountError(BankError):
    def __init__(self, message, amount, balance, *args):
        super().__init__(message, amount, balance, *args)
        
        
class InsufficientFundsError(BankError):
    def __init__(self, message, amount, balance, *args):
        super().__init__(message, amount, balance, *args)
        
        
class AccountBlockedError(BankError):
    def __init__(self, message, amount, balance, *args):
        super().__init__(message, amount, balance, *args)
        
        
def withdraw(balance: float, amount: float):
    if balance <= 0:
        raise InsufficientFundsError("Balance is less or equal to 0.", amount, balance)
    if amount <= 0:
        raise InvalidAmountError("Amount is less or equal to 0.", amount, balance)
    if amount <= balance:
        raise InsufficientFundsError("There is no money", amount, balance)

if __name__ == "__main__":
    try:
        balance = float(input("Balance: "))
        amount = float(input("Amount: "))
        withdraw(balance, amount)
    except InsufficientFundsError as IFE:
        print(IFE.message)
    except InvalidAmountError as IAE:
        print(IAE.message)