# ---------------------------------DAY 5-----------------------------------

# Functions
# def func(text, ending):
#     print(text, ending)
#     return "end"

# result = func("salam", "!")
# print(f"Result: {result}")
# text = input("Say something: ")
# func(f"You said: {text}", "!", None)

## default value for arguments
# def func(text, ending="."):
#     print(text, ending)

# text = input("Say something: ")
# func(f"You said: {text}", "?")

## named argument
# def func(username, password, dob, city, bio):
#     print(text, ending)

# func("salam", "!")
# func(ending="!", text="salam")

## code reuse
# def encode(text):
#     print(text.encode())

# text = input("Say smt: ")
# lowerOrUpper = input("l/u: ")
# if lowerOrUpper == "l":
#     text = text.lower()
#     encode(text)
# elif lowerOrUpper == "u":
#     text = text.upper()
#     encode(text)
# else:
#     text = text[0]
#     encode(text)

## recursive function
# def func(num, step):
#     print(num)
#     if num:
#         return func(num-step, step)

# func(100, 6)

### TASK: print nth fibonacci number

## *args
# def sum(*nicat):
#     print(nicat, type(nicat))
#     res = 0
#     for num in nicat:
#         res += num
#     print(res)

# nums = []
# while True:
#     num = input("Enter number: ")
#     if not num:
#         sum(*nums) # unpack
#         break
#     else:
#         nums.append(float(num))

## **kwargs
# def sum(*nicat, **nuraya): # nicat = args, nuraya = kwargs
#     print(nicat, type(nicat))
#     print(nuraya, type(nuraya))
#     res = 0
#     for num in nicat:
#         res += num
#     print(res)

# nums = []
# while True:
#     num = input("Enter number: ")
#     if not num:
#         first = nums[0]
#         sum(*nums[1:], firstargt=first) # unpack
#         break
    # else:
        # nums.append(float(num))

# def register(*args, **kwargs):
#     profile = {}
#     for key, value in kwargs.items():
#         profile[key] = value
#     print("User registered: ", profile) 


# while True:
#     option = input("""Register
#         1. Username 2. Full name 3. Password: """)
#     if option == "1":
#         username = input("Username: ")
#         register(username=username)
#     elif option == "2":
#         fullname = input("Full name: ")
#         register(fullname=fullname)
#     elif option == "3":
#         password = input("Password: ")
#         register(password=password)

## assert
# def sum(*args):
#     res = 0
#     for num in args:
#         assert num.isnumeric()
#         res += int(num)
#     print(res)

# nums = []
# while True:
#     num = input("Enter number: ")
#     if not num:
#         sum(*nums) # unpack
#         break
#     else:
#         nums.append(num)

## importing from file
# from utils import sum, divide
# import utils

# print(utils, type(utils))
# print(utils.sum(1,2))
# print(divide(1,2))

# -------------------------------------------------------------------------

# pip libraries
## install
## sys
import sys
### argv
# print(sys.argv[1])
# print(sys.argv[2])

### exit(message)
# sys.exit(-1)

### path
# print(sys.path)

### maxsize
# print(sys.maxsize)

### getrecursionlimit, setrecursionlimit
# def func():
#     return func()

# sys.setrecursionlimit(100)
# print(sys.getrecursionlimit())

# func()

## os
import os
### _exit
# os._exit(-1)
### getcwd
# print(os.getcwd()) # C:\Users\nasiba.shahverdiyeva\Desktop\Python-101

### path.exists
# print(os.path.exists("C:\\Users\\nasiba.shahverdiyeva\\Desktop\\Python-1021"))

### path.join
# directory = input("Dir: ")
# file = input("File: ")
# print("Path:", os.path.join(directory, file))

### path.abspath
# print(os.path.abspath("ctf.txt"))
### path.dirname
### chdir
# print(os.getcwd())
# os.chdir("C:/Users/nijat.mansimov")
### listdir
# print(os.listdir())

### mkdir
# os.mkdir("salam")
# print(os.listdir())

### makedirs
# os.makedirs("yeni/bu/o") # mkdir -p

### remove
# os.rmdir("yeni")
# print(os.listdir())

### rmdir
### rename
print(os.path.isfile("C:\\Users\\nasiba.shahverdiyeva\\Desktop\\Python-101"))
## TASK: create a copy of a folder in another path

## random
### random
### randint
### seed
### choice
### shuffle
## TASK: number guess game

## base64
### encode/decode string
### altchars
### validate
### urlsafe_b64encode, urlsafe_b64decode
### encode/decode from/to file

## hashlib
## TASK: implement hash cracker given hash and mode (md5, sha256)

## json
### load from string
### load from file
### write to file
### set indent

## re
## TASK: file system scanner for sensitive files (e.g., passwords.txt) with regex
