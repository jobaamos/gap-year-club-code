#python program that loops through series of questions and answers
questions = ['what is the capital of nigeria','what is the capital of lagos','who is the presidentof Nigeria','who is the president of the US']
answers = ['abuja','ikeja','buhari','trump']
num_score = 0
for i in range(len(questions)):
    users_input=input(questions[i]).lower()
    input(users_input)
    if users_input == answers[i]:
        #print('correct')
        num_score+=1
    #else:
        #print('wrong')
print('your total score is', num_score)
