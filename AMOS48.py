#python program that removes excess elements in the list
my_list=(input('enter a list of numbers'))
def remove(my_list):
    List=[]
    for num in my_list:
        if num not in List:
            List.append(num)
    return List
print(remove(my_list))
