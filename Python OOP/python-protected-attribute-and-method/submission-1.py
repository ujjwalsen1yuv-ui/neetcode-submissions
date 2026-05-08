class Account:
    def __init__(self, name, Balance):
        self.name = name
        self.Balance = Balance
        pass
    
    def _display_balance(self) -> None:
        print(f"Balance: ${self.Balance}")
        pass


# Do not modify the code below this line
account = Account("John", 1000)
account._display_balance()
