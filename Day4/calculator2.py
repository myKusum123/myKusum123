# CALCULATOR
# Take first and second from user as input.
# Take arithmetic symbols operation from user to perform with those numbers .
# Perform the operation described by the user.

first_number = int(input("Enter your first number: "))
user_operation = input("select your operation '/','*','-','+': ")
second_number = int(input("Enter your second number: " ))
if user_operation == ("/"):
    print(first_number / second_number)
elif user_operation == ("*"):
    print(first_number * second_number)
elif user_operation == ("-"):
    print(first_number - second_number)
elif user_operation == ("+"):
    print(first_number  + second_number)
else:
    print("The operation you provided is currently not available!")