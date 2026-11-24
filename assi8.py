
import math

def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        return math.pi * radius * radius

    elif shape == "rectangle":
        length, breadth = args
        return length * breadth

    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height

    else:
        return "Invalid shape!"


# Choose a shape
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    radius = float(input("Enter radius: "))
    area = calculate_area("circle", radius)
    print("Area of circle =", area)

elif choice == "2":
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = calculate_area("rectangle", length, breadth)
    print("Area of rectangle =", area)

elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = calculate_area("triangle", base, height)
    print("Area of triangle =", area)

else:
    print("Invalid choice!")
