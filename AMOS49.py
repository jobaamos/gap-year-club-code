#python program that removes the first letter of all the words listed
L=[]
for i in range(3):
    user_input = input('enter words')
    L.append(user_input)
#print(L)
Li = []
for j in L:
    g = j[1:]
    Li.append(g)
print(Li)
