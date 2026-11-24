
try:
    # Open the file in read mode
    file = open("sample.txt", "r")

    # Read the contents of the file
    content = file.read()

    # Print the contents
    print("File contents:")
    print(content)

    # Close the file
    file.close()

except FileNotFoundError:
    print("Error: File not found.")
