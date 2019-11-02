#python program to guess the computers hidden digit
from random  import randint
y=randint(1,10)
x= int ( input('what is your number'))
print ("Computer's number is", (y))
print ("Your number is",x)
if (y)==(x):
    print ('So you are correct')
else:
    print ('So you are wrong')
