
names = ["Heama", "Keerthy", "Kavya", "Sara", "Nila", "Abhi"]
grouped_names = {}

for name in names:
    first_letter = name[0]  
    if first_letter in grouped_names:
        grouped_names[first_letter].append(name)
    else:
        grouped_names[first_letter] = [name]

print(grouped_names)
