# Exercise 6 - Vanessa Belous

import re

# function to validate the user's phone number
def val_phone(phone_number):
    # uses a $ as an end-of-string character, with re.match
    phone_pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$'
    # checks if the input matches the above pattern
    if re.match(phone_pattern, phone_number):
        print("\tPhone number is valid.")
    else:
        print("\tPhone number has an incorrect format.")

# function to validate the user's social security number
def val_social(social_number):
    # does not use an end-of-string character, because re.fullmatch makes it unnecessary
    social_pattern = r'\d\d\d[ -]\d\d[ -]\d\d\d\d'
    # checks if the input matches the above pattern
    if re.fullmatch(social_pattern, social_number):
        print("\tSocial security number is valid.")
    else:
        print("\tSocial Security number has an incorrect format.")

# function to validate the user's zip code
def val_zip(zip_code):
    zip_pattern = r'\d\d\d\d\d'
    # checks if the input matches the above pattern
    if re.fullmatch(zip_pattern, zip_code):
        print("\tZip code is valid.")
    else:
        print("\tZip code has an incorrect format.")

def main():
    # variables to store user inputs
    phone = input("Enter your phone number: ")
    social = input("Enter your Social Security number: ")
    zip_code = input("Enter your zip code: ")

    # function calls, which display results
    print("\nResults:")
    val_phone(phone)
    val_social(social)
    val_zip(zip_code)

main()