.
# difining addition function
def add(a,b):
    sum = a+b
    print(a,"+",b, "=",sum)

# difining  subtraction function
def subtract(a,b):
    difference = a-b
    print(a,"-",b,"=", difference)

#defining multiplcation function
def multiply(a,b):
    product = a*b
    print(a,"X",b,"=",product)

#defining division function
def divide(a,b):
    division = a/b
    print(a,"/",b,"=", division)

#printing the heading
print("WELCOME TO A SIMPLE CALCULATOR")

# using the while lopp to print menu list
while True :
    print("\n MENU")
    print("1. sum of two number")
    print("2. difference two number")
    print("3. product of two number")
    print("4. division of two number")
    print("5.exit")
    choice = int (input("\nenter the choice: "))

#using if-elif-else statement to pick different options
    if choice== 1:
        print("\nADDITION\n")
        a= int(input("first number :"))
        b = int(input("second number:"))
        add(a,b)


    elif choice == 2:
        print("\nSUBTRACTION\n")
        a = int(input("first number: "))
        b = int(input("second number: "))
        subtract(a,b)

    elif choice == 3:
        print("\nMULTIPLICATION\n")
        a= int(input("first number :"))
        b = int(input("second number:"))
        multiply(a,b)

    elif choice == 4 :
        print("\DIVISION\n")
        a= int(input("first number :"))
        b = int(input("second number:"))
        divide(a,b)

    elif choice == 5:
        break

    else:
        print("please provide a valid input !")
        
        
    
