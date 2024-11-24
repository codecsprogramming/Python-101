# ---------------------------------DAY 3-----------------------------------

# list, tuple, dictionary, set
## list
lst = []
### add item
# ret = lst.append("necesen")
# print(lst)
### add 2 lists
lst2 = ["salam", "yaxsiyam"]
lst += lst2
lst += lst2
# print(lst)
### remove
ret = lst.remove("salam")
# print(ret)
# print(lst)
### pop
# print(lst)
removed_element = lst.pop(1)
# print(removed_element)
### count
# print(lst.count("salam")) 
### copy
lst3 = lst.copy()
# print(lst)
# print(lst3)
lst.append("1")
# print(lst)
# print(lst3)
### insert
# print("Before:", lst)
# lst.append("salam2")
# print("Append:", lst)
# lst.insert(2, "salam3")
# print("Insert:", lst)
### sort
array = [5, 1, 4, 5, 7, 8]
# print("Before:", array)
# array.sort()
# print("Sort:", array)
# print("Sorted:", sorted(array))
# print("After sorted:", array)
### reverse method, reversed function
# print("Reversed:", reversed(array))
# for el in reversed(array):
#     print(el)
# print("After reversed:", array)
# array.reverse()
# print("After reverse:", array)
### del keyword
# array = [5, 1, 4, 5, 7, 8]
# del array
# print(array) # NameError: name 'array' is not defined. Did you forget to import 'array'?

### list comprehension
# lst = []
# for i in range(10):
#     lst.append(i)
# print(lst)
# lst2 = [chr(i).lower() for i in range(61, 70)]
# obj = {key+"1": value+"1" for key, value in {"a": "1"}.items()}
# print(obj)
# print(lst2)
### str->list, list->str, list->bytes, bytes->list
# soz = "Azerbaycan"
# print(list(soz)) # ['A', 'z', 'e', 'r', 'b', 'a', 'y', 'c', 'a', 'n']
# print([i.upper() for i in soz]) # ['A', 'Z', 'E', 'R', 'B', 'A', 'Y', 'C', 'A', 'N']
# lst = ["a", "b", "d", "c"]
# print(".".join(lst[:-1])) # a.b.d
# lst = [56, 62]
# print(bytes(lst).decode())
# print("8>".encode())
# for i in "8>".encode():
#     print(i)

## tuple (immutable)
tup = (1, 2, 1)
tup2 = (3, 4)
# print(len(tup))
# print(tup, type(tup), dir(tup))
# print(tup.count(1)) # 2
# print(tup.index(2)) # 1

# def func():
#     return 1, 2, 3

# print(type(func()))

## dict
dict2 = {"key": "value", "key2": 1}
# print(dict2["key3"][1])
# print(dict2["key4"]["key5"]["key6"])
# print(dict2["key2"]) # indexed, unordered, mutable
# dict2["key2"] = 4
# print(dict2) # {'key': 'value', 'key2': 3, 'key3': 2}
# print(dir(dict2))

### add item to dict
# dict2["key3"] = 2
### delete item
# deleted = dict2.pop("key3")
# print(dict2, deleted) # {'key': 'value', 'key2': 1, 'key0': {'key5': {'key6': 'value'}}} [1, 2, 4]

### dynamic key value for dict
# key = input("Add a key: ")
# value = input("Value: ")
# if value.isnumeric():
#     value = float(value)
# dict2[key] = value
# print(dict2)

### dict.update
# old = {"key": "value", "key2": 1}
# new = {"key": [123]}
# print("Before:", old)
# old.update(new)
# print("After:", old)

### keys
dict2 = {"key": "value", "key2": 1, "1": 2}
# while True:
#     key = input("What do you want: ")
#     if key in dict2:
#         print(dict2[key])
#     else:
#         print("This key does not exist")
#         break
# print(old.keys())
# for key in old.keys():
    # print(key)
### values
# print(old.values())

## set (mutable, no index, no duplicate, unordered)
# set1 = set([1,2,3,1])
# print(set1, type(set1))
### assign item (!)
# set1[0] = 5
# print(set1) # error
### add item
# set1.add(6)
# print(set1)
# ### remove item
# set1.remove(1)
# print(set1)

## TASK: port to service mapper

# -------------------------------------------------------------------------

# if/elif/else
# print(1 == 1 or 2 == 3, type(1 == 1 or 2 == 3))
# if 1 == 1 or 2 == 3:
#     print("Here")
# elif 2==2:
#     print("There")
# else:
#     print("Nowhere")
## falsy expressions
# var = False
# var = 0
# var = []
# var = {}
# var = ""
# var = None
# print(not {})
# inp = input("Enter something: ")
# if inp:
#     print("Not empty:", inp)
# else:
#     print("Empty")
# if not var:
#     print("True")
# else:
#     print("False")

## and or, priority
## grouping

# if 1 == 1 and 2 == 1 or 1 == 4 or 3==4 or 2 == 3 and 3==3:
#     print("Here")
# else:
#     print("There")
## one-liner syntax - ternary
print(1 if 1 == 2 else (2 if 3 == 2 else 5))
# RESULT1 IF COND1 ELSE (RESULT2 IF COND2 ELSE (RESULT3 IF COND3 ELSE RESULT4))

## TASK: IP address format validator
