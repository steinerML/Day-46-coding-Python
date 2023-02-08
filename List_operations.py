#List Operations

list1 = ["apple", "banana", "orange", "pineapple", "kiwi","avocado", "avocado"]

list2 = ['1', '2', '3','4','5','6','7']

#Length of the 1st and last element

print(len(list1[0]))
print(len(list1[-1]))

#Add element to list
list1.insert(0,'melon')
print(list1)

#Slicing elements: Last 2 elements
print(list1[-2:])

#Count elements in the list
print(list1.count('avocado'))

#Insert element at a given position
print(list1.insert(2, 'sugar cane'))
print(list1)

#Append element (at the end)
print(list1.append('coconut'))
print(list1)

#Index, returns index of a given element
print(list1.index('banana'))

#Remove element
list1.remove('coconut')
print(list1)

#Sort, sorts in alphabetical order.
list1.sort()
print(list1)

#Reverse list (List permanenelty modified)
list1.reverse()
print(list1)

#Sorted, sorts alphabetically without modifying list.
print(sorted(list1))
print(list1)

#Zip 2 lists together
new_list = list(zip(list1,list2))
print(new_list)

#List comprehension

a_list = [i**3 for i in (1,2,3)]
print(a_list)

#List comprehension

b = [i**4 for i in (1,2,3,4,5)]
print(b)

#Remove duplicates from a list.
h = [1,2,3,1,2,5]
new = list(set(h))
print(new)
