# ---------------------------------DAY 4-----------------------------------

# loops
## for
# for i in range(1, 10):
#     print(i)

## range()
# print(list(range(1,10)))

## for loop
### list
# lst = ["salam", 1.5, -0.2, {}, {"a": {}}]
# for i in lst:
    # print(i)
    # for k in i:
        # print(k)
### string
# for i in list("sgfdfgdfgdfhgf"):
    # print(i)

### bytes
# for i in b"salam":
#     print(i)
### object keys(), values(), items()
obj = {"key1": "val1", "key2": [1,2,3]}
# for i in obj.keys():
#     print(i)
# for i in obj.values():
#     print(i)

# for kv in obj.items():
#     print(kv, type(kv))

# key1: val1
# key2: val2    
# for key, value in obj.items():
#     print(f"{key}: {value}")

### else
# for i in range(1, 10):
#     print(i)
#     if i == 55:
#         break
# else:
#     print("Here")

### reverswe loop
# for i in reversed(range(55, 60)):
#     print(i)

### step
# for i in range(0, 15, 2):
    # print(i) # only cut ededler

# for i in range(NUM) -> START=0, END=NUM, STEP=1
# for i in range(NUM1, NUM2) -> START=NUM1, END=NUM2, STEP=1
# for i in range(NUM1, NUM2, NU3) -> START=NUM1, END=NUM2, STEP=NUM3

### continue
# for i in range(1, 10):
#     if i == 6:
#         continue
#     print(i)
# else:
#     print("bitdi")
### break
# for i in range(1, 10):
#     if i == 6:
#         break
#     print(i)
# else:
#     print("bitdi")
### pass
for i in range(10):
    pass

## while loop
i = 2
# while i < 1000000000:
#     print(i)
#     i *= i
### else
# while i < 10:
#     print(i)
#     i *= i
#     if i > 10:
#         break
# else:
#     print("Bitdi")

## TASK: caesar cipher - encrypt, decrypt
## TASK: create patterns from a list of passwords

# -------------------------------------------------------------------------

# files
f = open("ctf.txt", "r+")
# print(f, type(f))
# print(dir(f))
## File methods - read, readlines
# print(type(f.readline()))
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(f"[+] {line}")
# f.close()
## File open modes - r, r+, w, w+, a, a+
## File methods - write, writelines
# f = open("temp", "w")
# f.write("salam\n")
# f.write("salam2")
# f.writelines(["salam\n", "salam2"])
# f.close()
## File methods - seek
# f = open("temp", "r")
# f.seek(6)
# print(f.readline())
# f.close()
## File open modes - r, r+, w, w+, a, a+
# f = open("temp", "a")
# f.write("3333333333")
# print(f.readline())
# f.close()
# with open("temp", "r") as f:
#     print(f.readlines())

# print(f.readlines())

## reading binary files
# with open("filemodes.png", "rb") as f:
#     print(list(f.read()))

## changing encoding
# with open("a", "r", encoding="utf-8") as f:
#     print(f.read())

## with keyword
## TASK: CTF challenge

# -------------------------------------------------------------------------

# Exceptions and Error handling
## try, except
## catch specific errors - e.g. zero division

# try:
    # print(int("here"))
    # a = [0,1,2][56]
    # 1/0
#     "fgfd" + 1
# except ZeroDivisionError:
#     print("0 a bolmek olmaz")
# except IndexError:
#     print("Bele index yoxdu")
# except ValueError:
#     print("Bu integer deyil axi!")
# except Exception as e:
#     print("Basqa error bas verdi: ", e)
## else
# try:
#     # 1/0
#     a = input("Birinci reqem: ")
#     b = input("Ikinci reqem: ")
#     c = int(a) * int(b)
# except:
#     print("Error")
# else:
#     print("Error cixmadi")
#     print(c)
## finally
# try:
#     # 1/0
#     a = input("Birinci reqem: ")
#     b = input("Ikinci reqem: ")
#     c = int(a) * int(b)
# except:
#     print("Error")
# else:
#     print("Error cixmadi")
#     print(c)
# finally:
#     print("Proqram bitdi")

## raise exception
# try:
#     a = input("Sozunu de: ")
#     if "salam" not in a:
#         raise Exception("Salam ver!")
# except Exception as e:
#     print(e)
# else:
#     print("Eleykime salam")

# -------------------------------------------------------------------------

# Functions
## code reuse
## recursive function
## default value for arguments
## *args **kwargs
## assert
## TASK: prime number detector - use exception handling
## TASK: apache log file analysis

# -------------------------------------------------------------------------

# pip
## sys
### argv
### exit(message)
### path
### maxint
### getrecursionlimit, setrecursionlimit

## os
### exit
### getcwd
### chdir
### listdir
### path.exists
### mkdir
### makedirs
### remove
### rmdir
### rename
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
