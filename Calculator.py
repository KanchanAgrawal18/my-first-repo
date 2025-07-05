first_number = float(input("Enter first number:\n"))
operation = input("Enter operation(+, -, *, /, ^(for power))\n")
second_number = float(input("Enter second number:\n"))
if operation == "+":
    print("Result: " + str(first_number + second_number))
elif operation == "-":
    print("Result: " + str(first_number - second_number))
elif operation == "*":
    print("Result: " + str(first_number * second_number))
elif operation == "^":
    print("Result: " + str(first_number ** second_number))
else:
    print("Result: " + str(first_number / second_number))
print("Thank you for using the calculator.")

    