class Account(object):
    ID_COUNT = 1
    value = 0
    
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
        
        if dir(dest) != dir(origin) or amount < 0:
            return False
        
        if origin not in self.account or dest not in self.account:
            return False

        sender = next(x for x in self.account if origin.id == x.id or origin.name == x.name)
        receiver = next(x for x in self.account if dest.id == x.id or dest.name == x.name)
        if sender.value < amount:
            return False
        else:
            sender.transfer(-amount)
            receiver.transfer(amount)
        return True     
   
        
        
    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        
        acc = next(x for x in self.account if account.id == x.id or account.name == x.name)
        acc_data = dir(account)
        
        if "name" not in acc_data:
            acc.name = ""
        elif "id" not in acc_data:
            acc.id = acc.ID_COUNT
        elif "value" not in acc_data:
            acc.value = 0
        
        for element in acc_data:
            if element.startswith("__b") or element.startswith("b"):
                del element
        
        if len([x for x in acc_data if x.startswith('zip')]) == 0:
            acc.zip = ""
        if len([x for x in acc_data if x.startswith('addr')]) == 0:
            acc.addr = ""
        
        if len(acc_data) % 2 != 1:
            return False
        
        print(dir(account))
        return True