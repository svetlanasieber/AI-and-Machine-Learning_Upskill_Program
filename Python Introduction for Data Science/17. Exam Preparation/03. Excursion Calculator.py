# Input hier:
tourists = int(input())
season = input()


price_per_tourist = 0

# Calculation hier:
if season == "spring":
    if tourists > 5:
        price_per_tourist = 48
    else:
        price_per_tourist = 50
elif season == "summer":
    if tourists > 5:
        price_per_tourist = 45
    else:
        price_per_tourist = 48.50
elif season == "autumn":
    if tourists > 5:
        price_per_tourist = 49.50
    else:
        price_per_tourist = 60
elif season == "winter":
    if tourists > 5:
        price_per_tourist = 85
    else:
        price_per_tourist = 86


final_price = price_per_tourist * tourists


if season == "summer":
    final_price *= 0.85
elif season == "winter":
    final_price *= 1.08

# Output hier:
print(f"{final_price:.2f} leva.")
