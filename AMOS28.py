#python program to convert temperature units
a=eval(input('what is the temperature'))
b=(input('what unit is the given value in'))
g=(input('what unit do you want to change it to?'))
if b==('celsius') and g==('fahrenheit'):
    c=a*1.8
    d=32
    solution=c+d
    print(a, 'celsius in fahrenheit is', solution)
elif b==('celsius') and g==('kelvin'):
    h=a+273.15
    print(a, 'celsius in kelvin is', h)
elif b==('celsius') and g==('rankine'):
    q=a+273.15
    r=1.8
    s=q*r
    print(a, 'celsius in rankine is', s)
elif b==('fahrenheit') and g==('celsius'):
    e=a-32
    f=1.8
    solution=e/f
    print(a, 'fahrenheit in celsius is', solution)
elif b==('fahrenheit') and g==('kelvin'):
    i=a-32
    j=1.8
    k=273.15
    solution=i/j+k
    print(a, 'fahrenheit in kelvin is', solution)
elif b==('fahrenheit') and g==('rankine'):
    t=a+459.67
    print(a, 'fahrenheit in rankine is', t)
elif b==('kelvin') and g==('celsius'):
    l=273.15
    m=a-l
    print(a, 'kelvin in celsius is', m)
elif b==('kelvin') and g==('fahrenheit'):
    n=a*1.8
    o=459.67
    p=n-o
    print(a, 'kelvin in celsius is', p)
elif b==('kelvin') and g==('rankine'):
    u=a*1.8
    print(a, 'kelvin in rankine is', u)
elif b==('rankine') and g==('celsius'):
    v=a-491.67
    w=1.8
    x=v/w
    print(a, 'rankine in celsius is', x)
elif b==('rankine') and g==('fahrenheit'):
    y=a-459.67
    print(a, 'rankine in fahrenheit is', y)
elif b==('rankine') and g==('kelvin'):
    z=a/1.8
    print(a, 'rankine in kelvin is', z)

