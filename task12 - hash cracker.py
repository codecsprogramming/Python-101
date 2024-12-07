# TASK: implement md5 hash cracker
# Take 2 inputs from command line
# 1. hash 2. wordlist
# python hashcracker.py hashinozu words.txt
# 482c811da5d5b4bc6d497ffa98491e38

import sys
import hashlib

if len(sys.argv) < 3:
    print("[-] Usage: python crackpy hash wordlist")
    sys.exit()

input_hash = sys.argv[1]
wordlist = sys.argv[2]
with open(wordlist, "r") as f:
    passwords = f.readlines()
    for i in range(len(passwords)):
        password = passwords[i].strip()
        digest = hashlib.md5(password.encode()).hexdigest()
        if digest == input_hash:
            print(f"[+] Hash cracked at {i+1}. attempt: {password}")
            sys.exit()