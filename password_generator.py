import random
import string

#Collect user details
#length
#Must have Uppercase
#Must have digits
#Must have special charecter

def generate_password():
    length = int(input("Enter desired password length:").strip())
    include_uppercase = input("Include upper case letters? (yes/no):").strip().lower()
    include_digits = input("Include digits? (yes/no)").strip().lower()
    include_special = input("Include special charecters? (yes/no)").strip().lower()
#get all available charecters
#randomly pick charecters
#Ensure atleaste we one charecter of each type
#Ensure length is valid

generate_password()