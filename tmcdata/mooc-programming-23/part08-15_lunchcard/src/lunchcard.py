

class LunchCard:
    def __init__(self, balance):
        self.balance = balance

    def eat_lunch(self):
        if self.balance > 2.60:
            self.balance -= 2.60
        

    def eat_special(self):
        if self.balance > 4.60:
            self.balance -= 4.60
       

    def deposit_money(self, balance):
        if balance < 0:
            myError = ValueError("You cannot deposit an amount of money less than zero")
            raise myError
        self.balance += balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"


peters = LunchCard(20)
graces = LunchCard(30)
peters.eat_special()
graces.eat_lunch()
print("Peter:", peters)
print("Grace:", graces)
peters.deposit_money(20)
graces.eat_special()
print("Peter:", peters)
print("Grace:", graces)
peters.eat_lunch()
peters.eat_lunch()
graces.deposit_money(50)
print("Peter:", peters)
print("Grace:", graces)