number_of_trips_to_the_sea = int(input())
number_of_excursions_per_mountain = int(input())
sea_cost = 680
mountain_cost = 499
profit_sum = 0
while True:
    package_name = input()
    if package_name == "Stop":
        break
    if package_name == "sea":
        if number_of_trips_to_the_sea == 0:
            continue
        profit_sum += sea_cost
        number_of_trips_to_the_sea -= 1
    if package_name == "mountain":
        if number_of_excursions_per_mountain == 0:
            continue
        profit_sum += mountain_cost
        number_of_excursions_per_mountain -= 1
    if number_of_trips_to_the_sea == 0 and number_of_excursions_per_mountain == 0:
        print("Good job! Everything is sold.")
        break
print(f"Profit: {profit_sum} leva.")