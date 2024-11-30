with open("ctf.txt", "r") as f:
    lines = f.readlines()

for line in lines[2:]:
    codes = line.split(" ")
    decodedline = "".join([chr(int(i)) for i in codes])
    # for i in codes :
    #     decodedchar=chr(int(i))
    #     decodedline+=decodedchar
    # print(decodedline)
    # print(decodedline.split(" ")[1] if "PassWoRd" in decodedline else None)
    if "PassWoRd" in decodedline:
        print(decodedline.split(" ")[1])
        
        