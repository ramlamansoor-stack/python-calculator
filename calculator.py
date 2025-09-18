# Step 1: Ask the user to choose an operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Step 2: Get user input
choice = input("Enter choice (1/2/3/4): ")

# Step 3: Get two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 4: Perform the operation
if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid input")
