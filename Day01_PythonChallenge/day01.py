# All the inputs are taken from the user
FullName = input("Full Name:")
Email = input("Email:")
Mobile = input("Mobile:")
Age = int(input("Age:"))

# Name Validation
if FullName.count(" ") >= 1 and FullName[len(FullName) - 1] != " " and FullName[0] != " ":
    FullName_valid = True
else:
    FullName_valid = False

# Email Validation
if Email.count("@") == 1 and Email.count(".") >= 1 and Email[0] != "@":
    Email_valid = True
else:
    Email_valid = False

# Mobile Number Validation
if len(Mobile) == 10 and Mobile.isdigit() and Mobile[0] != '0':
    Mobile_valid = True
else:
    Mobile_valid = False

# Age Validation
if Age >= 18 and Age <= 60:
    Age_valid = True
else:
    Age_valid = False

# Final Output
if FullName_valid and Email_valid and Mobile_valid and Age_valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
