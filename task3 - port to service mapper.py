# TASK: port to service mapper
# a. Run the program in while True loop until exit is selected
# b. Store a dictionary with default 5 ports
# c. Show options to user
## 1. Query a port -> take input from user, find it from dictionary and show service name to user. 
### 1.1 Check if port is valid
### 1.2 Show error if does not exist

## 2. Add a service -> take port from user, take name from user, add to dictionary 
### 2.1 Check if port not in dictionary -> Show error
### 2.2 Check if port not in range 1-65535 -> Show error
### 2.3 Check if service not in dictionary -> Show error
### 2.4 Check if service is empty -> Show error

## 3. List all services
### 3.1 Print all services in new line

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