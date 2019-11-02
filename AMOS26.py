#python program for a quiz
name=(input('what is your name?'))
print(name+' welcome to a cbt, be in order')
#the questions and answers
q1=print('what is the capital of Nigeria?')
a1=(input('what is the answer?'))
num_score=0
if a1==('abuja'):
    num_score+=1
    print('correct')
else:
      print('wrong')
q2=print('who is the president of Nigeria?')
a2=(input('what is your answer?'))
if a2==('buhari'):
    num_score+=1
    print('correct')
else:
    print('wrong')
q3=print('who is the president of the us?')
a3=(input('what is your answer?'))
if a3==('trump'):
    num_score+=1
    print('correct')
else:
    print('wrong')
q4=print('what does cchub stand for?')
a4=(input('what is your answer?'))
if a4==('co-creation hub'):
    num_score+=1
    print('correct')
else:
    print('wrong')
q5=print('what is the most populated state in Nigeria?')
a5=(input('what is your answer?'))
if a5==('lagos'):
    num_score+=1
    print('correct')
else:
    print('wrong')
print(name ,'your score is', num_score)
