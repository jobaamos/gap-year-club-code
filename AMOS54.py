#python program that removes the first letter of all the elements in the list
L=[]
for i in range(3):
    user_input = input('enter a list')
    L.append(user_input)
#print(L)
Li = []
for j in L:
    g = j[1:]
    Li.append(g)
print(Li)
