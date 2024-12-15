# TASK: create a copy of a folder in another path
# Input 1: in folder path
# Input 2: out folder path
# Check
## If folder exists - falsedisa error ver cix
## Check if folder - filedisa error ver cix
## How to:
### List files in in folder
### Get their absolute path
### Extract directory portion using os.path.dirname()
### Create using makedirs
### Eger o folderda path var idise icinde onlari yarat - f"{dirname}/{filename}"

import sys

inpath = input("Input path: ")
output = input("Output path: ")
# check if inpath exists
## false -> exit
## true -> check if file
### true -> exit
### false -> 
#### listdir content of folder
#### iterate over folder content. for each item
##### check if file -> truedisa fayl yarat (open), deyilse folder yarat
##### folderdisa -> outpathde folder yarat, inputdaki inner folderi listdir et
import os

def recurse(inpath, outpath):
    content = os.listdir(inpath)
    for item in content
    if item is folder:
        create folder in outpath
        recurse(path + folder, outpath+folder)
    else:
        create file

recurse(inpath, outpath)