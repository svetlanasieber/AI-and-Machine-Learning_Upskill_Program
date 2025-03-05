n = int(input())

total_sales = 0
total_rating = 0


for _ in range(n):

    data = int(input())

    rating = data % 10
    possible_sales = data // 10


    if rating == 2:
        percent_sales = 0
    elif rating == 3:
        percent_sales = 0.50
    elif rating == 4:
        percent_sales = 0.70
    elif rating == 5:
        percent_sales = 0.85
    elif rating == 6:
        percent_sales = 1.00
    else:
        percent_sales = 0


    actual_sales = possible_sales * percent_sales
    total_sales += actual_sales
    total_rating += rating


average_rating = total_rating / n


print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")
