class NutritionCalculator:
    def __init__(self, percent_fats, percent_proteins, percent_carbohydrates, total_calories, percent_containing_water):
        self.percent_fats = percent_fats
        self.percent_proteins = percent_proteins
        self.percent_carbohydrates = percent_carbohydrates
        self.total_calories = total_calories
        self.percent_containing_water = percent_containing_water

    def calculate_nutritional_content(self):

        self.total_grams_fats = (self.percent_fats * self.total_calories) / 9
        self.total_grams_proteins = (self.percent_proteins * self.total_calories) / 4
        self.total_grams_carbohydrates = (self.percent_carbohydrates * self.total_calories) / 4


        self.weight_food = self.total_grams_fats + self.total_grams_proteins + self.total_grams_carbohydrates
        self.calories_one_gram_food = self.total_calories / self.weight_food
        self.percent_food = 100 - self.percent_containing_water


        self.calories = self.calories_one_gram_food * self.percent_food

        return self.calories


percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_containing_water = int(input())


calculator = NutritionCalculator(percent_fats, percent_proteins, percent_carbohydrates, total_calories, percent_containing_water)


calories = calculator.calculate_nutritional_content()
print(f"{calories:.4f}")
