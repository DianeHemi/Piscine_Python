from the_bank import Account, Bank

bank = Bank()
a1 = Account("Diane")
a1.transfer(1000)
a2 = Account("Loic")
a2.transfer(500)
a3 = Account("Jim")
a3.transfer(200)

bank.add(a1)
bank.add(a2)
bank.add(a3)

bank.transfer(a1, a2, 200)
bank.fix_account(a1)
