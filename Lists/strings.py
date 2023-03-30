# string = 'spam spam spam'
# lst = string.split()
# print('@'.join(lst))

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1[:]
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

print(fruit_list1)
print(fruit_list2)
print(fruit_list3)
