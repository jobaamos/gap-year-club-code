#python program to print a receipt according to the buyer's quantity
a=12
b=10
c=7
d=10
e=99
g=100
f=int(input('how many items are you buying?'))
if f<=d:
    price=f*a
    print('your total price is', price)
elif f<=e:
    price=f*b
    print('your total price is', price)
elif f>=g:
    price=f*c
    print('your total price is', price)
    
