import re

number = input("What's your phone number? ").strip()

if re.search(r"^07\d{9}", number):
    print("Valid")

else:
    print("Invalid phone number")