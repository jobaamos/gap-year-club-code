num_list=eval(input('enter a list of integers enclosed in a square bracket:'))
List=[]
x=List.append(num_list)
print(len(num_list))#prints the list of the integers
print(num_list[-1])#prints the last digit
num_list.reverse()#b=the reverse of the code
print(num_list)#prints b
for i in num_list:
    if 5 in num_list:#prints if theres a 5 in the list or not
        print('yes')
        break
    else:
        print('no')
        break
del num_list[0]#deletes the first digit
del num_list[-1]#deletes the last digit
num_list.sort()
print(num_list)
count=0
for i in num_list:
    if i < 5:
        count+=1
print(count)#prints the amount of digits that are less than 5
