# TASK: simple calculator
# Input -> Num1OperationNum2
# Operation -> + | - | * | / | // | :

while True:
    expression = input("Calculate: ")
    if "//" in expression:
        parts = expression.split("//")
        result = float(parts[0]) // float(parts[1])
    elif "/" in expression:
        parts = expression.split("/")
        result = float(parts[0]) / float(parts[1])
    elif "+" in expression:
        parts = expression.split("+")
        result = float(parts[0]) + float(parts[1])
    elif "-" in expression:
        parts = expression.split("-")
        result = float(parts[0]) - float(parts[1])
    elif "*" in expression:
        parts = expression.split("*")
        result = float(parts[0]) * float(parts[1])
    elif ":" in expression:
        parts = expression.split(":")
        result = float(parts[0]) % float(parts[1])

    print(result)