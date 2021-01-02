# calculator 

operator = input("enter your operator '+','-','*','/'):"
num1 = int(input("enter your first number:"))
num2 = int(input("enter your secand number:"))

if operator == "+":
   print( num1 +num2)
elif operator == "-":
   print( num1- num2)
elif operator == "*":
   print( num1 * num2)
elif operator == "/":
   print( num1 / num2)
else :
   print("Are you kidding me!!!")

