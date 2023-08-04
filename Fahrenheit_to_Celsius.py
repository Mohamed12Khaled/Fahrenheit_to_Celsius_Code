x = int(input("if u want to convert to celsius enter 1 \n"
              "if u want to convert to fahrenheit enter 0"))
if x == 1:
    y = eval(input("enter the the degree in fahrenheit"))
    result = (y - 32) * 5/9
    print(result, "celsius")
if x == 0:
    z = eval(input("enter the the degree in celsius"))
    result = 9/5* (z) + 32
    print(result, "fahrenheit")