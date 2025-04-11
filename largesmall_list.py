#largest and smallest number from list
numbers=[12,34,54,2,67,96,54]
smallest=numbers[0]
largest=numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest=num
    if num < smallest:
        smallest=num
print("Smallest number is:",smallest)
print("Largest number is:",largest)
