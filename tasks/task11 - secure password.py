# TASK: secure password generator given policy
# 1. Min 8 len, at least 1 uppercase, lowercase, digit, symbol
# 2. Generate temp password with all letter types
# 3. Fill the rest based on len 
# 4. Shuffle
# 5. Join

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']
import random
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
def passwordduzelt(uzunluq) :
    password= [ random.choice(DIGITS) ,
               random.choice(UPCASE_CHARACTERS),
               random.choice(LOCASE_CHARACTERS),
               random.choice(SYMBOLS)
                ]
    if uzunluq>=4:
        password+=random.choices(COMBINED_LIST,k=uzunluq-4)
        print(password)
    if uzunluq<4 :
        print( "Minimum 4 uzunluq vermelisen")
    random.shuffle(password)
    return "".join(password)
print(passwordduzelt(2))
