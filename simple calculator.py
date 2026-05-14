#calculator mini project
#simple calculator progarm
while True:
    def add(a,b): 
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def division(a,b):
        if b==0:
            return "Cannot divide by zero"
        return a/b
    print("simple calculator \n 1.Addition \n 2.Subtraction \n 3.Multipliation \n 4.Division")
    choice=int(input("Enter your choice (1-4):"))
    num1=int(input("enter the first number: "))
    num2=int(input("enter the second number: "))
    if choice==1:
        print("Result: ",add(num1,num2))
    elif choice==2:
        print("Result: ",subtract(num1,num2))
    elif choice==3:
        print("Result: ",multiply(num1,num2))
    elif choice==4:
        print("Result: ",division(num1,num2))
    else:
        print("Invalid Choice")
        
    

      
           
