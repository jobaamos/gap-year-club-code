#python program to sum up all the digits of a number
num=int(input('enter a number:'))
result=0
hold=num
while num>0:
   rem=num%10
   result=result+rem
   num=int(num/10)
print('the sum of all digits of',hold,'is',result)
