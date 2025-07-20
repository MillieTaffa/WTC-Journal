def calculator():
    expression = input("Expression: ").strip()
    x,op,y = expression.split()
    x = float(x)
    y = float(y)

    if op == "+":
        print(round(x + y,1))
    elif op == "-":
        print(round(x - y,1))
    elif op == "*":
        print(round(x * y,1))
    elif op == "/":
        print(round(x / y,1))
    else:
        print("Inavlid")
calculator()
