import random
import string

def gen_pass(min_len, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    char = letters
    if numbers:
        char += digits
    if special_characters:
        char += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(char)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd
        

min_len = int(input("ENTER THE MINIMUM LENGTH: "))
has_number = input("DO YOU WANT TO HAVE NUMBERS? (y/n) ").lower() == "y"
has_special = input("DO YOU WANT TO HAVE SPECIAL CHARACTERS? (y/n) ").lower() == "y"
pwd = gen_pass(min_len, has_number, has_special)
print("THE GENERATED PASSWORD IS:", pwd)