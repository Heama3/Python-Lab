contacts = {
    "Heama": "7566756748",
    "Priya": "2345678675"
}
name = input("Enter contact name: ")
phone = input("Enter phone number: ")


if name in contacts:
    print(f"Updating {name}'s number.")
else:
    print(f"Adding new contact: {name}")

contacts[name] = phone


print(f"{name}'s number is now {contacts[name]}")
