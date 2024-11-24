# TASK: IP address format validator
# Input: 555.555.555.555, 5.5.5.5, 5.5.5
# Output: valid or not
'''
while True:
    counter =0
    a=input("enter the ip addr: ")
    var = a.split(".")

    if( len(var)<=3):
        counter+=1
        print("sehvdir")
        break

    ip1=int(var[0])

    if (ip1>255 or ip1<=0):
       counter+=1

    ip2=int(var[1])

    if (ip2>255 or ip2<0):
        counter+=1

    ip3=int(var[2])

    if (ip3>255 or ip3<0):
     counter+=1

    ip4=int(var[3])


if (ip4>255 or ip4<0):
    counter+=1


if (counter>0):
    print("ip sehvdir")
else:
    print("duzdur")

'''
ip = input("Enter ip: ")
splitted = ip.split(".")
if len(splitted) != 4:
    print("Invalid length")
else:
    correct = 0
    for i in range(4):
        octet = splitted[i]
        if not octet.isnumeric():
            print("Invalid ip")
            break
        octet = int(octet)
        if octet > 255 or octet < 0:
            print(f"{i+1}. octet  is invalid")
        else:
            correct += 1
    if correct == 4:
        print("Valid ip")
    else:
        print("Invalid ip")