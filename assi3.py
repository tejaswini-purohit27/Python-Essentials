
# Create a list of assignments
assignments = ["Python", "Mathematics", "C++"]

print("Original assignments:", assignments)

# Add a new assignment
new_assignment = input("Enter a new assignment: ")
assignments.append(new_assignment)

print("After adding:", assignments)

# Remove a completed assignment
completed = input("Enter the completed assignment to remove: ")

if completed in assignments:
    assignments.remove(completed)
    print("Assignment removed successfully.")
else:
    print("Assignment not found.")

# Print the updated list
print("Updated assignments:", assignments)
