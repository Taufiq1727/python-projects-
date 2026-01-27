try:
    a = int(input("Enter the first number :"))

    b = int(input("Enter the second number :"))


    print("What kind of operation do you want to perform. press + for addition\npress - for subtraction\npress / for division\npress * for multiplication")

    o = input("Enter Operation :")
    match o :
        
        case "+":
            print(f"The result is  : {a+b}")
        case "-":
            print(f"The result is  : {a-b}")
        case "/":
            print(f"The result is  : {a/b}")
        case "*":
            print(f"The result is  : {a*b}")
except Exception as e:
    print("Enter a valid value of a and b")