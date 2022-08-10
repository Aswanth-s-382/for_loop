print("********   WELCOME TO THE ZODIAC CALCULATOR   ********")
print("enter the number1 :")
num1=int(input())
print("enter the number2 :")
num2=int(input())
print("THESE ARE THE OPERATORS YOU CAN USE :")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication ")
print("4. Division")
print("5. Modulus")
operator=input("please choose an option from these (1,2,3,4,5):")
print("operator")
if operator=="1":
    print("This is an Addition Operation")
    print("The sum of two numbers is :",num1+num2)
if operator=="2":
    print("this is an Subtraction operation")
    print("The difference of two numbers is :",num1-num2)
if operator=="3":
    print("This is an Multiplication operation")
    print("The product of two numbers is :",num1*num2)
if operator=="4":
    print("This is an Division Operation")
    print("The difference between two numbers is :",num1/num2)
if operator=="5":
    print("This is an Modulus Operation")
    print("the mod od two numbers is :",num1%num2)

