sub_list=['mathematics','english','physics','chemistry','biology']
print(len(sub_list))
sub_list.append('history')
s=sub_list.sort()
print(sub_list.count('mathematics'))
print(s)
print(sub_list.index('mathematics'))
sub_list[3]='catering and crafts'
print(sub_list.reverse())
print(sub_list)
print(sub_list.remove('mathematics'))
sub_list.insert(3, 'civic')
print(sub_list)
print(sub_list.pop(3))
