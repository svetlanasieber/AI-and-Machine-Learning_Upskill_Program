class SavingsCalculator:
    def __init__(self, daily_money, daily_earnings, expenses, gift_price):
        self.daily_money = daily_money
        self.daily_earnings = daily_earnings
        self.expenses = expenses
        self.gift_price = gift_price

    def calculate_savings(self):

        saved_money_pockets = 5 * self.daily_money
        earned_money = 5 * self.daily_earnings


        total_saved_money = saved_money_pockets + earned_money
        all_saved_money = total_saved_money - self.expenses

        return all_saved_money

    def evaluate_savings(self):

        all_saved_money = self.calculate_savings()


        if all_saved_money > self.gift_price:
            return f"Profit: {all_saved_money:.2f} BGN, the gift has been purchased."
        else:
            needed_money = self.gift_price - all_saved_money
            return f"Insufficient money: {needed_money:.2f} BGN."


daily_money = float(input())
daily_earnings = float(input())
expenses = float(input())
gift_price = float(input())


savings_calculator = SavingsCalculator(daily_money, daily_earnings, expenses, gift_price)


print(savings_calculator.evaluate_savings())
#Wir studieren objektorientierte Programmierung
# in der Schule und das ist meine Erfahrung für diese Aufgabe