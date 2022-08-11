replace1=""
flag="print"
print("********    Welcome to Calculator   ********")
num1=int(input("enter a number1:"))
print(num1)
num2=int(input("enter a number2:"))
print(num2)
print("These are the operators you can use: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
result="0"
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator=='1':
    replace1="Addition"
    result=num1+num2
if operator=="2":

    if num1<num2:
        flag="do not print"
        print("cannot subtract the first number is less than the second number")
    else:
        flag="print"
    replace1="Subtraction"
    result=num1-num2
if operator=="3":
    replace1="Multiplication"
    result=num1*num2
if operator=="4":
    replace1="Division"
    result=num1//num2
if operator=="5":
    replace1="Modulus"
    result=num1%num2
if flag=="print":
 print("The result of",replace1,"of",num1,"and",num2,"is",result)

