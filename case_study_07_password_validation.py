password = input("Enter password: ")

errors = []

if len(password) < 8:
    errors.append("Minimum 8 characters required")

if not any(c.isupper() for c in password):
    errors.append("At least one uppercase letter required")

if not any(c.islower() for c in password):
    errors.append("At least one lowercase letter required")

if not any(c.isdigit() for c in password):
    errors.append("At least one digit required")

if not any(not c.isalnum() for c in password):
    errors.append("At least one special character required")

if "password" in password.lower():
    errors.append("Cannot contain the word 'password'")

if errors:
    print("Invalid Password")
    for error in errors:
        print("-", error)
else:
    print("Valid Password")