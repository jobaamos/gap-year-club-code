#python program to sum up the factors of a number
div_sum=0
x=int(input('enter a number'))
print('the sum of the factors of', x, 'is')
for i in range(1, x + 1):
        if x % i==0:
            div_sum+=i
print(div_sum)
