def add(num1, num2):
 return num1 + num2
 
def sub(num1, num2):
 return num1 - num2
 
def mul(num1, num2):
 return num1 * num2
 
def div(num1, num2):
 return num1 / num2
 
def mod(num1, num2):
 return num1 % num2
 

num1 = int(input("Enter first number: "))
operation = input("specify operation(+, -, *, /, %):")
num2 = int(input("Enter second number: "))
 
result = 0
if operation == '+':
 result = add(num1,num2)
elif operation == '-':
 result = sub(num1,num2)
elif operation == '*':
 result = mul(num1,num2)
elif operation == '/':
 result = div(num1,num2)
elif operation == '%':
 result = mod(num1,num2)
else:
 print("Please enter: +, -, *, / or %")
 
print(result)
