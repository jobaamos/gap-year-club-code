#python program to print the heighest digit out of two
while True:
    print("enter 'x' for exit.")
    print("enter two numbers;")
    num1=input()
    num2=input()
    if num1=='x':
           break
    else:
           number1=int(num1)
           number2=int(num2)
           if number1>number2:
                   largest=number1
           else:
                   largest=number2
           print("largest of entered two numbers is", largest,"\n")
