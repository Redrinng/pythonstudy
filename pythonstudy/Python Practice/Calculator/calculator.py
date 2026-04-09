print("1 - Osszeadas")
print("2 - Kivonas")
print("3 - Szorzas")
print("4 - Osztas")
option = int(input("Choose an operation:"))
result = 0

if(option in [1,2,3,4]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if(option == 1):
            result = num1 + num2
    elif(option == 2):
            result = num1 - num2
    elif(option == 3):
            result = num1 * num2
    elif(option == 4):
            result = num1 / num2
else:
    print("Invalid operation entered")

print("Result: {}".format(result))
