my_list = ['terraform','aws','linux','devops', 2, 5.6, True, 2, 1 , 1]

#List Methods .append() , .pop(), .clear(), .copy() , change item, len(), extend(), insert(), .count()

print(len(my_list))

my_list.append( 'Huston' )
print(my_list)
my_list[0]= 'Terraform'
print(my_list)
print(my_list[-1].upper())
my_list.extend([10,56,78,'utrains'])
print(my_list)
print(dir(my_list))
my_list.insert(2, 'kouadio')
print(my_list)