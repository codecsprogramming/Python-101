# TASK: create patterns from a list of passwords
# create a pattern for passwords in a list
# lowercase letter > ?l
# uppercase letter > ?u
# digit > ?d
# symbol > ?s
# Example
# Passwd12! -> ?u?l?l?l?l?l?d?d?s
a = """Passwd12!
letmein2@
!!pwd12!!
@B4kili@
Salamm23@
gedebey2!
abcdefg5@
Strong23^
##qwerty33"""
passwords = a.split("\n")

for password in passwords:
    for char in password:
        if char.isupper():
            print("?u", end="")
        elif char.islower():
            print("?l", end="")
        elif char.isnumeric():
            print("?d", end="")
        else:
            print("?s", end="")
    print()