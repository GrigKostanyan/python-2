class BankAccount:
  def CreateAccount(self):
    print("Bank account")

class PersonalAccount(BankAccount):
  def CreateAccount(self):
    print("Personal account")

class BusinessAccount(BankAccount):
  def CreateAccount(self):
    print("Business account")

class BankAccountFactory:
  def __init__(self):
    self.accounts = { "PersonalAccount": PersonalAccount,
                      "BusinessAccount": BusinessAccount }

  def create(self, account):
    if account in self.accounts:
      return self.accounts[account]()
    else:
      print("Invalid account...")

class Client:
  def __init__(self):
    self.accounts = { "1": "PersonalAccount",
                      "2": "BusinessAccount" }
    self.accountCreator = BankAccountFactory()

  def createAccount(self):
    x = input("Choose account type:\n1 - Personal account\n2 - Business account\n")
    if x in self.accounts:
      self.accountCreator.create(self.accounts[x]).CreateAccount()
    else:
      print("Invalid number...")

client = Client()
client.createAccount()
