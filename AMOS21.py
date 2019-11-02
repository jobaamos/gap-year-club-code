#python program to know if the user is either 18 or a nigerian before access can be granted
age=int(input('what is your age'))
country=(input('what country are you from'))
if age>=18 or country==('nigeria'):
    print('access granted')
else:
    print('access denied')
