try:
    print("Welcome to my Calculator")
    a = int(input("Enter the First Number: "))
    b = int (input("Enter the Second Number: "))

    print("What kind of operation you want to perform.\n Press + for addition.\n Press - for subtraction.\n Press / for Division\n Press * for multiplication")
    
    o = input("Enter the operation: ")

    match o:
        case "+":
            print(f"The result is: {a+b}")
        case "-":
            print(f"The result is: {a-b}")
        case "*":
            print(f"The result is: {a*b}")
        case "/":
            print(f"The result is: {a/b}")
        case default:
            print("Enter the valid operation")

except:
    print("Please enter the valid nuumber")  