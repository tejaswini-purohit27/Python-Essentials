
# Input the secret message and coded message
secret_message = input("Enter the secret message (substring): ")
coded_message = input("Enter the coded message (string): ")

# Check whether the secret message exists
if secret_message in coded_message:
    print("Secret message found!")
else:
    print("Secret message not found!")
