sea_trips = int(input())
mountain_trips = int(input())

sea_price = 680
mountain_price = 499


total_profit = 0

all_sold = False

while True:

    package = input()

    if package == "Stop":
        break

    if package == "sea" and sea_trips > 0:
        total_profit += sea_price
        sea_trips -= 1
    elif package == "mountain" and mountain_trips > 0:
        total_profit += mountain_price
        mountain_trips -= 1


    if sea_trips == 0 and mountain_trips == 0:
        all_sold = True
        break


if all_sold:
    print("Good job! Everything is sold.")
print(f"Profit: {total_profit} leva.")
