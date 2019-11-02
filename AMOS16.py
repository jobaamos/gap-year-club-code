#python program to print the least digit
def smallest_num_in_list(list):
    min=list[0]
    for a in list:
        if a<min:
            min=a
    return min
print(smallest_num_in_list([4,6]))
