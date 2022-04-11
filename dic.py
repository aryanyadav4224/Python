a_dict = {'Yellow': 'Marigold', 'Red': 'Rose', 'White': 'Lilly'}

a_list = ['Black', 'Purple']

dict_copy = a_dict.copy()
a_list.append(dict_copy)

# accessing dictionary values
dict_access = a_list[2]
dict_access1 = a_list[2]['Red']
dict_access2 = a_list[2]['White']

#printing 
print(dict_access)
print(dict_access1)
print(dict_access2)