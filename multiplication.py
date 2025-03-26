# Function to calculate sum and multiplication
def calculate_operations(a, b):
    # Sum
    sum_result = a + b
    # Multiplication
    multiplication_result = a * b
    return sum_result, multiplication_result


num1 = 2
num2 = 2

sum_result, multiplication_result = calculate_operations(num1, num2)

print(f"Sum: {sum_result}")
print(f"Multiplication: {multiplication_result}")
