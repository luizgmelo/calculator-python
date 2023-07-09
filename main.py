# type number
# operation
# another number
# result
firstNumber = int(input("Type a number: "))
operation = str(input("Type the operation: "))
secondNumber = int(input("Type another number: "))

if operation == "+":
    result = firstNumber + secondNumber
    print(f"{firstNumber} + {secondNumber} = {result}")
elif operation == "-":
    result = firstNumber - secondNumber
    print(f"{firstNumber} - {secondNumber} = {result}")
elif operation == "*" or operation == "x":
    result = firstNumber * secondNumber
    print(f"{firstNumber} x {secondNumber} = {result}")
elif operation == "/":
    result = firstNumber / secondNumber
    print(f"{firstNumber} / {secondNumber} = {result}")
else:
    print("Value is not valid, Try Again")
