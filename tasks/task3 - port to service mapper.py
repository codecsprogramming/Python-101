# TASK: port to service mapper
# a. Run the program in while True loop until exit is selected
# b. Store a dictionary with default 5 ports - ports are keys, service names are values
# c. Show options to user in every iteration
## 1. Query a port -> take input from user, find it from dictionary and show service name to user. 
### 1.1 Check if port exists in dictionary

## 2. Add a service -> take port from user, take name from user, add to dictionary 
### 2.1 Check if port is numeric
### 2.2 Check if port in range 1-65535
### 2.3 Check if port not in dictionary keys
### 2.4 Check if service is empty
### 2.5 Check if service not in dictionary values

## 3. List all services
### 3.1 Print all services in new line
#### port -> servicename 

## 4. Exit - break out of loop

services = {
    22: "ssh",
    25: "smtp",
    80: "http",
    443: "https"
}
menu = """Port to service mapper
1. Query a port
2. Add a service
3. List all services
4. Exit
Select an option: """
while True:
    option = input(menu)
    if option == "1":
        continue
    elif option == "2":
        port = input("Enter a port: ")
        service = input("Enter service name: ")
        continue
    elif option == "3":
        continue
    else:
        print("Invalid option") 