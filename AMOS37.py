#python program to sum up the factorial of a number
num=int(input('enter a number'))
fac=1
fac_sum=0
for i in range(1, num+1):
    fac=fac*i
    fac_sum+=fac*1
print(fac_sum)
