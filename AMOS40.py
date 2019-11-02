#python program that prints the list if the users input is in the list 
sub_list=['mathematics','english','chemistry','biology','physics']
for sub in sub_list:
    a=(input('enter a subject'))
    if a in sub_list:
        print(sub_list)
        break
    else:
        print('not found')
        break
