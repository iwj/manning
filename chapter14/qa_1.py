class BankAccount:
    def __init__(self):
        self.name = "Liu Xiaoying"
        self.number = 4567543871468146
        self.balance = 9108.01

    def showBalance(self,):
        self.stars()
        print "Dear " + self.name + ","
        print "Your number: " + str(self.number)
        print "Your balance:"
        print "$ " + str(self.balance)

    def saveMoney(self, saveAmount):
        self.stars()
        print "You printed " + str(saveAmount)
        if isinstance(saveAmount, float):
            print "float"
            self.balance += saveAmount
            self.showBalance()
        elif isinstance(saveAmount, int):
            print "int"
            self.balance += float(saveAmount)
            self.showBalance()
        else:
            print "Not a number!"

    def withdrawals(self, withdrawAmount):
        self.stars()
        if isinstance(withdrawAmount, float):
            print "float"
            if withdrawAmount > self.balance:
                print "You do not have so much money."
            else:
                print "withdraw success"
                self.balance -= withdrawAmount
            self.showBalance()
        elif isinstance(withdrawAmount, int):
            print "int"
            self.balance += float(saveAmount)
            self.showBalance()
        else:
            print "Not a number!"

    def stars(self,):
        print "\n" + "* "*8

myBank = BankAccount()
myBank.showBalance()
myBank.saveMoney(100)
myBank.saveMoney(2.2)
myBank.saveMoney("oops")
myBank.withdrawals(300.01)
myBank.withdrawals(3999900.01)
