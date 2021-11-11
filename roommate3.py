class Roommate:
    def __init__(self,name,days):
        self.name = name
        self.days = days

    def pay(self,mate_date,t):
        amount = (int(self.days) * t) / (mate_date + self.days)
        return amount

'''
total = int(input("Enter the total amount: "))
bill = input("What is the bill period? E.g. Oct 12: ")

name1 = input("What is your name? ")
days1 = int(input(f"How many days did {name1} stay? "))

name2 = input("What is yout roommate name? ")
days2 = int(input(f"How many days did {name2} stay? "))

person1 = Roommate(name1,days1)
person2 = Roommate(name2,days2)

print(bill)
print(f"{name1} pays: {person1.pay(days2,total)}")
print(f"{name2} pays: {person2.pay(days1,total)}")
'''