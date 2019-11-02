#python program of a quiz
q=['who is the president of nigeria?','who is the president on the US?','what is capital of Nigeria?','what is the capital of lagos?']
a=['buhari','trump','abuja','ikeja']
score=0
for i in a:
    print(q.pop(0))
    v=(input('what is your answer?'))
    if v==a.pop(0):
        score+=1
        print('correct')
    else:
        print('wrong')
    print(q.pop(1))
    w=(input('what is your answer?'))
    if w==a.pop(1):
        score+=1
        print('correct')
    else:
        print('wrong')
        print(score)
        break

