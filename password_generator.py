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
    include_special = input("Include special charecters? (yes/no):").strip().lower()
    include_digits = input("Include digits? (yes/no):").strip().lower()

    if length < 4:
        print("password must be at least 4 characters")
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase =="yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower+uppercase+special+digits

    required_characters = []
    if uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if special == "yes":
        required_characters.append(random.choice(special))
    if digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range (remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password


#get all available charecters
#randomly pick charecters
#Ensure atleaste we one charecter of each type
#Ensure length is valid

password = generate_password()
print(password)