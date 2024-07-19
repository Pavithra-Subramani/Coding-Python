num1=int(input("enter the num1 :"))
num2=int(input("enter the num2 :"))
num3=int(input("enter the num3 :"))
if (num1 > num2)and(num1 > num3):
    print("Number 1 is Greater")
elif(num2 >num1) and(num2 > num3):
    print("number 2 is greater")
elif(num3 >num1) and (num3 >num2):
    print("number 3 is greater")
else:
    print("invalid number")
    
    
