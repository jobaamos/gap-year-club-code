#python program to know if at least one of two digits ends woth a 0
a=int(input('1st digit'))
b=int(input('2nd digit'))
if a%10==0 or b%10==0:
      print('yes')
else:
      print('no')
