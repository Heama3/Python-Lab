# Function to check whether the number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input from the user
num = int(input("Enter a number: "))


result = check_even_odd(num)
print(f"The number {num} is {result}.")
