tereza_day_money = float(input())
money_tereza_gets = float(input())
tereza_expenses = float(input())
gift_price = float(input())

saved_money_pockets = 5 * tereza_day_money
earned_money = 5 * money_tereza_gets
total_saved_money = saved_money_pockets + earned_money
all_saved_money = total_saved_money - tereza_expenses

if all_saved_money > gift_price:
    print(f"Profit: {all_saved_money:.2f} BGN, the gift has been purchased.")
else:
    needed_money = gift_price - all_saved_money
    print(f"Insufficient money: {needed_money:.2f} BGN.")