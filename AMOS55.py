#python program that counts the amount of letters in a string excluding the spaces
s=(input('enter a sentence'))
count=0
g=len(s)
#print(g)
for i in s:
    if ' ' in i:
        count+=1
print(g -count)
    
