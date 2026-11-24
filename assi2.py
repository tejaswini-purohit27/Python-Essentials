EARTH_GRAVITY = 9.8
MOON_GRAVITY = 1.6

def calculate_weight(mass, gravity):
    weight = mass * gravity
    return weight

layout = "Weight Calculator"

mass = float(input("Enter the mass of the object in kg: "))

earth_weight = calculate_weight(mass, EARTH_GRAVITY)
moon_weight = calculate_weight(mass, MOON_GRAVITY)

print("Weight on Earth:", earth_weight, "N")
print("Weight on Moon:", moon_weight, "N")

# Answers
print("Constant identifier:", "EARTH_GRAVITY")
print("User defined function:", "calculate_weight")
print("Data type of layout:", type(layout).__name__)
print("Parameter name:", "mass")
print("Arithmetic operator:", "*")