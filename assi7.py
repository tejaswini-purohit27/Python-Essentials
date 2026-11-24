
# Function to calculate total calories
def calculate_calories(carbs, fats, proteins):
    total_calories = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total_calories


# Input grams of nutrients consumed
carbs = float(input("Enter grams of carbohydrates: "))
fats = float(input("Enter grams of fats: "))
proteins = float(input("Enter grams of proteins: "))

# Calculate total calories
calories = calculate_calories(carbs, fats, proteins)

# Display the result
print("Total daily caloric intake =", calories, "calories")
