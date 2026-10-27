##alogarithm
Algorithm
1.	Start.
2.	Read a password.
3.	Check length and each required character category.
4.	Check for three identical consecutive characters.
5.	Store every failed rule in a list.
6.	If no rules fail, print valid; otherwise print the failed rules.
7.	End.

##flowchart
          ( START )
              |
       / Read password /
              |
       < Length >= 8? >
          /        \
        No          Yes
         |           |
   [Invalid]  < Has uppercase,
         |      lowercase, digit
       (END)   and special char? >
                  /        \
                No          Yes
                 |           |
            [Invalid]     [Valid]
                 \           /
                / Print result /
                       |
                    ( END )
##python code
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
##output
Enter password: Hello@123
Valid Password