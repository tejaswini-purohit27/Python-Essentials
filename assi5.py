
# Input the number of students
n = int(input("Enter the number of students: "))

class_total = 0

# Loop through each student
for i in range(1, n + 1):
    print("\nStudent", i)
    total = 0

    # Input marks for 5 tests
    for j in range(1, 6):
        marks = float(input("Enter marks for test " + str(j) + ": "))
        total += marks

    # Calculate student average
    average = total / 5
    print("Average marks of student", i, "=", average)

    class_total += total

# Calculate overall class average
class_average = class_total / (n * 5)

print("\nOverall class average =", class_average)
