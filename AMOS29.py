#python program to comply marks after quiz being conducted
name=(input('what is your name'))
print(name+ ' welcome to quick Qs and As')
q1=print('how many colours does the Nigerian flag have?')
print('(a)4 (b)3 (c)2')
a1=(input('what is your answer?'))
score=0
if a1==('c'):
    score+=1
    print('correct')
else:
    print('wrong')
q2=print('what year was Nigeria gain her independence?')
print('(a)1960 (b)1963 (c)1965')
a2=(input('what is your answer?'))
if a2==('a'):
    score+=1
    print('correct')
else:
    print('wrong')
q3=print('After how many years is a re-election conducted in Nigeria?')
print('(a)4 (b)5 (c)6')
a3=(input('what is your answer?'))
if a3==('a'):
    score+=1
    print('correct')
else:
    print('wrong')
print(name, ' your total score is', score)
