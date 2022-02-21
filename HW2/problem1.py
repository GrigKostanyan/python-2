class BankAccount:
    def __init__(self):
        self.id = 0
        self.balance = 0
        self.rate = 0

class BankAccountBuilder:
    def __init__(self):
        pass
    def setId(self):
        pass
    def setBalance(self):
        pass
    def setRate(self):
        pass
    
class PersonalAccountBuilder(BankAccountBuilder):
    def __init__(self):
        self.bankAccount = BankAccount()
    def setId(self, id):
        self.bankAccount.id = id
    def setBalance(self, b):
        self.bankAccount.balance = b

class BusinessAccountBuilder(BankAccountBuilder):
    def __init__(self):
        self.bankAccount = BankAccount()
    def setId(self, id):
        self.bankAccount.id = id
    def setBalance(self, b):
        self.bankAccount.balance = b
    def setRate(self, rate):
        self.bankAccount.rate = rate
        
personalAccountBuilder = PersonalAccountBuilder()
personalAccountBuilder.setId(1)
personalAccountBuilder.setBalance(10000)
personalAccount = personalAccountBuilder.bankAccount

businessAccountBuilder = BusinessAccountBuilder()
businessAccountBuilder.setId(1)
businessAccountBuilder.setBalance(10000)
businessAccountBuilder.setRate(5)
businessAccount = businessAccountBuilder.bankAccount
