print('Amigos! I am practicing python programming')

input1 = int(input("Value 1: "))
input2 = int(input("Value 2: "))

operator = input("Operator (+, -, *, /): ")

if operator == "+":
    print(input1 + input2)

elif operator == "-":
    print(input1 - input2)

elif operator == "*":
    print(input1 * input2)

elif operator == "/":
    print(input1 / input2)

else:
    print("Write the right operator: +, -, *, /")