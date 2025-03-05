percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_containing_water = int(input())


total_grams_fats = (percent_fats * total_calories) / 9
total_grams_proteins = (percent_proteins * total_calories) / 4
total_grams_carbohydrates = (percent_carbohydrates * total_calories) / 4

weight_food = total_grams_fats + total_grams_proteins + total_grams_carbohydrates
calories_one_grams_food = total_calories / weight_food
percent_food = 100 - percent_containing_water
calories = calories_one_grams_food * percent_food

# Output hier:
print(f"{calories:.4f}")
