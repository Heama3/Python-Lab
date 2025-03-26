# Function to calculate the square and cube of a number
def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# Input from the user
number = float(input("Enter a number: "))

# Calculate square and cube
square, cube = calculate_square_and_cube(number)

print(f"The square of {number} is: {square}")
print(f"The cube of {number} is: {cube}")
