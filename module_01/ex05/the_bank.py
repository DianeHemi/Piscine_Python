class Account(object):
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1
        
    def transfer(self, amount):
        self.value += amount


class Bank:
    """The bank"""
    
    def __init__(self):
        self.account = []
        
    def add(self, account):
        self.account.append(account)
        
    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        
        if dir(dest) != dir(origin):
            raise Exception("Sender or receiver is not an account")
        
        if origin not in self.account or dest not in self.account:
            raise Exception("Sender or receiver is not a registered account")
        
        if amount < 0:
            raise Exception("Transfer amount cannot be negative")

        sender = next(x for x in self.account if origin.id == x.id or origin.name == x.name)
        receiver = next(x for x in self.account if dest.id == x.id or dest.name == x.name)
        print(sender.name, "to", receiver.name)
        

        

        
        
        
    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        