# TASK: take input from user and print encoded string based on choice
# 1. utf-8, 2. hex, 3. binary
text = input("say something: ")
option = int(input("Which option: "))

if option ==1:
    text=text.encode("utf-8")
    print(list(text))
elif option==2:
    text = text.encode()
    text = text.hex()
    print(text)
elif option==3:
    res = ""
    for char in text:
        asc = ord(char)
        binary = format(asc, "08b")
        res += binary
    # text = "".join(format(ord(char), 'b') for char in text)
    print(res)