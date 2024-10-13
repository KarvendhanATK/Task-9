#Task-9.4

#Write a Python function to validate the Regular Expression for the following :- 
# a.) Email Address
# b.) Mobile numbers of Bangladesh
# c.) Telephone numbers of USA 
# d.) 16 character Alpha-Numeric password composed of alphabets of Upper Case,Lower Case,Special Characters,Numbers.

import re

def validate_input(email, bangladesh_mobile, usa_telephone, password):
    # Regular patterns
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    bangladesh_mobile_pattern = r'^\+8801[3-9]\d{8}$'
    usa_telephone_pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'

    # Validations of email,mobile no,telephone,password
    email_valid = bool(re.match(email_pattern, email))
    mobile_valid = bool(re.match(bangladesh_mobile_pattern, bangladesh_mobile))
    telephone_valid = bool(re.match(usa_telephone_pattern, usa_telephone))
    password_valid = bool(re.match(password_pattern, password))

    return {
        "Email Valid": email_valid,
        "Bangladesh Mobile Valid": mobile_valid,
        "USA Telephone Valid": telephone_valid,
        "Password Valid": password_valid
    }

# Example:
result = validate_input(
    "atk@gmail.com",
    "+8801712345678",
    "(123) 456-7890",
    "Atkatkatk@123456"
)

print(result)
