# Taking input from the user
number = int(input("Enter number to find Factorial = "))

# Initialize variables for calculation
multiplier = 1
factorial = 1

# Loop to calculate factorial
while multiplier <= number:
    factorial *= multiplier  # factorial = factorial * multiplier
    multiplier += 1  # multiplier = multiplier + 1
    
print(f"Factorial of {number} is = ", factorial)
