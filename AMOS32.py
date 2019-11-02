#python program to print if a number is prime or not
num=int(input('what is the number'))
for i in range(2,num):
    if num%i==0:
        print('it is not a prime number')
        break
else:
    print('it is a prime number')
