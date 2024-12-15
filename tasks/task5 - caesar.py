# TASK: caesar cipher
# plaintext - p
# key - k
from string import ascii_lowercase
alphabet = list(ascii_lowercase)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Len alpha: ", len(alphabet))
plain = input("Plaintext: ")
key = int(input("Key: "))
cipher = ""
for letter in plain:
    # find index of letter in alphabet
    if letter not in alphabet:
        print("Invalid plaintext")
        break
    index = alphabet.index(letter)
    
    # find new index
    print("Index:", index)
    added = (index + key)
    print("After add:", added)
    if added > len(alphabet) - 1:
        new_index = added - len(alphabet)
    else:
        new_index = added
    print("after division:", new_index)
    # find letter in new index
    new_letter = alphabet[new_index]
    cipher += new_letter

print("Cipher: ", cipher)