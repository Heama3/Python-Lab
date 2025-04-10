#Valid password checking
password=input("Enter your password:")
has_upper=any(char.isupper() for char in password)
has_lower=any(char.islower() for char in password)
has_digit=any(char.isdigit() for char in password)
is_long_enough=len(password)>=8

if has_upper and has_lower and has_digit and is_long_enough:
    print("Valid password")
else:
    print("Invalid password")
