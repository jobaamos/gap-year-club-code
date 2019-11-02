#python program to print a comment for a student's grade
grade=(input('what is your grade'))
name=(input('what is your name'))
if grade==('a'):
    print('congratulations' +name+ ' you got an A')
elif grade==('b'):
    print('congratulations' +name+ ' you got a B')
elif grade==('c'):
    print('congratulations' +name+ ' you got a C')
elif grade==('d'):
    print('ooops' +name+ ' you failed with a D')
elif grade==('e'):
    print('ooops' +name+ ' you failed woefully with an E')
elif grade==('f'):
    print(name+' you failed drastically with an F')
