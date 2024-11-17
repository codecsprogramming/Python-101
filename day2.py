# ---------------------------------DAY 2-----------------------------------

# string methods (cont.)
var = """Weather is good today
I want to go out"""
# print("A".join(var.split())) # WeatherAisAgoodAtodayAIAwantAtoAgoAout

## lstrip, rstrip, strip
var = "    salam    "
# print(var.strip(), "salam")  # salam salam
# print(var.strip()+"salam")   # salamsalam
# print(var.lstrip(), "salam") # salam       salam
# print(var.rstrip(), "salam") #     salam salam

## lower, upper
var = "Hello world"
# print(var.upper()) # HELLO WORLD
# print(var.lower()) # hello world

## find, rfind VS index
var = "Hello world! I am Vusala. I live on the world"
# print(var.find("world1"))  # -1
# print(var.index("world1")) # error

# print(var.find("world")) # 6
# print(var.rfind("world")) # 40
# print(var.find("world")) # 6

# TASK: find all occurences

## replace
var = "Hello world! I am Vusala. I live on the world"
# print(var.replace("world", "mars", 1)) # Hello mars! I am Vusala. I live on the world

## quote inside quote - escaping
# print("Kitabin adi 'Sefiller\"") # Kitabin adi 'Sefiller"
# print('Kitabin adi "Sefiller\'') # Kitabin adi "Sefiller'

## dir function
var = "Hello world! I am Vusala. I live on the world"
# print(dir(var))

# -------------------------------------------------------------------------

# encoding, decoding
## UTF-8
var = "string"
# var = var.encode("utf-8")
# print(var, type(var))
# print(list(var)) # [115, 116, 114, 105, 110, 103]
# print(var.decode('utf-8'))
# print(type(b"string")) # <class 'bytes'>
# print(b"string"[0]) # 115

## Ascii
# var = var.encode("ascii")
# print(var[0])

## chr/ord
# print(ord("s")) # 115
# print(chr(115)) # s

## bytes(), bytearray()
# var = bytearray("salam".encode())
# var[0] = 116
# print(var)
# var = bytes("salam".encode())
# var[0] = 116 # error

## bytes -> hex
# print(b"string".hex()) # 737472696e67

## hexlify
# import binascii
# print(binascii.hexlify(b"string").decode()) # from bytes to hex
# print(bytes.fromhex("737472696e67").decode()) # from hex to ascii

# string formatting
## f-string
# name = "John"
# var = f"Hello {name}"
# print(var) # Hello John

### {{ in f-string
# name = "John"
# var = f"Hello {{ {name} }}" # Hello { John }
# print(var)

### expression in {}
# var = f"2 + 2 = {2+2}"
# print(var) # 2 + 2 = 4
# var = f"4 * A = {'A'*4}"
# print(var) # 4 * A = AAAA
# var = f"Ascii value of Z is {ord('Z')}"
# print(var) # Ascii value of Z is 90
# print(int("14", 16)) # convert from 16 base to 10 base = 20

## format
# var = "My name is {}"
# print(var.format("John")) # My name is John
# var = "My name is {}. I live in {}"
# city = "Baku"
# print(var.format("John", city)) # My name is John. I live in Baku

### named argument
# var = "My name is {name}. I live in {city}. I am {age} years old."
# print(var.format(name="John", city="Baku", age=15))

### Precision {price:.2f}
# price = 100.156789
# print("Price is {:.2f}".format(price)) # Price is 100.16
# print("Price is {:.3f}".format(price)) # Price is 100.157

### :c - unicode | :b :B - binary | :e :E  - scientific format | :x :X - hex | :% - percentage format
# print(f"Unicode of 125 is {111:c}")
# print(f"Unicode of 125 is {111:b}")
# print(f"Unicode of 125 is {111:e}")
# print(f"Unicode of 125 is {111:E}")
# print(f"Unicode of 125 is {111:x}")
# print(f"Unicode of 125 is {111:X}")
# print(f"Unicode of 125 is {0.4:%}")
# a = f"{111:x}"
# print(a)

# TASK: take input from user and print encoded string based on choice: 1. utf-8, 2. hex, 3. binary
# TASK: simple calculator

# -------------------------------------------------------------------------

# list, tuple, dictionary, set
## list
### add item
### add 2 lists
### remove
### pop
### count
### copy
### insert
### sort
### reverse method, reversed function
### del keyword
### list comprehension
### str->list, list->str, list->bytes, bytes->list

## tuple (immutable)

## dict
### add item to dict
### delete item
### dynamic key value for dict

## set (mutable, no duplicate, unordered)
### assign item (!)
### add item
### remove item

## dir function
### trying  methods in different data types

# -------------------------------------------------------------------------

# if/elif/else
## falsy expressions
## and or, priority
## grouping
## TASK: simple calculator
## TASK: IP address format validator

